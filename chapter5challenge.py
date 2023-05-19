#1
musician = list("superbeaver")
musician
['s', 'u', 'p', 'e', 'r', 'b', 'e', 'a', 'v', 'e', 'r']
# リスト（）のときはひとつの要素しかいれることができない

# リスト型(要素が決まっている)
リストオブジェクト = [要素1,要素2,要素3]

# リスト型(要素をあとから追加) 
リストオブジェクト = list()　もしくは　変数 = []
リストオブジェクト.append(要素1)
リストオブジェクト.append(要素2) 
リストオブジェクト.append(要素3)

musician = ["superbeaver","supittu"]

#2
location = tuple("1212")
l = [0, 1, 2]

lt = tuple(l)
print(lt)
print(type(lt))

location
('1', '2', '1', '2')
location = (12,12)

#3
information = dict("he")
d = dict(k1=1, k2=2, k3=3)
print(d)
# {'k1': 1, 'k2': 2, 'k3': 3}
information = {"height":166,"like_color":"blue"}

#4
def scan() :
    key = input("Please enter the information you want to know : ")
    return information[key]

#5
like_musician = {"superbeaver":["a","b","c"]}

#6
set型のオブジェクトは波括弧{}で要素を囲むと生成できる。

重複する値がある場合は無視されて、一意な値のみが要素として残る。
異なる型を要素として持つこともできる。ただし、リスト型のような更新可能なオブジェクトは登録できない。タプルはOK。

また、set型は順序をもたないので、生成時の順序は記憶されない
set型のオブジェクトはコンストラクタset()でも生成できる。

引数としてリストやタプルのようなイテラブルオブジェクトを指定すると、重複する要素が除外されて一意な値のみが要素となるsetオブジェクトが生成される。

l = [1, 2, 2, 3, 1, 4]

print(l)
print(type(l))
# [1, 2, 2, 3, 1, 4]
# <class 'list'>

s_l = set(l)

print(s_l)
print(type(s_l))
# {1, 2, 3, 4}
# <class 'set'>
