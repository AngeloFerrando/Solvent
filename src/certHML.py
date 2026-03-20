#!/usr/bin/env python3
import re
import sys
import os
import subprocess


def find_matching_brace(text, start):
    """Return index of '}' matching the '{' at position start, skipping // comments."""
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == '/' and i + 1 < len(text) and text[i + 1] == '/':
            # skip to end of line
            while i < len(text) and text[i] != '\n':
                i += 1
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def get_all_rule_names(text):
    """Return a list of all active (non-commented) rule names in order."""
    pattern = re.compile(r'^[ \t]*rule\s+(\w+)\s*\{', re.MULTILINE)
    rules = []
    for match in pattern.finditer(text):
        name = match.group(1)
        brace_pos = match.end() - 1
        brace_end = find_matching_brace(text, brace_pos)
        if brace_end != -1:
            rules.append((match.start(), brace_end, name))
    return rules


def remove_other_rules(text, property_name, rules=None):
    """Remove every active (non-commented) rule block except the one named property_name."""
    if rules is None:
        rules = get_all_rule_names(text)

    if not any(name == property_name for _, _, name in rules):
        raise ValueError(f"Active rule '{property_name}' not found in file")

    # Build result: keep non-rule text and only the target rule
    parts = []
    prev = 0
    for rule_start, rule_end, name in rules:
        parts.append(text[prev:rule_start])
        if name == property_name:
            parts.append(text[rule_start:rule_end + 1])  # include '}'
        prev = rule_end + 1
    parts.append(text[prev:])
    return ''.join(parts)


def run_for_property(text, contract, property_name, n_of_participants, timeout):
    """Run the full verification pipeline for a single property."""
    # Only emit filtered Kind2 summary lines (no extra headings)
    modified_text = remove_other_rules(text, property_name)

    os.makedirs('tmp', exist_ok=True)
    with open('tmp/verification_task.sol', 'w') as f:
        f.write(modified_text)

    # Step 1: translate to Lustre (suppress verbose translator output)
    cmd1 = ['python3', 'src/main_test.py', 'tmp/verification_task.sol', '2', n_of_participants]
    r1 = subprocess.run(cmd1, capture_output=True, text=True)
    if r1.returncode != 0:
        if r1.stdout:
            print(r1.stdout, end='')
        if r1.stderr:
            print(r1.stderr, end='', file=sys.stderr)
        print(f"main_test.py exited with code {r1.returncode}", file=sys.stderr)
        return r1.returncode

    # Step 2: run Kind2 and capture output into a temporary file to avoid direct tty writes
    cmd2 = ['kind2/kind2', 'out/outputTrace.lus', '--smt_solver', 'cvc5', '--timeout', timeout]
    os.makedirs('tmp', exist_ok=True)
    raw_path = 'tmp/kind2_raw.out'
    with open(raw_path, 'w') as fout:
        r2 = subprocess.run(cmd2, stdout=fout, stderr=subprocess.STDOUT, text=True)
    with open(raw_path, 'r') as fin:
        full_output = fin.read()

    # Strip ANSI escape sequences (kind2 prints colored output)
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    clean_output = ansi_escape.sub('', full_output)

    # Extract only the "Summary of properties" section and print the property lines
    summary_lines = []
    if 'Summary of properties:' in clean_output:
        idx = clean_output.find('Summary of properties:')
        tail = clean_output[idx:]
        for line in tail.splitlines():
            s = line.strip()
            if not s:
                continue
            if s.startswith('Summary of properties:'):
                continue
            if s.startswith('----') or s.startswith('==='):
                continue
            # Accept lines that look like "<name>: <status>"
            if ':' in s:
                # ignore header-like lines that are not property summaries
                if any(k in s for k in ['Analyzing', 'Summary', 'System']):
                    continue
                summary_lines.append(s)

    # Fallback: if we couldn't parse a summary, include last 40 chars of output
    if not summary_lines:
        summary_text = full_output.strip()
        if len(summary_text) > 2000:
            summary_text = summary_text[-2000:]
        print(summary_text)
        output_to_save = summary_text
    else:
        output_to_save = '\n'.join(summary_lines)
        print(output_to_save)

    # Save results (only the filtered summary)
    contract_base = os.path.basename(contract)
    os.makedirs('out_results', exist_ok=True)
    out_path = f"out_results/{contract_base}_{property_name}_{n_of_participants}_{timeout}.out"
    with open(out_path, 'w') as f:
        f.write(output_to_save)
    return 0


def main():
    if len(sys.argv) != 5:
        print("Usage: certHML.py <contract> <property|ALL> <n_of_participants> <timeout>")
        sys.exit(1)

    contract = sys.argv[1]
    property_name = sys.argv[2]
    n_of_participants = sys.argv[3]
    timeout = sys.argv[4]

    # Read the contract file (never modify the original)
    with open(contract, 'r') as f:
        text = f.read()

    if property_name == 'ALL':
        rules = get_all_rule_names(text)
        if not rules:
            print("No active rules found in the contract.")
            sys.exit(1)
        exit_code = 0
        for _, _, name in rules:
            rc = run_for_property(text, contract, name, n_of_participants, timeout)
            if rc != 0:
                exit_code = rc
        sys.exit(exit_code)
    else:
        rc = run_for_property(text, contract, property_name, n_of_participants, timeout)
        sys.exit(rc)


if __name__ == '__main__':
    main()
