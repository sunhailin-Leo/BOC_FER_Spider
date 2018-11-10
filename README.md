## 中国银行外汇牌价爬虫 (Spider for Bank Of China exchange rate)

---

<h3 id="Developer">开发者</h3>

* Core: sunhailin-Leo
* E-mail: 379978424@qq.com
* Wechat: 18666270636

* **在使用中如果有啥功能需求或者出现BUG的话, 欢迎提ISSUE或者直接联系我~**

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
    3. 通过cmdline_start_spider支持自定义存储路径(MySQL,MongoDB,CSV)

* 启动简介

```html
例子: python cmdline_start_spider.py -s (起始日期YYYY-MM-DD) -e (结束日期YYYY-MM-DD) -c (货币名称) -o (可选参数:MySQL | MongoDB | CSV)
使用范例: python cmdline_start_spider.py -s 2018-11-07 -e 2018-11-07 -c 港币 -o MySQL | MongoDB | CSV
```
或
```html
scrapy crawl BOC -a start_time={} -a end_time={} -a currency_name={} ({}需要自己填写)
注： 通过scrapy命令启动暂时不支持选择MySQL或MongoDB

* 注: start_time和end_time的格式是 YYYY-MM-DD; 
      currency_name 需要自行去currency_mapper中查看或到网页自行查看
```

* 文件简介:
    * BOC_FER_Spider
        * spiders: 爬虫
        * utils: 工具类
            * common_utils: 常用方法
            * enum_variable: 全局变量
            * get_total_page: selenium(chrome headless 需要依赖chrome driver)获取全部页数
        * items: 数据字段
        * middlewares: 中间件(本项目没有进行修改)
        * pipelines: 数据管道(异步写入MySQL)
        * settings: Scrapy配置
    * cmdline_start_spider: 执行这个py或者自行输入命令启动也ok
    * README.md: 说明文档
    * requirements.txt: 依赖文档
    * scrapy.cfg: Scrapy的框架配置
---

<h3 id="Dependency">项目依赖</h3>

* Scrapy
* selenium (需要配置chrome driver)
* pymysql
* pymongo

--- 

<h3 id="Future">未来开发方向</h3>

~~* 支持存储到MongoDB~~

~~* 支持存储到csv或者excel中~~

* 当日增量爬虫(可能需要借助Redis或者其他媒介进行爬虫状态存储)

* 集成pyecharts做数据可视化(导出数据图表文件)

* 支持将数据发到Kafka或者其他MQ中(实时计算的扩展) -- 考虑中...

---

<h3 id="ChangeLog">更新文档</h3>

* 版本 - v1.0 - 2018-11-07:
    * 基本实现爬虫功能以及存储功能
    * 支持自定义时间爬取
    * 支持页面可选的货币汇率纪录爬取

* 版本 - v1.1 - 2018-11-08:
    * 增加MySQL建表初始化的代码
    * 支持MySQL和MongoDB的数据自定义存储(通过cmdline_start_spider的命令参数实现, scrapy crawl命令暂时没实现)
    * 移除currency_mapper文件, 将映射字典放到enum_variable中

* 版本 - v1.2 - 2018-11-09:
    * 增加CSV导出的支持(可以配置csv的文件名和存放路径)
    
* 版本 - v1.3 - 2018-11-10:
    * 修复了多处细节错误
    * 增加了chrome driver在项目目录中
    