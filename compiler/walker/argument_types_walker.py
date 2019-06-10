from antlr4 import ParseTreeWalker

from compiler.listener.ArgumentTypesListener import ArgumentTypesListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ArgumentsContext) -> ArgumentTypesListener:
    listener = ArgumentTypesListener()
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
