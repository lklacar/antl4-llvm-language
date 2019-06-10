from antlr4 import ParseTreeWalker
from llvmlite import ir

from compiler.listener.ArgumentsListener import ArgumentsListener
from generated.CodeParser import CodeParser


def walk(ctx: CodeParser.ArgumentsContext, builder: ir.IRBuilder, callee_function: ir.Function):
    listener = ArgumentsListener(builder, callee_function)
    walker = ParseTreeWalker()
    walker.walk(listener, ctx)

    return listener
