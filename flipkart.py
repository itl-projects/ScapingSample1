import scrapy

class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    start_urls = 'https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles'
    next_page= response.css('._29UPft')
    print(next_page)
