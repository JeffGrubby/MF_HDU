# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

# USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True

DOWNLOADER_MIDDLEWARES  = {
    # 该中间件将会收集失败的页面，并在爬虫完成后重新调度。（失败情况可能由于临时的问题，例如连接超时或者HTTP 500错误导致失败的页面）
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,

    # 该中间件提供了对request设置HTTP代理的支持。您可以通过在 Request 对象中设置 proxy 元数据来开启代理。
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
    # 'example.middlewares.ProcessAllExceptionMiddleware': 543,
    # 'example.middlewares.RotateUserAgentMiddleware': 200,
}

ITEM_PIPELINES = {
    # 'example.pipelines.ExamplePipeline': 300,
    'example.pipelines.MeoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# REDIS_URL = 'redis://localhost:6379'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'Meo'  # database name
MONGODB_DOCNAME = 'Girl'  # table name

# 启用或禁用蜘蛛中间件
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'demo1.middlewares.Demo1SpiderMiddleware': 543,
# }

# 启用或禁用下载器中间件
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'demo1.middlewares.MyCustomDownloaderMiddleware': 543,