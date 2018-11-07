# -*- coding: UTF-8 -*-
"""
Created on 2018年11月5日
@author: Leo
存储一些全局变量
"""
# 请求URL
URL = "http://srh.bankofchina.com/search/whpj/search.jsp"

# 插入语句
INSERT_SQL = """
    INSERT INTO `exchange_rate`.`t_temp_1` (
    `currency_name`, `buying_rate`, `cash_buying_rate`,
    `selling_rate`, `cash_selling_rate`, `boe_conversion_rate`, 
    `rate_time`) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""