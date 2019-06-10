from antlr4 import ParseTreeWalker

from compiler.listener.FunctionDefinitionListener import FunctionDefinitionListener
from generated.CodeParser import CodeParser
from llvmlite import ir


def walk(module: ir.Module, ctx: CodeParser.FunctionDefinitionContext) -> FunctionDefinitionListener:
    listener = FunctionDefinitionListener(module)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
