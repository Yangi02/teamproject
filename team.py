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

r = []
s = []
c = []

cyc = 0
for i in list:
    cyc += 1
    r.append(i[0])
    s.append(i[1])
    c.append(i[2])
    if cyc == 10:
        break

r = [int(i) for i in r]

nc = []
for i in c:
    i = i.replace(',','')
    i = int(i)
    nc.append(i)

print('')
print(r)
print(s)
print(nc)

matplotlib.rcParams['axes.unicode_minus']=False
plt.rc('font',family='Malgun Gothic')

plt.suptitle('가온차트 top10')
plt.ylabel('가온지수')
plt.bar(r,nc,color='purple')
plt.axis([0,11,15000000,35000000])
plt.xticks(r,s,rotation='vertical')
plt.show()