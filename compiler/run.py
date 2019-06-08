import sys

from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser
from compiler.listener.ProgramListener import ProgramListener
import llvmlite.binding as llvm


def generate_object_file(module):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()

    # Turn off optimization for testing purposes
    target_machine = target.create_target_machine(opt=0)
    module_ref = llvm.parse_assembly(str(module))
    obj = target_machine.emit_object(module_ref)

    with open("../out/evaluate.o", "wb") as f:
        f.write(obj)


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
    generate_object_file(printer.module)


if __name__ == '__main__':
    main(sys.argv)
