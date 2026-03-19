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


def remove_other_rules(text, property_name):
    """Remove every active (non-commented) rule block except the one named property_name."""
    # Match only lines that begin with optional whitespace then 'rule'
    pattern = re.compile(r'^[ \t]*rule\s+(\w+)\s*\{', re.MULTILINE)

    # Collect (rule_start, brace_end, name) for all active rules
    rules = []
    for match in pattern.finditer(text):
        name = match.group(1)
        brace_pos = match.end() - 1  # regex ends with '\{', so last char is '{'
        brace_end = find_matching_brace(text, brace_pos)
        if brace_end != -1:
            rules.append((match.start(), brace_end, name))

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


def main():
    if len(sys.argv) != 5:
        print("Usage: certHML.py <contract> <property> <n_of_participants> <timeout>")
        sys.exit(1)

    contract = sys.argv[1]
    property_name = sys.argv[2]
    n_of_participants = sys.argv[3]
    timeout = sys.argv[4]

    # Read the contract file (never modify the original)
    with open(contract, 'r') as f:
        text = f.read()

    # Build modified text containing only the target rule
    modified_text = remove_other_rules(text, property_name)

    # Write to tmp/verification_task.sol
    os.makedirs('tmp', exist_ok=True)
    with open('tmp/verification_task.sol', 'w') as f:
        f.write(modified_text)

    # Step 1: translate to Lustre
    cmd1 = ['python3', 'src/main_test.py', 'tmp/verification_task.sol', '2', n_of_participants]
    print(f"Running: {' '.join(cmd1)}")
    r1 = subprocess.run(cmd1, capture_output=True, text=True)
    if r1.stdout:
        print(r1.stdout, end='')
    if r1.stderr:
        print(r1.stderr, end='', file=sys.stderr)
    if r1.returncode != 0:
        print(f"main_test.py exited with code {r1.returncode}", file=sys.stderr)
        sys.exit(r1.returncode)

    # Step 2: run Kind2
    cmd2 = ['kind2/kind2', 'out/outputTrace.lus', '--smt_solver', 'cvc5', '--timeout', timeout]
    print(f"Running: {' '.join(cmd2)}")
    r2 = subprocess.run(cmd2, capture_output=True, text=True)
    output = r2.stdout
    if r2.stderr:
        output += r2.stderr
    print(output, end='')

    # Save results
    contract_base = os.path.basename(contract)
    os.makedirs('out_results', exist_ok=True)
    out_path = f"out_results/{contract_base}_{property_name}_{n_of_participants}_{timeout}.out"
    with open(out_path, 'w') as f:
        f.write(output)
    print(f"\nResults saved to {out_path}")


if __name__ == '__main__':
    main()
