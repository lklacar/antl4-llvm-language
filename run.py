import sys

import llvmlite.binding as llvm
from antlr4 import *

from compiler.listener.ProgramListener import ProgramListener
from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser


def generate_object_file(module):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    target = llvm.Target.from_default_triple()

    target_machine = target.create_target_machine(opt=3)
    module_ref = llvm.parse_assembly(str(module))

    obj = target_machine.emit_object(module_ref)

    with open("./out/program.o", "wb") as f:
        f.write(obj)


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.program()

    printer = ProgramListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    generate_object_file(printer.module)

if __name__ == '__main__':
    main(sys.argv)
