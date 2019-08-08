# -*- coding:utf-8 -*-
from app.taobao import TBApi
from flask import Flask, render_template


app = Flask('uhq_by_xwl')


@app.route('/')
def index():
    return render_template('index.html', today_rec=TBApi.get_goods_list(1, 5),
                           txs=TBApi.get_goods_list(1, 10))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5566, debug=True)


