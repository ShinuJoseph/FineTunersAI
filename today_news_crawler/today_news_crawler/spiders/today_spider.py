# importing the necessary libraries.
import scrapy

# creating the spider class.
class TodaySpider(scrapy.Spider):
    name = 'today_spider'
    start_urls = ['https://www.today.com/archive/articles/2023/november']

    # parsing the main page.
    def parse(self, response):
        main = response.xpath("//main[@class='MonthPage']")
        for a in main.xpath(".//a"):
            link = a.xpath("./@href").get()
            title = a.xpath("./text()").get()
            yield scrapy.Request(url=link, callback=self.parse_link, meta={'title': title})

    def parse_link(self, response):
        content = response.xpath("//p/text()").getall()
        yield {
            "link": response.url,
            "title": response.meta['title'],
            "content": " ".join(content)
        }
