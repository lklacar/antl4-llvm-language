import sys

from antlr4 import *

from compiler.generator.CodeGenerator import CodeGenerator
from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.program()

    code_generator = CodeGenerator(
        tree
    )

if __name__ == '__main__':
    main(sys.argv)
