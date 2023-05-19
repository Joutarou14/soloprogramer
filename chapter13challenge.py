#1
class Rectangle:
    def __init__(self, long, short):
        self.long = long
        self.short = short

    def calculate_perimeter(self):
        return self.long * 2 + self.short*2

class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

#2
class Square(Square):
    def change_size(self,plus):
        self.plus = plus
        self.side = self.side + self.plus


#3
class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    pass

#4
class Rider:
    def __init__(self,rider):
        self.rider = rider

class Horse:
    def __init__(self,horse,rider):
        self.horse = horse
        self.rider = rider

R = Rider("jou")
H = Horse("jonasann",R)
