#1
#4つの属性　色、重さ、味、種類
class Apple:
    def __init__(self,c,w,t,k): # initの両端は長線2つ
        self.color = c
        self.weight = w
        self.taste = t
        self.kind = k
ap = Apple("red",100,"sweet","redapple")

#2
import math

class Circle:
    def __init__(self,h):
        self.half = h
        print("Created")

    def area(self,h):
        self.area = h**2 * math.pi

C.area(3)


#3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.high = h
        print("Created")

    def area(self, b, h):
        self.area = b * h / 2


#4
class Hexagon:
    def __init__(self,d):
        """
        dは中心から各頂点までの距離
        """
        self.dis = d
        print("created")

    def calculate_perimeter(self,d):
        d = math.sqrt(d**2 + d**2 - (2*d**2 * math.cos(360 / 6)))
        self.perimeter = d * 6
