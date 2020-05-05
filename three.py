"""
    In this project you will use the classes available
    to create a story of events so that the print
    at the end returns True.

"""


def tell_story():
    a = Bird()
    b = Dragon()
    c = Gorilla()
    # Generate  as many other objects as you want

    beetle = Beetle()
    chipmunk = Chipmunk()
    snake = Snake()
    cobra = Cobra()
    goat = Goat()
    sheep = Sheep()
    donkey = Donkey()
    pig = Pig()

    # Have objects interact

    b.eat(chipmunk)
    b.eat(goat)
    b.eat(sheep)

    # replace the replace_me_object
    replace_me_object = b
    final_phrase = replace_me_object.talk()
    return final_phrase


class Animal:
    def __init__(self):
        self.phrase = ""

    def eat(self, other):
        self.phrase += str(other.phrase)

    def talk(self):
        return self.phrase


class Beetle(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "ztrauq kcalb"


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "Tweet"


class Dragon(Animal):
    def __init__(self):
        super().__init__()

    def eat(self, other):
        self.phrase = str(other.phrase[::-1])

    def talk(self):
        return self.phrase[0::2]


class Gorilla(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "123456789"

    def beat(self, other1, other2):
        self.phrase = str(other1.phrase) + " " + str(other2.phrase)


class Chipmunk(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "Munchd"

    def eat(self, other):
        self.phrase = str(other.phrase[0])


class Snake(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "Hiss"

    def eat(self, other):
        self.phrase = str(other.phrase).toLower()


class Cobra(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "Snorflek"

    def eat(self, other):
        self.phrase = str(other.phrase).toUpper()


class Goat(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "Brae"

    def eat(self, other):
        self.phrase = str(other.phrase) + str(",")


class Sheep(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "GypJ"


class Donkey(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "vozx"

    def eat(self, other):
        self.phrase = str(other.phrase) + str("!")


class Pig(Animal):
    def __init__(self):
        super().__init__()
        self.phrase = "eduj"


if __name__ == "__main__":
    print(tell_story() == "Sphinx of black quartz, judge my vow!")
