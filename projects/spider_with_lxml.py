import requests
from lxml import etree

base = 'https://movie.douban.com/top250?start={start}'

movies_sum = 0
for i in range(0, 10):

    url = base.format(start=i * 25)
    res = requests.get(url=url)

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
        movie_name = None

        movie_pic = None
        movie_review = None

        movies_sum += 1
        divs = i.xpath('./div')

        if divs:
            pic = divs[0].xpath('./a')
            if pic:
                movie_name = pic[0].xpath('./img')[0].get('alt')
                movie_pic = pic[0].xpath('./img')[0].get('src')

        if divs is not None:
            introduction = divs[1].xpath('./div[@class="bd"]/p[@class="quote"]/span[@class="inq"]')
            if introduction:
                movie_review = introduction[0].text

        print('名称', movie_name)
        print('封面', movie_pic)
        print('简介', movie_review)
        print('======')

print('movies_sum', movies_sum)
