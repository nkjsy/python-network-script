from urllib.request import urlopen
from bs4 import BeautifulSoup
url=input("Enter url: ")
count=int(input("Enter count: "))
position=int(input("Enter position: "))

while count>0:
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    url=tags[position-1].get("href",None)
    print ("Retrieving: ",url)
    count-=1