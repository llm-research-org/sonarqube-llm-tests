# RSPEC-4144 Functions and methods should not have identical implementations
class MyClass:
    code = "secret"

    def calculate_code(self):
        self.do_the_thing()
        return self.__class__.code

    def get_name(self):  # Noncompliant: duplicates calculate_code
        self.do_the_thing()
        return self.__class__.code

    def do_the_thing(self):
        pass  # on purpose