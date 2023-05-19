'''
#17章
import re
l = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
'''

#Mad LIbs game
import re

text = """キリンは大昔から_複数名詞_の興味の対象でした。キリンは_複数名詞_のなかで一番背が高いですが、
科学者たちはそのような長い_体の一部_をどうやって獲得したのか説明できません。キリンの身長は_数値_ _単位_
近くあり、その高さのほとんどは脚と_体の一部_によるものです。"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=ヒント)の部分はあとを2つのアンダースコアで
挟んでください。ヒントの単語にはアンダースコアを含めないで下さい。___hint_hint__はだめです。__hint_はo
kです。
    
    """
    
    hints = re.findall("_.*?_",mls)
    if hints is not None:
       for word in hints:
           q = "{} を入力:".format(word)
           new = input(q)
           mls = mls.replace(word, new, 1)
           print('\n')
           mls = mls.replace("\n", "")
           print(mls)
    else:
        print("引数mlsが無効です。")

mad_libs(text)

              
#challenge
1,
grep -o Dutch zen.txt

2,
l = "Arizona 479, 501 ,870. California209, 231, 650."
grep [[:digit:]] l じゃならない

echo Arizona 479, 501 ,870. California209, 231, 650. | grep [[:digit:]]

3,
import re
l = "The ghost that says boo haunts the loo"
re.findall(".oo",l,re.MULTILINE)
































