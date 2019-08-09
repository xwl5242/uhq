# -*- coding:utf-8 -*-
from app.utils import *
from app.config import *
from flask_apscheduler import APScheduler
from flask import Flask, render_template


class AppServer:

    def __init__(self):
        self._handlers = dict()
        self.scheduler = APScheduler()
        self._server_app = Flask('yoviptv')

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

