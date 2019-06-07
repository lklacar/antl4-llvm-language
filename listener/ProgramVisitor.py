from generated.CodeParser import CodeParser
from generated.CodeVisitor import CodeVisitor
from generator import CodeGenerator
import llvmlite.binding as llvm

class ProgramVisitor(CodeVisitor):
    def __init__(self):
        self.generator = CodeGenerator("program")

    def visitProgram(self, ctx: CodeParser.ProgramContext):
        module = self.generator.generate_program(ctx)
        print(module)

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