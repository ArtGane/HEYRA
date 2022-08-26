import scrapy


class Jdd(scrapy.Spider):
    name = "title"
    start_urls = ["https://order.cdiscount.com/Account/LoginLight.html?referrer="]
