# -*- coding:utf-8 -*-
import re
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

    def run(self, host='127.0.0.1', port=9999, **kwargs):
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
        return render_template(html, menus=MENU, navs=NAV, material_map=MATERIAL_MAP, **kwargs)

    @staticmethod
    def render_page(ma_id=None, s_kw=None, html='index.html', **kwargs):
        user_agent = request.headers.get('User-Agent')
        webs = re.findall(r'iPhone|iPad|iPod|iOS|Android', user_agent)
        html = 'index_m.html' if len(webs) > 0 else html
        page_no = request.args.get('p')
        page_no = int(page_no) if page_no else 1
        top, txs = [], []
        total = 100 if s_kw else MATERIAL_COUNT_MAP.get(str(ma_id))
        if ma_id:
            pass
            # top = TBApi.get_goods_list(ma_id, page_no, 15)
            # txs = TBApi.get_goods_list(ma_id, page_no+1, 15)
        if s_kw:
            top = TBApi.search_item(s_kw, page_no, 15)
            txs = TBApi.search_item(s_kw, page_no+1, 15)
        return AppServer.render(html, page_no=page_no, banners=top, txs=txs, total=total, **kwargs)


