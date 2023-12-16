# Importing the necessary libraries.
import scrapy

class TodaySpider(scrapy.Spider):
    name = 'today_spider'
    start_urls = ['https://www.today.com/archive/articles/2023/october']

    def parse(self, response):
        main = response.xpath("//main[@class='MonthPage']")

        for a in main.xpath(".//a"):
            link = a.xpath("./@href").get()
            title = a.xpath("./text()").get()

            yield scrapy.Request(url=link, callback=self.parse_link, meta={'title': title})

    def parse_link(self, response):
        content = response.xpath("//p").getall()

        # Join the paragraphs using "\n" to preserve line breaks
        content_with_line_breaks = "\n".join(content)

        yield {
            "link": response.url,
            "title": response.meta['title'],a
            "content": content_with_line_breaks
        }

