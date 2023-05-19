#1
class Square:
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self.s1)

#2
class Square:
    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):

        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

#3
def juge(a,b):
    ans1 = a is b
    return ans1
