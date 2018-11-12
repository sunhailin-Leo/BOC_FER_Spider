# -*- coding: utf-8 -*- #
"""
Created on 2018年11月7日
@author: Leo
"""
# Python内置库
import os
import sys
import getopt
import pymysql
from typing import List, Tuple

# Python第三方库
# 通过调用命令行进行调试
# 调用execute这个函数可调用scrapy脚本
from scrapy.cmdline import execute
from scrapy.utils.project import get_project_settings

# 项目内部库
from BOC_FER_Spider.settings import ITEM_PIPELINES, CSV_FILE_NAME
from BOC_FER_Spider.utils.common_utils import time_format_validate
from BOC_FER_Spider.utils.enum_variable import CREATE_TABLE, CURRENCY_MAP


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
    print("-o [可选参数] 不填则为默认配置(PIPELINE -> MySQL) 可选参数有: MySQL MongoDB CSV")
    print("-i [可选参数] 存在-i参数则为增量模式(只爬取第一页), 不存在则为全量")
    print("-h 使用说明")


def init_db():
    """
    初始化MySQL数据库
    :return:
    """
    settings = get_project_settings()
    try:
        # 获取连接对象
        conn = pymysql.connect(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PWD'],
            database=settings['MYSQL_DB_NAME'],
            charset=settings['MYSQL_CHARSET']
        )
        with conn:
            # 获取游标
            cursor = conn.cursor()
            # 输出SQL语句
            using_sql = cursor.mogrify(query=CREATE_TABLE)
            print("SQL: {}".format(using_sql))
            # 执行SQL
            cursor.execute(query=CREATE_TABLE)
            conn.commit()
    except Exception:
        raise Exception("数据库初始化失败!请确认Scrapy数据库连接配置或数据库配置无误!")


def parse_args(option_list: List[Tuple[str, str]]):
    """
    解析参数列表
    :param option_list: 参数列表
    """
    start_time = ""
    end_time = ""
    currency_name = ""
    incremental = 0
    # Scrapy配置
    for op, value in option_list:
        if op == "-s":
            start_time = value
        elif op == "-e":
            end_time = value
        elif op == "-c":
            currency_name = value
        elif op == "-o":
            if value == "MongoDB":
                ITEM_PIPELINES.clear()
                ITEM_PIPELINES['BOC_FER_Spider.pipelines.BocFerSpiderMongoDBPipeline'] = 1
            elif value == "MySQL":
                ITEM_PIPELINES.clear()
                ITEM_PIPELINES['BOC_FER_Spider.pipelines.BocFerSpiderMySQLPipeline'] = 1
            elif value == "CSV":
                ITEM_PIPELINES.clear()
                ITEM_PIPELINES['BOC_FER_Spider.pipelines.BocFerSpiderCSVPipeline'] = 1
                if CSV_FILE_NAME['FILE_NAME'] == "":
                    CSV_FILE_NAME['FILE_NAME'] = "export_{}_{}_{}".format(currency_name,
                                                                          start_time.replace("-", ""),
                                                                          end_time.replace("-", ""))
            else:
                print("管道配置使用默认配置选项!")
        elif op == "-i":
            print("开启增量模式!")
            incremental = 1
        elif op == "-h":
            usage()
            sys.exit()
    # 创建数据库表
    if "MySQL" in list(ITEM_PIPELINES.keys())[0]:
        init_db()
    # 传递参数
    start_spider(start_time=start_time, end_time=end_time,
                 currency_name=currency_name, incremental=incremental)


def start_spider(start_time: str, end_time: str, currency_name: str, incremental: int):
    """
    用scrapy.cmdline命令启动Scrapy
    :param start_time: 起始时间
    :param end_time: 结束时间
    :param currency_name: 货币类型
    :param incremental: 增量爬取
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
             "-a", "currency_name={}".format(currency_name),
             "-a", "incremental={}".format(incremental)])


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hs:e:c:o:i")
    parse_args(option_list=opts)
