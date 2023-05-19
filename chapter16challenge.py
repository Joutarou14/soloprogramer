#Bash
1,
echo Self-taught

2,
絶対パス
パスの名前をうちこめばいい
相対パス
cd /

3,
---windowsver
setでpathの確認できる
set $python_projects="絶対パス" で環境変数の設定
st=open(".profile","w")
st.write("$python_project")
st.close
これをするともともと書いてあったものがすべて消えてしまうかもしれない。直接書いた方が良いかも

---macver
setの代わりにexportを使う
