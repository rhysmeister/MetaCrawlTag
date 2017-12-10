from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urlparse import urlparse
import os

class MySpider(CrawlSpider):
    name = 'MySpider'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
    }
    from urlparse import urlparse

    #meta_name = None
    #meta_value = None

    def __init__(self, url=None, meta_name=None, meta_value=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        os.remove('tag_and_value_found_urls_output.txt') if os.path.exists('tag_and_value_found_urls_output.txt') else None
        os.remove('tag_found_not_value_urls_output.txt') if os.path.exists('tag_found_not_value_urls_output.txt') else None
        os.remove('tag_not_found_urls_output.txt') if os.path.exists('tag_not_found_urls_output.txt') else None
        parsed_uri = urlparse(url)
        self.name = parsed_uri.netloc
        self.allowed_domains = [parsed_uri.netloc.replace('www.', '')]
        self.start_urls = [url]
        self.meta_name = meta_name
        self.meta_value = meta_value

    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse_item(self, response):
        c = response.xpath("//meta[@name='{0}']/@content".format(self.meta_name))
        if c:
            all_meta_values = []
            for item in c.extract():
                for i in item.splitlines():
                    for word in i.split(","):
                        all_meta_values.append(word.lower())
            if self.meta_value in all_meta_values:
                with open('tag_and_value_found_urls_output.txt', 'a') as f:
                    f.write("{0}|{1}\n".format(response.url, str(all_meta_values)))
            else:
                with open('tag_found_not_value_urls_output.txt', 'a') as f:
                    f.write("{0}|{1}\n".format(response.url, str(all_meta_values)))
        else:
            with open('tag_not_found_urls_output.txt', 'a') as f:
                f.write(response.url + "\n")
