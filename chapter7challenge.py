"""
#1
list = ["ウォーキング・デッド","アントラ―ジュ","ザ・ソプライノズ","ヴァンパイア・ダイアリーズ"]
for i in list:
    print(i)
#2
for i in range(25,51):
    print(i)

#3
for i in range(4):
    print(i)
    list[i]
"""
"""
#4
num = input("plese type number!(qが入力されるとこのプログラムは終了します。):")
lis = ["1","2","3"]
while num != "q":
    if num == lis:
        print("正解")
    elif num != lis:
        print("不正解")
    else :
        print("数字を入力するか、qで終了します。")
    num = input("plese type number!(qが入力されるとこのプログラムは終了します。):")
"""
"""
#5
lis1 = [8,19,148,4]
lis2 = [9,1,33,83]
new_list = []

for i in range(0,4):
    a = lis1[i]
    for j in range(0,4):
        new_list.append(a*lis2[j])

print(new_list)
"""
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows):
    print(index)
    print(show)
