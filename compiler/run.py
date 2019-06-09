import sys

import llvmlite.binding as llvm
from antlr4 import *

from compiler.listener.ProgramListener import ProgramListener
from generated.CodeLexer import CodeLexer
from generated.CodeParser import CodeParser


def optimize(module_ref):
    pass_manager_builder = llvm.create_pass_manager_builder()

    module_pass_manager = llvm.create_module_pass_manager()

    # Optimize the fuck out of this
    module_pass_manager.add_constant_merge_pass()
    module_pass_manager.add_dead_arg_elimination_pass()
    module_pass_manager.add_function_attrs_pass()
    module_pass_manager.add_function_inlining_pass(5)
    module_pass_manager.add_global_dce_pass()
    module_pass_manager.add_global_optimizer_pass()
    module_pass_manager.add_ipsccp_pass()
    module_pass_manager.add_dead_code_elimination_pass()
    module_pass_manager.add_cfg_simplification_pass()
    module_pass_manager.add_gvn_pass()
    module_pass_manager.add_instruction_combining_pass()
    module_pass_manager.add_licm_pass()
    module_pass_manager.add_sccp_pass()
    module_pass_manager.add_sroa_pass()
    module_pass_manager.add_type_based_alias_analysis_pass()
    module_pass_manager.add_basic_alias_analysis_pass()

    pass_manager_builder.populate(module_pass_manager)

    module_pass_manager.run(module_ref)


def generate_object_file(module):
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    target = llvm.Target.from_default_triple()

    target_machine = target.create_target_machine(opt=3)
    module_ref = llvm.parse_assembly(str(module))

    optimize(module_ref)

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
