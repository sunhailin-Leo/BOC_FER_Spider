# -*- coding: utf-8 -*- #
"""
Created on 2018年11月7日
@author: Leo
"""
import time
from selenium import webdriver
from BOC_FER_Spider.utils.enum_variable import *


def get_total_page(start_time: str, end_time: str, currency_name: str) -> str:
    """
    获取总页数 (selenium chrome headless mode)
    :param start_time: 起始时间
    :param end_time: 结束时间
    :param currency_name: 货币名称
    :return: 总页数
    """
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(executable_path="./chrome_driver/chromedriver2-35.exe", options=option)
    browser.get(URL)
    time.sleep(2)

    # 移除起始日期input框的readonly属性
    time_list = [start_time, end_time]
    remove_name = ["erectDate", 'nothing']
    for i, name in enumerate(remove_name):
        remove_js = 'document.getElementsByName("' + name + '")[0].removeAttribute("readonly");'
        browser.execute_script(remove_js)
        browser.find_element_by_name(name).send_keys(time_list[i])

    # 设置货币类型
    time.sleep(1)
    select_currency = """
    var all_options = document.getElementById("pjname").options;
    for (i=0; i<all_options.length; i++){
          if (all_options[i].label == '""" + currency_name + """')
          {
             all_options[i].selected = true;
          }
       }
    """
    browser.execute_script(select_currency)

    # 执行查询js
    time.sleep(1)
    browser.execute_script("executeSearch();")

    # 获取总页数
    time.sleep(1)
    page_context = browser.execute_script("return PageContext.params;")

    # 退出浏览器
    browser.quit()

    # 返回执行结果
    return page_context['PageCount']
