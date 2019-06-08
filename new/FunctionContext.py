from new.ProgramContext import ProgramContext


class FunctionContext:
    variables = {}

    def __init__(self, name, program_context: ProgramContext, function_head, function):
        self.program_context = program_context
        self.name = name
        self.function_head = function_head
        self.function = function
        program_context.add_function(name, self)

    def add_variable(self, name, pointer):
        self.variables[name] = pointer

    def get_variable(self, name):
        return self.variables[name]
