# -*- coding:utf-8 -*-
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
        # self.scheduler.add_job(id='app-job', func=MyJobs.app_index_job, trigger='interval', seconds=11 * 60)
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
    def render_page(material_id, html='index.html', **kwargs):
        page_no = request.args.get('p')
        page_no = int(page_no) if page_no else 1
        top = TBApi.get_goods_list(material_id, page_no, 15)
        txs = TBApi.get_goods_list(material_id, page_no+1, 15)
        return AppServer.render(html, page_no=page_no, banners=top, txs=txs,
                                total=MATERIAL_COUNT_MAP.get(str(material_id)), **kwargs)


