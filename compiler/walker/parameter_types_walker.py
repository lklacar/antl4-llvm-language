from antlr4 import ParseTreeWalker

from compiler.listener.ParameterTypesListener import ParameterTypesListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ParametersContext) -> ParameterTypesListener:
    listener = ParameterTypesListener()
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
