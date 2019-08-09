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
# 页面导航，二级菜单
NAV = [n for n in str(cp.get('MENU_NAV', 'nav')).split(',')]
# 各导航对应的物料id集合
MATERIAL_MAP = dict()
__options = cp.options('MATERIAL')
for option in __options:
    MATERIAL_MAP[str(option).replace('material_', '')] = [material for material in str(cp.get('MATERIAL', option)).split(',')]

if __name__ == '__main__':
    print(MATERIAL_MAP)
