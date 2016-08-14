from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://www.baidu.com/'
html=urlopen(url).read()
soup=BeautifulSoup(html)
#print (html)
#print (soup)
print (soup.a)