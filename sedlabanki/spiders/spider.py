import scrapy

from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from ..items import SedlabankiItem
from itemloaders.processors import TakeFirst


class SedlabankiSpider(scrapy.Spider):
	name = 'sedlabanki'
	start_urls = ['https://www.sedlabanki.is/utgefid-efni/frettir-og-tilkynningar/frettasafn/?all=1']

	def parse(self, response):
		post_links = response.xpath('//h3/a/@href')
		for post in post_links:
			if post.get()[-1:] == r'/':
				yield response.follow(post, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//div[@class="media-body"]/h2/text()').get()
		description = response.xpath('//div[@class="media-body"]/p//text()').getall()
		description = ' '.join(description)
		date = response.xpath('//div[@class="media-body"]/div[@class="muted"]/text()').get()
		print(date)

		item = ItemLoader(item=SedlabankiItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()