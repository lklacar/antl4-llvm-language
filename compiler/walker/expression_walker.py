from antlr4 import ParseTreeWalker

from compiler.listener.ExpressionListener import ExpressionListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ExpressionContext, builder) -> ExpressionListener:
    listener = ExpressionListener(builder)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
