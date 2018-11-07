# -*- coding: utf-8 -*- #
"""
Created on 2018年11月7日
@author: Leo
"""
# Python内置库
import os
import sys
import getopt
from typing import List, Tuple

# Python第三方库
# 通过调用命令行进行调试
# 调用execute这个函数可调用scrapy脚本
from scrapy.cmdline import execute

# 项目内部库
from BOC_FER_Spider.utils.currency_mapper import CURRENCY_MAP
from BOC_FER_Spider.utils.common_utils import time_format_validate


def usage():
    """
    使用说明
    """
    print("中国银行外汇牌价爬虫命令使用帮助(2018-11-07):\n")
    print("使用方法: python cmdline_start_spider.py [option]")
    print("示例: python cmdline_start_spider.py -s 2018-11-07 -e 2018-11-07 -c 港币")
    print("Option列表如下:")
    print("-s 起始时间(格式YYYY-MM-DD)")
    print("-e 结束时间(格式YYYY-MM-DD)")
    print("-c 货币类型(参考currency_mapper中的对应名称或自行参考中国银行外汇牌价网站)")
    print("-h 使用说明")


def parse_args(option_list: List[Tuple[str, str]]):
    """
    解析参数列表
    :param option_list: 参数列表
    """
    start_time = ""
    end_time = ""
    currency_name = ""
    for op, value in option_list:
        if op == "-s":
            start_time = value
        elif op == "-e":
            end_time = value
        elif op == "-c":
            currency_name = value
        elif op == "-h":
            usage()
            sys.exit()
    # 传递参数
    start_spider(start_time=start_time, end_time=end_time, currency_name=currency_name)


def start_spider(start_time: str, end_time: str, currency_name: str):
    """
    用scrapy.cmdline命令启动Scrapy
    :param start_time: 起始时间
    :param end_time: 结束时间
    :param currency_name: 货币类型
    """
    assert time_format_validate(time_str=start_time) is not True, "起始日期格式出错!请检查日期格式!"
    assert time_format_validate(time_str=end_time) is not True, "起始日期格式出错!请检查日期格式!"
    assert currency_name in list(CURRENCY_MAP.keys()) is not True, "货币名称有误!"

    # 设置工程路径，在cmd 命令更改路径而执行scrapy命令调试
    # 获取main文件的父目录，os.path.abspath(__file__) 为__file__文件目录
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    # 运行
    execute(["scrapy", "crawl", "BOC",
             "-a", "start_time={}".format(start_time),
             "-a", "end_time={}".format(end_time),
             "-a", "currency_name={}".format(currency_name)])


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hs:e:c:")
    parse_args(option_list=opts)
