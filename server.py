# -*- coding:utf-8 -*-
from app.config import *
from app.utils.aes import AESUtil
from app.appserver import AppServer
from flask import send_from_directory


app_server = AppServer()
app = app_server.server_app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/root.txt')
def root_txt():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                               'root.txt')


@app.route('/')
def index():
    return AppServer.render_page(ROOT, cur_q=ROOT)


@app.route('/q/<q_type>')
def menu_html(q_type):
    """
    根据大类别查询商品（网站页面菜单）
    :param q_type:
    :return:
    """
    q_type = int(AESUtil.decrypt(q_type))
    return AppServer.render_page(q_type, cur_q=q_type)


@app.route('/q-t/<q_type_item>')
def menu_nav_html(q_type_item):
    """
    根据大类别和小类别综合查询商品（网站页面菜单和导航结合）
    :param q_type_item:
    :return:
    """
    q_type_item = AESUtil.decrypt(q_type_item)
    cur_q = int(q_type_item.split('-')[0])
    cur_q_i = int(q_type_item.split('-')[1])
    return AppServer.render_page(cur_q_i, cur_q=cur_q, cur_q_i=cur_q_i)


@app.route('/q-k/<q_name>')
def search_item(q_name):
    """
    关键字搜索
    :param q_name:
    :return:
    """
    return AppServer.render_page(s_kw=q_name, cur_q=ROOT)


if __name__ == '__main__':
    app_server.run(host='0.0.0.0', port=5566, debug=True)


