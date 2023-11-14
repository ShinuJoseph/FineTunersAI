import scrapy
import csv

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        # Open the CSV file in append mode
        with open('quotes.csv', 'a', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['text', 'author', 'tags']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header if the file is empty
            if csv_file.tell() == 0:
                writer.writeheader()

            # Extract data from the web page using CSS selectors or XPath expressions
            for quote in response.css('div.quote'):
                text = quote.css('span.text::text').get()
                author = quote.css('small.author::text').get()
                tags = quote.css('div.tags a.tag::text').getall()

                # Write the data directly to the CSV file
                writer.writerow({
                    'text': text,
                    'author': author,
                    'tags': tags,
                })

            # Follow pagination links
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
