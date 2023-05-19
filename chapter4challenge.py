#1
def num():
    """
    Returns 2乗
    """
    number = input("数字を入力してください")
    int_number = int(number)
    number_1 = int_number**2
    print(number_1)

#2
def w():
    x = input("type words")
    return x


#3
def f(a,b,c,d=1,e=1):
    """
    Returns a+b+c+d+e
    :param a: int.
    :param b: int.
    :return: int sum of a and b.
    """
    return a+b+c+d+e

f(1,2,3,4,5)


#4
def one(x):
    one = x/2
    return one

def two(y):
    two = y*4
    return two

def three():
    x = input("type number")
    x = int(x)
    y = one(x)
    z = two(y)
    return z

#5
def flo():
    words = input("type!")
    try:
        words = float(words)
        return words
    except ValueError:
        print("type number!!")


