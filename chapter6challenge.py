
#1
a = "カミュ"
a[0]
a[1]
a[2]

#2
what = input("何を:")
who = input("誰に:")
r = "私は昨日{}を書いて、{}に送った！".format(what, who)
print(r)

#3
"ldous Huxley was born in 1984".capitalize()

#4
"どこで？　だれが？　いつ？".split("　")
#原因は、文字列リテラル以外の箇所に全角スペースがあることです。そのため構文エラーになります。
"どこで？　だれが？　いつ？".split("？")
['どこで', '\u3000だれが', '\u3000いつ', '']

#5
words = ["the", "fox", "jumped", "over", "thd", "fence", "."]
one = "".join(words)
one

#6
a = "A screaming comes across the sky.".replace("s","$")
print(a)

#7
"Hemingway".index("m")

#8
"彼は\"私たちは自由だ\"といった"

#9
"three" + " three" + " three"
"three " * 3

#10
a = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(a[:11])
