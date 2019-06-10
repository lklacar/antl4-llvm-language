from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.listener.ArgumentsListener import ArgumentsListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ArgumentsContext, argument_names: [str], builder: ir.IRBuilder) -> ArgumentsListener:
    listener = ArgumentsListener(argument_names, builder)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
