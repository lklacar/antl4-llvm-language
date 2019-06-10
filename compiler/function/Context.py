class Context:
    variables = {}

    def add_variable(self, name, variable):
        self.variables[name] = variable

    def get_variable(self, name):
        return self.variables[name]
