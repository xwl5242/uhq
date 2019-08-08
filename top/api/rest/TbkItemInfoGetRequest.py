from top.api.base import RestApi


class TbItemInfoGetRequest(RestApi):
    def __init__(self, item_ids):
        super(TbItemInfoGetRequest, self).__init__()
        self.num_iids = item_ids

    def getapiname(self):
        return "taobao.tbk.item.info.get"

