from Z3Visitor import *

from antlr4.error.ErrorListener import ErrorListener
import sys
import os

class LTLErrorListener( ErrorListener ):
    def __init__(self):
        super(TxScriptErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error: " + msg)

def parse(pattern):
    # try:
        lexer = LTLLexer(InputStream(pattern))
        stream = CommonTokenStream(lexer)
        parser = LTLParser(stream)
        # parser.addErrorListener(TxScriptErrorListener())
        tree = parser.ltlExpr()

        visitor = Z3Visitor()
        print(visitor.visit(tree))
    # except Exception as e:
    #     print(str(e))


def parseFile(file):
    with open(file, 'r') as content_file:
        pattern = content_file.read()
    parse(pattern)

def main(args):
    parseFile(args[1])

if __name__ == '__main__':
	main(sys.argv)
