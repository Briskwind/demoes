import requests
from bs4 import BeautifulSoup

base = 'https://movie.douban.com/top250?start={start}'

movies_sum = 0
for i in range(0, 10):

    url = base.format(start=i * 25)
    res = requests.get(url=url)

    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.find_all("div", {"class": "item"})

    for item in items:
        movies_sum += 1

        try:
            movie_name = item.find('span', {'class': 'title'}).text
            pic = item.img.attrs['src']

            introduction = item.find_all('span', {'class': 'inq'})
            if introduction:
                introduction[0].text

            director = item.find_all('p', {'class': ''})
            if director:
                director[0].text
            print('movie_name', movie_name)

        except Exception as e:
            print('error message', e, item)

print('movies_sum', movies_sum)