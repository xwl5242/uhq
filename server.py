# -*- coding:utf-8 -*-
from app.config import *
from app.taobao import TBApi
from app.utils.aes import AESUtil
from app.appserver import AppServer
from flask import render_template


app_server = AppServer()
app = app_server.server_app


@app.route('/')
def index():
    return render_template('index.html', today_rec=TBApi.get_goods_list(9660, 1, 5),
                           txs=TBApi.get_goods_list(9660, 1, 10), menus=MENU, navs=NAV, cur_q=3756, material_map=MATERIAL_MAP)


@app.route('/q/<q_type>')
def q_type(q_type):
    q_type = AESUtil.decrypt(q_type)
    print(q_type)
    pass


@app.route('/q-t/<q_type_item>')
def q_type_item(q_type_item):
    q_type_item = AESUtil.decrypt(q_type_item)
    print(q_type_item)
    pass


if __name__ == '__main__':
    app_server.run(host='0.0.0.0', port=5566, debug=True)


