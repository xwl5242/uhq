from top.api.base import RestApi


class TbkDgMaterialOptionalRequest(RestApi):
    def __init__(self, keyword, adzone_id, page_no=1, page_size=20):
        super(TbkDgMaterialOptionalRequest, self).__init__()
        self.q = keyword
        self.page_no = page_no
        self.page_size = page_size
        self.adzone_id = adzone_id

    def getapiname(self):
        return "taobao.tbk.dg.material.optional"


