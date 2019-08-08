# -*- coding:utf-8 -*-
from app.config import *
from top.api.rest import *


class TBApi:

    @staticmethod
    def get_goods_list(page_no=1, page_size=20):
        goods = []
        try:
            req = TbkDgOptimusMaterialRequest(TB_ADZONE_ID, page_no, page_size)
            req.material_id = 9660
            resp = req.getResponse()
            g_list = resp.get('tbk_dg_optimus_material_response')\
                .get('result_list').get('map_data')
            item_ids = ','.join([str(g.get('item_id')) for g in g_list])
            items = TBApi.get_item_info(item_ids)
            for g in g_list:
                good = dict()
                item_id = g.get('item_id')
                good['item_id'] = item_id
                good['zk_final_price'] = g.get('zk_final_price')
                good['reserve_price'] = items.get(item_id).get('reserve_price')
                good['small_images'] = items.get(item_id).get('small_images')
                good['coupon_amount'] = g.get('coupon_amount')
                good['coupon_start_fee'] = g.get('coupon_start_fee')
                good['coupon_total_count'] = g.get('coupon_total_count')
                good['coupon_start_time'] = g.get('coupon_start_time')
                good['title'] = g.get('title')
                good['volume'] = g.get('volume')
                good['coupon_end_time'] = g.get('coupon_end_time')
                good['coupon_click_url'] = g.get('coupon_click_url')
                good['pict_url'] = g.get('pict_url')
                good['click_url'] = g.get('click_url')
                good['short_title'] = g.get('short_title')
                good['coupon_share_url'] = g.get('coupon_share_url')
                goods.append(good)
            return goods
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)

    @staticmethod
    def get_item_info(item_ids):
        item_map = dict()
        try:
            req = TbItemInfoGetRequest(item_ids)
            resp = req.getResponse()
            items = resp.get('tbk_item_info_get_response').get('results').get('n_tbk_item')
            for item in items:
                item_map[item.get('num_iid')] = item
            return item_map
        except Exception as e:
            print(e)

    @staticmethod
    def search_item(keyword, page_no=1, page_size=20):
        try:
            req = TbkDgMaterialOptionalRequest(keyword, TB_ADZONE_ID, page_no=page_no, page_size=page_size)
            resp = req.getResponse()
            items = resp.get('tbk_dg_material_optional_responseg').get('result_list').get('map_data')
            return items
        except Exception as e:
            print(e)


if __name__ == '__main__':
    TBApi.search_item('女装')

