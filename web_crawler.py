import requests
from bs4 import BeautifulSoup
import LineNotifyAPI as ln

url = 'https://www.books.com.tw/web/sys_cebtopb/cebook?loc=subject_004'


r = requests.get(url, timeout=10)
soup = BeautifulSoup(r.text,'html5lib')

lines = soup.find_all(class_='type02_bd-a')
count=0
collect=list()
for line in lines:
  s=''
  count += 1
  name = line.find('h4').text[:-6]
  link = line.find('a').get('href')
  book_id = link[34:44]
  s += ' TOP ' + str(count) + '\n'
  s += name + '\n'
  s += 'https://www.books.com.tw/products/' + book_id
  collect.append(s)
  if count >= 5:
    break

greeting = '又是美好的早晨！閱讀一本書，開啟新的一天吧 (*•̀ㅂ•́)و\n以下是博客來中文電子書暢銷榜前五名：\n'
ln.lineNotify(msg=greeting)
for st in collect:
  ln.lineNotify(msg=st)