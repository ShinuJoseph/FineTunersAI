# Importing the necessary libraries.
import scrapy

# Creating the spider class.
class TodaySpider(scrapy.Spider):
    # Setting the spider name and initial URL.
    name = 'today_spider'
    start_urls = ['https://www.today.com/archive/articles/2013/december']

    # Parsing the main page.
    def parse(self, response):
        # Extracting the main section of the page.
        main = response.xpath("//main[@class='MonthPage']")
        
        # Iterating through the links in the main section.
        for a in main.xpath(".//a"):
            # Extracting link and title from each link.
            link = a.xpath("./@href").get()
            title = a.xpath("./text()").get()
            
            # Making a request to the link and calling parse_link function with additional metadata.
            yield scrapy.Request(url=link, callback=self.parse_link, meta={'title': title})

    # Parsing the individual link page.
    def parse_link(self, response):
        # Extracting the content from the link page.
        content = response.xpath("//p").getall()
        
        # Yielding a dictionary containing link, title, and content.
        yield {
            "link": response.url,
            "title": response.meta['title'],
            "content": " ".join(content)
        }
