from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print ('Retrieving', url)
uh = urlopen(url).read()
print ('Retrieved',len(uh),'characters')
tree = ET.fromstring(uh)
results = tree.findall("comments/comment")
print ("Count: ",len(results))
sum=0
for i in results:
    sum+=int(i.find("count").text)
print (sum)