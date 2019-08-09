# -*- coding:utf-8 -*-
from app.config import *
from app.taobao import TBApi
from app.utils.aes import AESUtil
from app.appserver import AppServer


app_server = AppServer()
app = app_server.server_app


@app.route('/')
def index():
    top = TBApi.get_goods_list(ROOT, 1, 15)
    txs = TBApi.get_goods_list(ROOT, 2, 15)
    return AppServer.render('index.html', today_rec=top[:5], banners=top[5:], txs=txs, cur_q=ROOT)


@app.route('/q/<q_type>')
def menu_html(q_type):
    q_type = int(AESUtil.decrypt(q_type))
    top = TBApi.get_goods_list(q_type, 1, 15)
    txs = TBApi.get_goods_list(q_type, 2, 15)
    return AppServer.render('index.html', today_rec=top[:5], banners=top[5:], txs=txs, cur_q=q_type)


@app.route('/q-t/<q_type_item>')
def menu_nav_html(q_type_item):
    q_type_item = AESUtil.decrypt(q_type_item)
    cur_q = int(q_type_item.split('-')[0])
    cur_q_i = int(q_type_item.split('-')[1])
    top = TBApi.get_goods_list(cur_q_i, 1, 15)
    txs = TBApi.get_goods_list(cur_q_i, 2, 15)
    return AppServer.render('index.html', today_rec=top[:5], banners=top[5:], txs=txs, cur_q=cur_q, cur_q_i=cur_q_i)


@app.route('/q-k/<q_name>')
def search_item(q_name):
    items = TBApi.search_item(q_name)
    return items


if __name__ == '__main__':
    app_server.run(host='0.0.0.0', port=5566, debug=True)


