# -*- coding:utf-8 -*-
import os
import configparser

cp = configparser.ConfigParser()
cp.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini'))

TB_ADZONE_ID = str(cp.get('TAO_BAO', 'ad_zone_id'))


if __name__ == '__main__':
    print(TB_ADZONE_ID)
