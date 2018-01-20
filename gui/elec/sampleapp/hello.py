#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask, render_template #追加

app = Flask(__name__)

@app.route("/")
def hello():
    name = "Hoge"
    #return name
    return render_template('first.html',template_folder='templates', title='flask test', name=name) #変更


if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)
