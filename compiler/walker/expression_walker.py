from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.listener.ExpressionListener import ExpressionListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ExpressionContext, builder, t: ir.Type) -> ExpressionListener:
    listener = ExpressionListener(builder, t)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
