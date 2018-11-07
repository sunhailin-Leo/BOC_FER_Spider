# -*- coding: UTF-8 -*-
"""
Created on 2018年11月7日
@author: Leo
"""
import re


def time_format_validate(time_str: str, default_pattern=r"(\d{4}-\d{2}-\d{2})") -> bool:
    """
    日期格式校验(默认格式: YYYY-MM-DD)
    可以扩展成任何形式只需要改变正则即可
    :param time_str: 日期字符串
    :param default_pattern: 默认的正则表达式(校验YYYY-MM-DD)
    :return: bool (True则日期格式出错,False则日期格式正常)
    """
    time_str_reg = re.search(default_pattern, time_str)
    return [False, True][time_str_reg is None]
