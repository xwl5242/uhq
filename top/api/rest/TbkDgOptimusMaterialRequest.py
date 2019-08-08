from top.api.base import RestApi


class TbkDgOptimusMaterialRequest(RestApi):
    def __init__(self, adzone_id, page_no=1, page_size=20):
        super(TbkDgOptimusMaterialRequest, self).__init__()
        self.page_no = page_no
        self.page_size = page_size
        self.adzone_id = adzone_id

    def getapiname(self):
        return "taobao.tbk.dg.optimus.material"


