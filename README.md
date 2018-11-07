## 中国银行外汇牌价爬虫 (Spider for Bank Of China exchange rate)

---

<h3 id="Developer">开发者</h3>

* Core: sunhailin-Leo
* E-mail: 379978424@qq.com
* Wechat: 18666270636

---

<h3 id="DevEnv">开发环境</h3>

* 系统环境: Windows 10 x64
* Python版本: Python 3.6
* 编译器: Pycharm

---

<h3 id="ProjectInfo">项目简介</h3>

* 项目简介:
    1. 获取中国银行外汇牌价的汇率(本项目模板以港币为Base)
        * 爬虫地址：[网址](http://srh.bankofchina.com/search/whpj/search.jsp)
    2. 获取时间可以自定义(设置起始时间不建议跨度太长)

* 启动简介

```html
python cmdline_start_spider.py (参数)
```
或
```html
scrapy crawl BOC -a start_time={} -a end_time={} -a currency_name={} ({}需要自己填写)

* 注: start_time和end_time的格式是 YYYY-MM-DD; 
      currency_name 需要自行去currency_mapper中查看或到网页自行查看
```

* 文件简介:
    * BOC_FER_Spider
        * spiders: 爬虫
        * utils: 工具类
            * common_utils: 常用方法
            * currency_mapper: 货币映射规则
            * enum_variable: 全局变量
            * get_total_page: selenium(chrome headless 需要依赖chrome driver)获取全部页数
        * items: 数据字段
        * middlewares: 中间件(本项目没有进行修改)
        * pipelines: 数据管道(异步写入MySQL)
        * settings: Scrapy配置
    * cmdline_start_spider: 执行这个py或者自行输入命令启动也ok
---

<h3 id="Dependency">项目依赖</h3>

* Scrapy
* selenium
* pymysql

--- 

<h3 id="Future">未来开发方向</h3>

* 支持存储到MongoDB
* 集成pyecharts做数据可视化
