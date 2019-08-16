# -*- coding:utf-8 -*-
import os
import configparser

cp = configparser.ConfigParser()
cp.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'), encoding='utf-8')
# AES_KEY AES加密key
AES_KEY = cp.get('AES_KEY', 'aes_key')
# 推广位id
TB_ADZONE_ID = str(cp.get('TAO_BAO', 'ad_zone_id'))
# 页面菜单
MENU = [m for m in str(cp.get('MENU', 'menu')).split(',')]
ROOT = int(MENU[0].split(':')[1])
# 页面导航，二级菜单
NAV = [n.split(':')[0] for n in str(cp.get('MENU_NAV', 'nav')).split(',')]
NAV_IMG = [f"images/icon{n.split(':')[1]}.png" for n in str(cp.get('MENU_NAV', 'nav')).split(',')]
# 各导航对应的物料id集合
MATERIAL_MAP, MATERIAL_COUNT_MAP = dict(), dict()
__options = cp.options('MATERIAL')
for option in __options:
    __key = str(option).replace('material_', '')
    __count = str(cp.get('MATERIAL', option)).split(':')[1]
    __ma_list_str = str(cp.get('MATERIAL', option)).split(':')[0]
    __value = [material for material in __ma_list_str.split(',')]
    MATERIAL_MAP[__key] = __value
    MATERIAL_COUNT_MAP[__key] = __count
    for v in __value:
        MATERIAL_COUNT_MAP[v] = __count

DATA_SOURCE = str(cp.get('DATA_SOURCE', 'local'))


if __name__ == '__main__':
    print(MATERIAL_MAP)
    print(MATERIAL_COUNT_MAP)
