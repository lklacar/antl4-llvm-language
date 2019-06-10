from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.listener.FunctionBodyListener import FunctionBodyListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.FunctionBodyContext, builder: ir.IRBuilder) -> FunctionBodyListener:
    listener = FunctionBodyListener(builder)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
