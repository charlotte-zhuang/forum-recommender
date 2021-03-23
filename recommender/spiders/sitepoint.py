import scrapy
import json


class SitepointSpider(scrapy.Spider):
    name = 'sitepoint'
    allowed_domains = ['sitepoint.com']
    topic_root_url = 'https://www.sitepoint.com/community/t'
    topic_req_url = 'https://www.sitepoint.com/community/latest.json?no_definitions=true&page='
    start_urls = [topic_req_url + '1']
    page_limit = 100
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_MAX_DELAY': 5.0,
        'AUTOTHROTTLE_START_DELAY': 0.1
    }

    def parse(self, response):
        # scrape from feed
        # for topic in response.xpath('//tr[@class="topic-list-item"]'):
        #     yield {
        #         'title': topic.xpath('.//a[contains(@class, "title")]/text()').extract_first(),
        #         'url': topic.xpath('.//a[contains(@class, "title")]/@href').extract_first(),
        #         'cat': topic.xpath('.//span[contains(@class, "category-name")]/text()').extract_first(),
        #         'tags': topic.xpath('.//a[contains(@class, "discourse-tag")]/text()').extract()
        #     }

        # follow pages from feed
        # for topic in response.xpath('//a[contains(@class, "title")]/@href'):
        #     yield response.follow(
        #         topic,
        #         callback=self.parse_topic
        #     )

        # follow pages from json
        data = json.loads(response.body)

        for topic in data.get('topic_list', {}).get('topics', []):
            url = f'{self.topic_root_url}/{topic.get("slug")}/{topic.get("id")}'
            yield response.follow(url, callback=self.parse_topic)

        page_index = int(response.url[len(self.topic_req_url) :])
        if page_index < self.page_limit:
            yield scrapy.Request(self.topic_req_url + str(page_index + 1))

            

    def parse_topic(self, response):
        yield {
            'title': response.xpath('//div[contains(@id, "topic-title")]//a/text()').extract_first(),
            'category': response.xpath('//span[contains(@class, "category-name")]/text()').extract_first(),
            'tags': response.xpath('//a[contains(@class, "discourse-tag")]/text()').extract(),
            'post': response.xpath('//div[contains(@class, "topic-body")]')[0].xpath('.//p/text()').extract()
        }
        # get all text: response.xpath('//div[contains(@class, "topic-body")]//p/text()').extract()
