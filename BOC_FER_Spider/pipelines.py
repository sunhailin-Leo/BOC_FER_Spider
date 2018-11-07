# -*- coding: utf-8 -*-
import copy
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

# 项目内部库
from BOC_FER_Spider.utils.enum_variable import INSERT_SQL


class BocFerSpiderPipeline(object):
    """
    保存到数据库中对应的class
    1、在settings.py文件中配置
    2、在自己实现的爬虫类中yield item,会自动执行
    """
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        """
        1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
        2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
        3、可以通过类来调用，就像C.f()，相当于java中的静态方法
        """
        # 读取settings中配置的数据库参数
        db_params = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=cursors.DictCursor,
            use_unicode=False,
        )
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        # 相当于db_pool赋值给了这个类，self中可以得到
        return cls(db_pool)

    # pipeline默认调用
    def process_item(self, item, spider):
        # 对象拷贝，深拷贝
        async_item = copy.deepcopy(item)
        query = self.db_pool.runInteraction(self._conditional_insert, async_item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    # 写入数据库中
    # SQL语句在这里
    def _conditional_insert(self, tx, item):
        params = (
                   item['currency_name'],
                   item['buying_rate'],
                   item['cash_buying_rate'],
                   item['selling_rate'],
                   item['cash_selling_rate'],
                   item['boe_conversion_rate'],
                   item['rate_time'])
        tx.execute(INSERT_SQL, params)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print(failue)


