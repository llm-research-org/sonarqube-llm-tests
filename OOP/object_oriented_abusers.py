class Animal:
    def __init__(self, type):
        self.type = type

    def make_sound(self):
        if self.type == "cat":
            return "meow"
        elif self.type == "dog":
            return "woof"
        else:
            raise ValueError("Invalid animal type")
