# -*- coding:utf-8 -*-
from app.config import *
from app.taobao import TBApi
from app.utils.aes import AESUtil
from app.appserver import AppServer


app_server = AppServer()
app = app_server.server_app


@app.route('/')
def index():
    today_rec = TBApi.get_goods_list(ROOT, 1, 5)
    txs = TBApi.get_goods_list(ROOT, 1, 15)
    return AppServer.render('index.html', today_rec=today_rec, txs=txs, cur_q=ROOT)


@app.route('/q/<q_type>')
def menu_html(q_type):
    q_type = int(AESUtil.decrypt(q_type))
    today_rec = TBApi.get_goods_list(q_type, 1, 5)
    txs = TBApi.get_goods_list(q_type, 1, 15)
    return AppServer.render('index.html', today_rec=today_rec, txs=txs, cur_q=q_type)


@app.route('/q-t/<q_type_item>')
def menu_nav_html(q_type_item):
    q_type_item = AESUtil.decrypt(q_type_item)
    cur_q = int(q_type_item.split('-')[0])
    cur_q_i = int(q_type_item.split('-')[1])
    today_rec = TBApi.get_goods_list(cur_q_i, 1, 5)
    txs = TBApi.get_goods_list(cur_q_i, 1, 15)
    return AppServer.render('index.html', today_rec=today_rec, txs=txs, cur_q=cur_q, cur_q_i=cur_q_i)


if __name__ == '__main__':
    app_server.run(host='0.0.0.0', port=5566, debug=True)


