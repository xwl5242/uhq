# -*- coding:utf-8 -*-
from flask import Flask, render_template


app = Flask('uhq_by_xwl')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5566, debug=True)


