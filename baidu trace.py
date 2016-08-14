from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlencode
serviceurl="http://api.map.baidu.com/trace/v2/entity/add"
url=serviceurl+urlencode({"service_id":122182,"ak":"nFsfdYhtApLgU6pj7M3qQ5ptKF2KByGI"})
html=urlopen(url).read()
soup=BeautifulSoup(html)
print(soup)
