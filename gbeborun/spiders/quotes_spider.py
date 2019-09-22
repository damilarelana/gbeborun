# import the scrapy package
import scrapy


# QuotesSpider() class
class QuotesSpider(scrapy.Spider):  # make a new class based on the base class scrapy.Spider
    name = "quotes"   # name of the spider

    # define class method `start_requests` : which initiates crawling requests
    def start_requests(self):
        urls = [
          'http://quotes.toscrape.com/page/1/',
          'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.data_extractor)  # start request, then use class method parse() to handle the response

    # def parse(self, response):
    #     page = response.url.split("/")[-2]  # extract the page number i.e. 2nd element from the back
    #     filename = 'quotes-%.html' % page  # use extracted page number to autogenerate a filename
    #     with open(filename, 'wb') as f:  # open the file (as `writable binary`) and do not close it until data has been written
    #         f.write(response.body)  # extract the binary response data and save to file
    #     self.log('Saved file %s' % filename)  # log the newly created filename

    def data_extractor(self, response):
        for quote in response.css('div.quote'):  # iterate through the response to extract the quote
            yield {
                'text': quote.css('span.text::text').get(),  # css selectors are use to extract the data
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),  # see how selectors are chained
            }