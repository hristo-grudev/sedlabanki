BOT_NAME = 'sedlabanki'

SPIDER_MODULES = ['sedlabanki.spiders']
NEWSPIDER_MODULE = 'sedlabanki.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'sedlabanki.pipelines.SedlabankiPipeline': 100,

}