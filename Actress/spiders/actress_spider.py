# -*- coding: utf-8 -*-
import scrapy
from Actress.items import ActressItem


class ActressSpiderSpider(scrapy.Spider):
    name = 'actress_spider'
    allowed_domains = ['javbus.com']
    start_urls = [
        'https://www.javbus.com/actresses',
        'https://www.javbus.com/uncensored/actresses'
    ]

    def parse(self, response):
        hrefs = response.xpath('//a[contains(@class, "avatar-box")]/@href').extract()
        for href in hrefs:
            yield scrapy.Request(url=href, callback=self.parse_detail)

        next_page = response.xpath('//a[@id="next"]/@href').extract_first()
        if next is not None:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item = ActressItem()
        name = response.xpath('//span[contains(@class, "pb10")]/text()').extract_first()

        # 以下信息有误，以后再处理
        # birth = response.xpath('//div[@class="photo-info"]//p[1]/text()').extract_first()
        # age = response.xpath('//div[@class="photo-info"]//p[2]/text()').extract_first()
        # # 腰围
        # waist = response.xpath('//div[@class="photo-info"]//p[6]/text()').extract_first()
        # # 罩杯
        # cup = response.xpath('//div[@class="photo-info"]//p[4]/text()').extract_first()
        # # 胸围
        # bust = response.xpath('//div[@class="photo-info"]//p[5]/text()').extract_first()
        # # 臀围
        # hips = response.xpath('//div[@class="photo-info"]//p[7]/text()').extract_first()
        # # 身高
        # height = response.xpath('//div[@class="photo-info"]//p[3]/text()').extract_first()
        # 演员作品名
        film_list = response.xpath("//a[@class='movie-box']//span/text()").extract()
        # 作品番号
        tags = response.xpath("//a[@class='movie-box']//date[1]/text()").extract()
        # 作品时间
        dates = response.xpath("//a[@class='movie-box']//date[2]/text()").extract()

        item['name'] = name
        # item['age'] = age
        # item['birth'] = birth
        # item['waist'] = waist
        # item['hips'] = hips
        # item['cup'] = cup
        # item['bust'] = bust
        # item['height'] = height

        films = []
        for film in film_list:
            # 去除换行符的干扰字符
            afilm = film.strip('\t \n \r '' /')
            if afilm != '':
                films.append(afilm)
        for j in range(len(films)):
            item['film'] = films[j]
            item['tag'] = tags[j]
            item['date'] = dates[j]
            yield item
        next_page = response.xpath("//a[@id='next']/@href").extract_first()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_url, callback=self.parse_detail)




