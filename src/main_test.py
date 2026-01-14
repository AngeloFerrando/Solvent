from Kind2Visitor import *
from TypeVisitor import *

from antlr4.error.ErrorListener import ErrorListener
import sys
import os
import re

class TxScriptErrorListener( ErrorListener ):
    def __init__(self):
        super(TxScriptErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error: " + msg)

def parse(pattern):
    if len(sys.argv) != 4 and len(sys.argv) != 6:
        print('The script requires 3 parameters (plus two optional ones which are True and -1 by default), as follows: <name of the SOL file> <number of transactions> <number of participants> (<accept transactions any time> <fixed_iteration>)?')
        return
    
    lexer = TxScriptLexer(InputStream(pattern))
    stream = CommonTokenStream(lexer)
    parser = TxScriptParser(stream)
    parser.addErrorListener(TxScriptErrorListener())
    tree = parser.contractExpr()

    can_transactions_arrive_any_time = (sys.argv[4]=='True' or sys.argv[4]=='true') if len(sys.argv) == 6 else True
    fixed_iteration = int(sys.argv[5]) if len(sys.argv) == 6 and sys.argv[5] != '-1' else -1

    type_visitor = TypeVisitor()
    visitor = Kind2Visitor(int(sys.argv[2]), int(sys.argv[3]), True, can_transactions_arrive_any_time, fixed_iteration)

    isExist = os.path.exists('./out')
    if not isExist:
        os.makedirs('./out')
    try:
        type_visitor.visit(tree)
    except Exception as e:
        print(e)
        return
    # try:
    with open('./out/outputTrace.lus', 'w') as file:
        res = visitor.visit(tree)
        file.write(re.sub(r'a0_tx\d*', 'a0', res))
    # visitor = Kind2Visitor(int(sys.argv[2]), int(sys.argv[3]), False, can_transactions_arrive_any_time, fixed_iteration)
    # with open('./out/outputState.py', 'w') as file:
    #     file.write(visitor.visit(tree))
    # except Exception as e:
    #     print(str(e))


def parseFile(file):
    with open(file, 'r') as content_file:
        pattern = content_file.read()

    # If constructor missing, inject it
    if 'constructor' not in pattern:
        if 'contract' in pattern and '{' in pattern and '}' in pattern:
            if 'function' in pattern:
                pattern = (
                    pattern[:pattern.index('function')] +
                    '\nconstructor(){\n\trequire(msg.sender != this)\n}\n' +
                    pattern[pattern.index('function'):]
                )
            else:
                pattern = (
                    pattern[:pattern.index('}')] +
                    '\nconstructor(){\n\trequire(msg.sender != this)\n}\n' +
                    pattern[pattern.index('}'):]
                )
    else:
        # Ensure constructor starts with require(msg.sender != this);
        pattern = re.sub(
            r'(constructor\s*\([^)]*\)\s*\{)',
            r'\1\n\trequire(msg.sender != this);',
            pattern
        )

    # Existing replacements
    pattern = re.sub(r'\.transfer\((.*?)\)', r'!\1', pattern)
    pattern = pattern.replace('<tx> ', '<tx>').replace('<tx>', 'app_tx_st.')
    pattern = re.sub(
        r'(contract\s+\w+\s*\{)',
        lambda match: match.group(1) + ' bool lastReverted;\nint block_num;\n',
        pattern
    )
    pattern = re.sub(
        r'(\bfunction\s+\w+\s*\([^)]*\)\s*)(?!payable\b)\{',
        r'\1{ require(msg.value == 0); ',
        pattern
    )
    pattern = re.sub(
        r'(\bfunction\s+\w+\s*\([^)]*\)(?:\s*payable)?\s*)\{',
        r'\1{ require(msg.sender != this); require(msg.sender != a0);',
        pattern
    )

    parse(pattern)


def main(args):
    parseFile(args[1])

if __name__ == '__main__':
	main(sys.argv)
