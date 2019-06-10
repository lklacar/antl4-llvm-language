from llvmlite import ir

from compiler.function.Function import Function


def create(module: ir.Module, function_name: str, return_type: ir.Type, parameter_types: [ir.Type]) -> ir.IRBuilder:
    function = Function(
        module,
        ir.FunctionType(return_type, parameter_types),
        function_name
    )
    block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    return builder
