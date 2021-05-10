import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL")
soup=BeautifulSoup(html, "lxml")

start_table=soup.find_all('div',{'class':'chart'})

tbody=start_table[0].find_all('tr')

list = []
for tr in tbody:
    a = []
    rank=tr.find_all("td",{'class':'ranking'})
    sub=tr.find_all('td',{'class':'subject'})
    count=tr.find_all('td',{'class':'count'})

    for i in rank:
        b = i.get_text()
        b = b.replace('\n','')
        print(b,end=' ')
        a.append(b)

    for i in sub:
        b = i.get_text()
        b = b.replace('\n', '')
        print(b, end=' ')
        a.append(b)

    for i in count:
        b = i.get_text()
        b = b.replace('\n', '')
        print(b)
        a.append(b)
    list.append(a)
del list[0]

