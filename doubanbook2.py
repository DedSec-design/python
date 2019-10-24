from lxml import etree
import requests
import re
import pymongo

client = pymongo.MongoClient(',7)
mydb = client['mydb']
musictop = mydb['']

writer.writerow(('name', 'url',  'author', 'publisher', 'date', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

for url in urls:
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
