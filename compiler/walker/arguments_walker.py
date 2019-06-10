from antlr4 import ParseTreeWalker

from compiler.listener.ArgumentsListener import ArgumentsListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ArgumentsContext) -> ArgumentsListener:
    listener = ArgumentsListener()
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
