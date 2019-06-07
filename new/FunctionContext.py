class FunctionContext:
    variables = {}

    def add_variable(self, name, pointer):
        self.variables[name] = pointer

    def get_variable(self, name):
        return self.variables[name]
