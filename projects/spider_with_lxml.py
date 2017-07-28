
import requests
from lxml import etree

base = 'https://movie.douban.com/top250?start=0'

res = requests.get(url=base)

text = res.text
data = etree.HTML(text.lower())

# 一步一步查找 step by step
# items = data.xpath(
#     '//div[@id="wrapper"]/div[@id="content"]/div[@class="grid-16-8 clearfix"]/div[@class="article"]/ol[@class="grid_view"]/li/div[@class="item"]')

# 一步到位 One pace reachs the designated position
items = data.xpath(
    '//div[@class="item"]')

# 从item 子节点进行查找
for i in items:
    divs = i.xpath('./div')
    pic = divs[0].xpath('./a')

    print('名称', pic[0].xpath('./img')[0].get('alt'))
    print('封面', pic[0].xpath('./img')[0].get('src'))
