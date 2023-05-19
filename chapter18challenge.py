#18章
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "りゅうくんとえいくんのおバカ"


app.run(host='0.0.0.0')

#app.run(host='0.0.0.0')にすると他のパソコンからも閲覧することが出来る。
#また画面消したらなくなる

"""

#pip install audiobook

from audiobook import AudioBook

ab = AudioBook("C:\Users\bb38121048\Documents\mywork\soloprogramer\zen.txt")
ab.text_to_speech()

"""
