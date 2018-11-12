# -*- coding: UTF-8 -*-
"""
Created on 2018年11月5日
@author: Leo
存储一些全局变量
"""
from BOC_FER_Spider.settings import MYSQL_DB_NAME, MYSQL_TABLE_NAME

# 请求URL
URL = "http://srh.bankofchina.com/search/whpj/search.jsp"

# 货币名称映射
CURRENCY_MAP = {
    "英镑": "1314",
    "港币": "1315",
    "美元": "1316",
    "瑞士法郎": "1317",
    "德国马克": "1318",
    "法国法郎": "1319",
    "新加坡元": "1375",
    "瑞典克朗": "1320",
    "丹麦克朗": "1321",
    "挪威克朗": "1322",
    "日元": "1323",
    "加拿大元": "1324",
    "澳大利亚元": "1325",
    "欧元": "1326",
    "澳门元": "1327",
    "菲律宾比索": "1328",
    "泰国铢": "1329",
    "新西兰元": "1330",
    "韩元": "1331",
    "卢布": "1843",
    "林吉特": "2890",
    "新台币": "2895",
    "西班牙比塞塔": "1370",
    "意大利里拉": "1371",
    "荷兰盾": "1372",
    "比利时法郎": "1373",
    "芬兰马克": "1374",
    "印尼卢比": "3030",
    "巴西里亚尔": "3253",
    "阿联酋迪拉姆": "3899",
    "印度卢比": "3900",
    "南非兰特": "3901",
    "沙特里亚尔": "4418",
    "土耳其里拉": "4560"
}


# MySQL相关语句
# 建表语句
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {}.{} (" \
               "currency_name varchar(255) NOT NULL, " \
               "buying_rate varchar(255) DEFAULT NULL, " \
               "cash_buying_rate varchar(255) DEFAULT NULL, " \
               "selling_rate varchar(255) DEFAULT NULL, " \
               "cash_selling_rate varchar(255) DEFAULT NULL, " \
               "boe_conversion_rate varchar(255) DEFAULT NULL, " \
               "rate_time varchar(255) NOT NULL," \
               "md5_str varchar(255) NOT NULL," \
               "UNIQUE KEY `unique_md5_str` (`md5_str`)" \
               ") ENGINE=InnoDB DEFAULT CHARSET=utf8;".format(MYSQL_DB_NAME, MYSQL_TABLE_NAME)

# 插入语句
INSERT_SQL = \
    "INSERT INTO {}.{} " \
    "(currency_name, buying_rate, cash_buying_rate, " \
    "selling_rate, cash_selling_rate, boe_conversion_rate, " \
    "rate_time, md5_str) " \
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(MYSQL_DB_NAME, MYSQL_TABLE_NAME)
