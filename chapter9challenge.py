
#1
st = open("st.txt","w")
st.write("Hi from python")
st.close

with open ("st.txt","r") as f:
    print(f.read())

#2
with open("toi2.txt","w+",encoding = "utf-8") as toi2:
    ans = input("あなたの名前は何ですか？(what is your name?)")
    toi2.write(ans)

toi2 = open("toi2.txt","w+",encoding = "utf-8")
print(toi2.read())
toi2.close
#toi2.closeをした後toi2.txtの中身が消えている。と思ったが、w+でもう一度読み込むと消えている。

#3
#csvファイルに書き込む
toi3 = [["Top Gun","Risky Business","Minority","Report"],["Titanic","The Revienant","Inception"]]
import csv
with open("toi3.csv","w") as f:
          w = csv.writer(f,delimiter=",")
        　"""
          wには<_csv.writer object at 0x0000011E2FDF3DC0>というオブジェクトが返される。
          要するに書く準備が整ったみたいなこと
          csvモジュールのwriterメソッドはファイルオブジェクトとデリミタを受け取って、csv
          オブジェクトを返す。そしてcsvオブジェクトにはwriterowメソッドがあり引数として
          リストを受け取って、その内容をcsvファイルに書き出す。writerowは一回の呼び出しで一行を書く。
          """
          for row in toi3:
              w.writerow(row)

#csvファイルに書き込んだものをpython上に書き出す。
with open("toi3.csv","r") as fr:
    r = csv.reader(fr, delimiter=",")#csvオブジェクトに変換して読み込んでいる。
    #rは<_csv.reader object at 0x0000011E2FE2C400>　機械語みたいなもの？
    for row in r:
        print(",".join(row))#csvオブジェクトをループごとに取り出されてたrowの要素をカンマで
        #結合して出力している。ｒは行ごとに出力される。

for row in r:
    row.append(row)
    
row
[[...]]
・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・・
for row in r:
        print(row)

          
['Top Gun', 'Risky Business', 'Minority', 'Report']
[]#リストとリストの間のコンマ？で区切っているから空白のリスト？
['Titanic', 'The Revienant', 'Inception']
[]

#4
encoding = "utf-8"にすればいい
