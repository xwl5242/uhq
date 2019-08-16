# -*- coding:utf-8 -*-
import re, os, json
from app.utils import *
from app.config import *
from app.taobao import TBApi
from flask_apscheduler import APScheduler
from flask import Flask, render_template, request


class AppServer:

    def __init__(self):
        self._handlers = dict()
        self.scheduler = APScheduler()
        self._server_app = Flask('uhq')

    @property
    def server_app(self):
        """
        flask app, 并添加filters，jobs
        :return:
        """
        self._server_app.add_template_filter(math_mod, 'math_mod')
        self._server_app.add_template_filter(str_split, 'str_split')
        self._server_app.add_template_filter(get_tuple, 'get_tuple')
        self._server_app.add_template_filter(get_list, 'get_list')
        self._server_app.add_template_filter(get_sub_list, 'get_sub_list')
        self._server_app.add_template_filter(b64encode, 'b64encode')
        # self.scheduler.init_app(self._server_app)
        # self.scheduler.add_job(id='app-job', func=MyJobs.app_index_job, trigger='interval', seconds=30 * 60)
        # self.scheduler.start()
        return self._server_app

    def run(self, host='0.0.0.0', port=9999, **kwargs):
        """
        flask启动
        :param host: host，默认是127.0.0.1
        :param port: 端口，默认是9999
        :param kwargs: 其他flask app run的参数，如 debug=False
        :return:
        """
        self._server_app.run(host=host, port=port, **kwargs)

    @staticmethod
    def render(html, **kwargs):
        """
        页面渲染
        :param html: 要渲染的html
        :param kwargs: 传递的参数
        :return:
        """
        return render_template(html, menus=MENU, navs=NAV, nav_icons=NAV_IMG, material_map=MATERIAL_MAP, **kwargs)

    @staticmethod
    def render_page(ma_id=None, s_kw=None, html='index.html', **kwargs):
        """
        分页渲染
        :param ma_id: 物料id
        :param s_kw: 关键字
        :param html: 要渲染的html
        :param kwargs: 传递的参数
        :return:
        """
        # 判断当前访问的设备是移动端还是pc端
        user_agent = request.headers.get('User-Agent')
        webs = re.findall(r'iPhone|iPad|iPod|iOS|Android', user_agent)
        # 移动端访问带_m的页面
        html = 'index_m.html' if len(webs) > 0 else html
        # 分页相关参数
        page_size = 10 if len(webs) > 0 else 20
        page_no = request.args.get('p')
        page_no = int(page_no) if page_no else 1
        top, txs = [], []
        if DATA_SOURCE == '1':
            total = 15
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/goods.json')
            with open(file_path, encoding='utf-8') as f:
                good_json = json.loads(f.read())
                top, txs = good_json, good_json
        else:
            # 分页总条数
            total = 100 if s_kw else MATERIAL_COUNT_MAP.get(str(ma_id))
            if ma_id:
                # 根据物料id获取商品信息
                top = TBApi.get_goods_list(ma_id, page_no, page_size)
                txs = TBApi.get_goods_list(ma_id, page_no+1, page_size)
            if s_kw:
                # 根据关键字获取商品信息
                top = TBApi.search_item(s_kw, page_no, page_size)
                txs = TBApi.search_item(s_kw, page_no+1, page_size)
        return AppServer.render(html, page_no=page_no, banners=top, txs=txs, total=total, **kwargs)




