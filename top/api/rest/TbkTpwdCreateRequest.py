from top.api.base import RestApi


class TbkTpwdCreateRequest(RestApi):
	def __init__(self):
		RestApi.__init__(self)
		self.ext = None
		self.logo = None
		self.text = None
		self.url = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.tbk.tpwd.create'
