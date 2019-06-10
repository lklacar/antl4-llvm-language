from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.listener.ParametersListener import ParametersListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ParametersContext, parameter_names: [str], builder: ir.IRBuilder) -> ParametersListener:
    listener = ParametersListener(parameter_names, builder)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
