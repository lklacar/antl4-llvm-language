import sys
from antlr4 import *

from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser
from listener.FileListener import FileListener
import llvmlite.binding as llvm


def generate_object_file(module):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    context = llvm.create_context()

    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()

    module_ref = llvm.parse_assembly(str(module))

    obj = target_machine.emit_object(module_ref)

    with open("out/evaluate.o", "wb") as f:
        f.write(obj)


def main(argv):
    input_stream = FileStream("./test/example.code")
    lexer = CodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CodeParser(stream)
    tree = parser.file()

    listener = FileListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    module = listener.get_llvm_module()

    # print(module)
    generate_object_file(module)


if __name__ == '__main__':
    main(sys.argv)
