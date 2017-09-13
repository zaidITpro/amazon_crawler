# -*- coding: utf-8 -*-
import scrapy
from amazon_crawler.items import AmazonCrawlerItem
import re
import requests
from bs4 import BeautifulSoup


class AmazonSpider(scrapy.Spider):
  name = "amazon"
  allowed_domains = ["amazon.com"]
  
  #Use working product URL below''



  def get_product_id():
  	 linklist=[]
  	 url='https://www.amazon.in/Tupperware-Modular-Container-4-Pieces-Multicolor/dp/B00GQUTBSA/ref=sr_1_3?s=kitchen&rps=1&ie=UTF8&qid=1505278591&sr=1-3&refinements=p_98%3A10440597031%2Cp_n_pct-off-with-tax%3A2665399031'
  	 headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
  	 response=requests.get(url,headers=headers)
  	 page_html=BeautifulSoup(response.content)
  	 links=page_html.find_all('a')
  	 for tag in links:
  	 	 link=tag.get('href',None)
  	 	 if link is not None:
  	 	 	 linklist.append(link)
  	 	 else:
  	 	 	 pass
  	 linkhref=[]
  	 asin_regex=r'/([A-Z0-9]{10})'
  	 for link in linklist:
  	 	 result=re.search(asin_regex,link)
  	 	 if result:
  	 	 	 if result.group(1) not in linkhref:
  	 	 	 	linkhref.append(result.group(1))
  	 	 	 else:
  	 	 	 	pass
  	 	 else:
  	 	 	 pass
  	 for id in range(0,len(linkhref)):
  	 	 linkhref[id]='https://www.amazon.in/dp/'+linkhref[id]
  	 return linkhref
  	 pass

  def get_links():
  	pass


  start_urls=get_product_id()




 
  def parse(self, response):
     items = AmazonCrawlerItem()
     title = response.xpath('//h1[@id="title"]/span/text()').extract()
     sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
     category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
     availability = response.xpath('//div[@id="availability"]//text()').extract()
     items['product_name'] = ''.join(title).strip()
     items['product_sale_price'] = ''.join(sale_price).strip()
     items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     items['product_availability'] = ''.join(availability).strip()
     yield items
