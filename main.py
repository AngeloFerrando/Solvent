from Z3Visitor import *
from TypeVisitor import *

from antlr4.error.ErrorListener import ErrorListener
import sys
import os

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
    visitor = Z3Visitor(int(sys.argv[2]), int(sys.argv[3]), True, can_transactions_arrive_any_time, fixed_iteration)

    isExist = os.path.exists('./out')
    if not isExist:
        os.makedirs('./out')
    try:
        type_visitor.visit(tree)
    except Exception as e:
        print(e)
        return
    try:
        with open('./out/outputTrace.py', 'w') as file:
            file.write(visitor.visit(tree))
        visitor = Z3Visitor(int(sys.argv[2]), int(sys.argv[3]), False, can_transactions_arrive_any_time, fixed_iteration)
        with open('./out/outputState.py', 'w') as file:
            file.write(visitor.visit(tree))
    except Exception as e:
        print(str(e))


def parseFile(file):
    with open(file, 'r') as content_file:
        pattern = content_file.read()
    if 'constructor' not in pattern:
        if 'contract' in pattern and '{' in pattern and '}' in pattern:
            if 'function' in pattern:
                pattern = pattern[:pattern.index('function')] + '\nconstructor(){\n\tskip\n}\n' + pattern[pattern.index('function'):]
            else:
                pattern = pattern[:pattern.index('}')] + '\nconstructor(){\n\tskip\n}\n' + pattern[pattern.index('}'):]
    parse(pattern)

def main(args):
    parseFile(args[1])

if __name__ == '__main__':
	main(sys.argv)
