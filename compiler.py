import sys
from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser
from listener.FileListener import FileListener


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.file()

    listener = FileListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(tree)

if __name__ == '__main__':
    main(sys.argv)