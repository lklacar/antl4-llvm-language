from antlr4 import ParseTreeWalker

from compiler.listener.StatementListener import StatementListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.StatementContext, builder) -> StatementListener:
    listener = StatementListener(builder)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
