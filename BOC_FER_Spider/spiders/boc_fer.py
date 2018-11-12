# -*- coding: UTF-8 -*-
"""
Created on 2018年11月7日
@author: Leo
"""
# Python内置库
import time
import hashlib
from collections import OrderedDict

# Scrapy
import scrapy

# 项目内部库
from BOC_FER_Spider.settings import INCREMENTAL_CRAWLER_TIME
from BOC_FER_Spider.utils.get_total_page import get_total_page
from BOC_FER_Spider.utils.enum_variable import URL, CURRENCY_MAP


class BOCFERScrapySpider(scrapy.Spider):

    name = "BOC"

    def __init__(self,
                 start_time: str,
                 end_time: str,
                 currency_name: str,
                 incremental: int = 0):
        """
        中国银行外汇牌价查询爬虫
        :param start_time: 起始时间
        :param end_time: 结束时间
        :param currency_name: 货币类型
        :param incremental: 增量参数 默认为False
        """
        self._start_time = start_time
        self._end_time = end_time
        self._currency_name = currency_name
        self._incremental = int(incremental)

        # 启动的URL
        self.start_urls = [URL]

        super(BOCFERScrapySpider).__init__()

    def start_requests(self):
        self.logger.info("开始爬取!当前网址为: {}".format(self.start_urls[0]))
        total_page = get_total_page(start_time=self._start_time,
                                    end_time=self._end_time,
                                    currency_name=self._currency_name)
        post_data = {
            "erectDate": self._start_time,
            "nothing": self._end_time,
            "pjname": CURRENCY_MAP[self._currency_name],
            "page": str(1)
        }
        self.logger.info("开始下一页! 下一页为第 {} 页, 总共 {} 页!".format(str(1), total_page))
        yield scrapy.FormRequest(url=self.start_urls[0],
                                 method="POST",
                                 formdata=post_data,
                                 meta={'tp': total_page, 'post_data': post_data},
                                 dont_filter=True,
                                 callback=self.parse)

    def parse(self, response):
        # 房屋数据字典(为了兼容其他3.X版本使用了有序字典OrderDict)
        exchange_data = OrderedDict()
        # 汇率列表
        exchange_list = response.xpath('//div[@class="BOC_main publish"]/table/tr')
        for exchange in exchange_list[1:-1]:
            exchange_data['currency_name'] = exchange.xpath('string(td[1])').extract_first()
            exchange_data['buying_rate'] = exchange.xpath('string(td[2])').extract_first()
            exchange_data['cash_buying_rate'] = exchange.xpath('string(td[3])').extract_first()
            exchange_data['selling_rate'] = exchange.xpath('string(td[4])').extract_first()
            exchange_data['cash_selling_rate'] = exchange.xpath('string(td[5])').extract_first()
            exchange_data['boe_conversion_rate'] = exchange.xpath('string(td[6])').extract_first()
            exchange_data['rate_time'] = \
                time.strftime("%Y-%m-%d %H:%M:%S",
                              time.strptime(exchange.xpath('string(td[7])').extract_first(), "%Y.%m.%d %H:%M:%S"))
            exchange_data['md5_str'] = \
                str(hashlib.md5(
                    (exchange_data['rate_time'] + exchange_data['selling_rate']).encode('UTF-8')
                ).hexdigest()).upper()
            yield exchange_data
        # 获取meta的结果
        post_data = response.meta['post_data']
        total_page = response.meta['tp']
        # 判断是否为增量爬虫
        if self._incremental == 1:
            self.logger.info("增量爬取中!间隔时间为{}秒".format(str(INCREMENTAL_CRAWLER_TIME)))
            yield scrapy.FormRequest(url=self.start_urls[0],
                                     method="POST",
                                     formdata=post_data,
                                     meta={'tp': total_page, 'post_data': post_data},
                                     dont_filter=True,
                                     callback=self.parse)
            time.sleep(INCREMENTAL_CRAWLER_TIME)
        else:
            # 判断是否翻页
            next_page_num = int(post_data['page']) + 1
            if next_page_num <= total_page:
                post_data['page'] = str(next_page_num)
                self.logger.info("开始下一页! 下一页为第 {} 页, 总共 {} 页!".format(next_page_num, total_page))
                yield scrapy.FormRequest(url=self.start_urls[0],
                                         method="POST",
                                         formdata=post_data,
                                         meta={'tp': total_page, 'post_data': post_data},
                                         dont_filter=True,
                                         callback=self.parse)
            else:
                self.logger.info("爬取完毕!")
