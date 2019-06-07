import sys
from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser
import llvmlite.binding as llvm

from listener.ProgramVisitor import ProgramVisitor


def generate_object_file(module):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    target = llvm.Target.from_default_triple()

    # Turn off optimization for testing purposes
    target_machine = target.create_target_machine(opt=0)
    module_ref = llvm.parse_assembly(str(module))
    obj = target_machine.emit_object(module_ref)

    with open("out/evaluate.o", "wb") as f:
        f.write(obj)


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CodeParser(tokens)

    program_visitor = ProgramVisitor()
    parser.program().accept(program_visitor)


    #generate_object_file(module)

    #print("LLVM IR Code: ")
    #print(module)


if __name__ == '__main__':
    main(sys.argv)
