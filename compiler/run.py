import sys

from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser
from compiler.listener.ProgramListener import ProgramListener


def main(argv):
    input_stream = FileStream("../test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.program()

    printer = ProgramListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(printer.module)


if __name__ == '__main__':
    main(sys.argv)
