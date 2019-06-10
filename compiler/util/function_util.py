from llvmlite import ir


def create(module: ir.Module, function_name: str, return_type: ir.Type, argument_types: [ir.Type]) -> ir.IRBuilder:
    function = ir.Function(
        module,
        ir.FunctionType(return_type, argument_types),
        function_name
    )
    block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    return builder
