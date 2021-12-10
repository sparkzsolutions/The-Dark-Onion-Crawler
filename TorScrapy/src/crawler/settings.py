DOWNLOADER_MIDDLEWARES = {
	## User agent
	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	#need pip install scrapy_fake_useragent  (in conda)
	'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,

	## Proxy (privoxy + tor) 
	#cf https://trevsewell.co.uk/scraping/anonymous-scraping-scrapy-tor-polipo/
	# activate http proxy (turn on proxy)
	'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
	# call the middleware to customize the http proxy  (set proxy to 'http://127.0.0.1:8118')
	'gumtree.middlewares.ProxyMiddleware': 100,

}
DOWNLOAD_DELAY = 1
#HTTP_PROXY = 'http://tor-proxy:8118'
# # # # ROBOTSTXT_OBEY = False
# DOWNLOAD_TIMEOUT = 180
# # # HTTPCACHE_ENABLED = False

# # ROBOTSTXT_OBEY = False
#FAKEUSERAGENT_FALLBACK = 'Mozilla/5.0 (Android; Mobile; rv:40.0)'
#DUPEFILTER_DEBUG = True



# REACTOR_THREADPOOL_MAXSIZE = 20
# LOG_LEVEL = 'INFO'
# COOKIES_ENABLED = False
# RETRY_ENABLED = False
# DOWNLOAD_TIMEOUT = 15
# REDIRECT_ENABLED = False
# AJAXCRAWL_ENABLED = True
# DNSCACHE_ENABLED = True