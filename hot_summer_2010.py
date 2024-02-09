import scrapy


class HotSummer2010Spider(scrapy.Spider):
    name = "hot_summer_2010"
    allowed_domains = ["w.wiki"]
    start_urls = ["https://w.wiki/97hM"]

    def parse(self, response, **kwargs):
        """
        :param response:
        :return:
        """
        list_items = response.xpath(".//table[@class='wikitable sortable'][1]/tbody/tr")
        for row in list_items[1:]:
            yield {
                'City': row.xpath(".//td/a/text()").get(),
                'Meteostation': row.xpath(".//td[2]/text()").get(),
                'Max t, \u2103': row.xpath(".//th/text()").get(),
                'Known dates': row.xpath(".//td[3]/text()").get() + row.xpath(".//td[3]/p/text()").get()
            }
