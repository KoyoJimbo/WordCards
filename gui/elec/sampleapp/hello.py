#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from py_modules import main
import time
from flask import Flask, render_template
from flask import request
import random

app = Flask(__name__)

ins_main = main.Main()
w_e, w_j = ins_main.main_func()
rnum = random.randint(0,len(w_e)-1)

@app.route("/")
def hello():
    message= self.w_j[self.rnum]
    #return name
    return render_template('first.html',template_folder='templates',
                           title='flask test',message=message) #変更

@app.route('/post',methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        answer = w_e[rnum]
        message= w_j[rnum]
        # first.html をレンダリングする
        return render_template('first.html',name=name,message=message,answer=answer)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('first'))


if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)
