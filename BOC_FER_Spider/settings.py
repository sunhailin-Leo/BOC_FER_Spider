# -*- coding: utf-8 -*-

BOT_NAME = 'BOC_FER_Spider'

SPIDER_MODULES = ['BOC_FER_Spider.spiders']
NEWSPIDER_MODULE = 'BOC_FER_Spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = \
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# MySQL配置
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = ""
MYSQL_DB_NAME = "exchange_rate"
MYSQL_TABLE_NAME = "t_exchange_rate_1"
MYSQL_CHARSET = "utf8"

# MONGODB配置
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_USER = ""
MONGODB_PASS = ""
MONGODB_DB_NAME = "db_exchange_rate"
MONGODB_COL_NAME = "t_rate"

# CSV配置
# 注: 默认保存路径放到根目录下
# 如果CSV文件名不为空则按定义的名称进行保存, 如果为空则格式为: export_货币名称_起始时间_结束时间.csv (时间都去掉"-"符号)
CSV_FILE_NAME = {
    "FILE_NAME": "",
    "FILE_SUFFIX": ".csv"
}
# 最好不要修改
CSV_DEFAULT_HEADER = ['货币名称', '现汇买入价', '现钞买入价', '现汇卖出价', '现钞卖出价', '中行折算价', '发布时间']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "Content-Type": "application/x-www-form-urlencoded",
  "Host": "srh.bankofchina.com",
  "Origin": "http://srh.bankofchina.com",
  "Referer": "http://srh.bankofchina.com/search/whpj/search.jsp",
  "Upgrade-Insecure-Requests": "1",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'BOC_FER_Spider.middlewares.BocFerSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'BOC_FER_Spider.middlewares.BocFerSpiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 配置ITEM PIPELINES
ITEM_PIPELINES = {
    'BOC_FER_Spider.pipelines.BocFerSpiderMySQLPipeline': 1,
    # 'BOC_FER_Spider.pipelines.BocFerSpiderMongoDBPipeline': 1
    # 'BOC_FER_Spider.pipelines.BocFerSpiderCSVPipeline': 1
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
