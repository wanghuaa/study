

import requests
from bs4 import BeautifulSoup

import pymongo
url='http://www.qu.la/book/24868/'



def start_url():
    all_url=requests.get(url).text
    try:
        return all_url
    except:

        print('获取不到源码')


def all_url(start1):
    all_urls=BeautifulSoup(start1,'lxml').find('div',id='list').find_all('dd')
    for i in all_urls:
        url_='http://www.qu.la'+i.a['href']
        print(url_)
        yield url_


def Content_Titie(i):
    list=requests.get(i).text
    all_list=BeautifulSoup(list,'lxml').find('div','box_con')
    title=all_list.find('div','bookname').h1.get_text()
    content=all_list.find('div',id='content').get_text()
    dict={'title':title.strip(),
          'content':content.strip()
          }
    Mongo(dict)


def Mongo(i):
    connent=pymongo.MongoClient()
    db=connent['biqu810']['data']
    db.insert(i)


if __name__ == '__main__':
  start1=start_url()
  all_url1=all_url(start1)
  for i in all_url1:

    Content_Titie(i)