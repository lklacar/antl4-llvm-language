import sys

from antlr4 import *

from compiler.listener.ProgramListener import ProgramListener
from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.program()

    printer = ProgramListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
