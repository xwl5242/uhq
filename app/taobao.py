# -*- coding:utf-8 -*-
from app.config import *
from top.api.rest import *


class TBApi:

    @staticmethod
    def get_goods_list(material_id, page_no=1, page_size=20):
        """
        获取指定物料类型的精选商品信息
        :param material_id: 物料id
        :param page_no: 页码
        :param page_size: 条数
        :return:
        """
        goods = []
        try:
            # 请求taobao api
            req = TbkDgOptimusMaterialRequest(TB_ADZONE_ID, page_no, page_size)
            req.material_id = material_id
            resp = req.getResponse()
            # 获取并解析查询结果
            g_list = resp.get('tbk_dg_optimus_material_response')\
                .get('result_list').get('map_data')
            # 由于结果中的一口价为None，所以需要再次调用获取物料详情接口
            item_ids = ','.join([str(g.get('item_id')) for g in g_list])
            # 获取物料详情
            items = TBApi.get_item_info(item_ids)
            for g in g_list:
                good = dict()
                item_id = g.get('item_id')  # 商品id
                good['item_id'] = item_id
                good['zk_final_price'] = g.get('zk_final_price')  # 折扣价
                good['reserve_price'] = items.get(item_id).get('reserve_price')  # 一口价
                good['small_images'] = items.get(item_id).get('small_images')  # 商品小图片
                good['coupon_amount'] = g.get('coupon_amount')  # 优惠券额度
                good['coupon_start_fee'] = g.get('coupon_start_fee')  # 优惠券开始满多少才能使用
                good['coupon_total_count'] = g.get('coupon_total_count')  # 优惠券总量
                good['coupon_start_time'] = g.get('coupon_start_time')  # 优惠券的开始时间
                good['title'] = g.get('title')  # 商品名称
                good['volume'] = g.get('volume')  # 月销量
                good['coupon_end_time'] = g.get('coupon_end_time')  # 优惠券的结束时间
                good['coupon_click_url'] = g.get('coupon_click_url')  # 优惠券点击链接
                good['pict_url'] = g.get('pict_url')  # 商品图片
                good['click_url'] = g.get('click_url')  # 淘宝客分享推广链接
                good['short_title'] = g.get('short_title')  # 短名称
                good['coupon_share_url'] = g.get('coupon_share_url')  # 优惠券分享链接
                goods.append(good)
            return goods
        except Exception as e:
            print(e)

    @staticmethod
    def get_item_info(item_ids):
        """
        根据商品id获取商品详情信息
        :param item_ids: 商品id，多个以","分隔
        :return:
        """
        item_map = dict()
        try:
            # 调用api
            req = TbItemInfoGetRequest(item_ids)
            resp = req.getResponse()
            # 查询结果
            items = resp.get('tbk_item_info_get_response').get('results').get('n_tbk_item')
            # 将查询结果转为dict，方便使用
            for item in items:
                item_map[item.get('num_iid')] = item
            return item_map
        except Exception as e:
            print(e)

    @staticmethod
    def search_item(keyword, page_no=1, page_size=20):
        """
        搜索物料信息
        :param keyword: 搜索的关键字
        :param page_no: 页码
        :param page_size: 条数
        :return:
        """
        try:
            # 调用api
            req = TbkDgMaterialOptionalRequest(keyword, TB_ADZONE_ID, page_no=page_no, page_size=page_size)
            resp = req.getResponse()
            # 返回结果
            items = resp.get('tbk_dg_material_optional_responseg').get('result_list').get('map_data')
            return items
        except Exception as e:
            print(e)


if __name__ == '__main__':
    TBApi.search_item('女装')

