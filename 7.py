import json
from urllib.request import urlopen

address = input('Enter location: ')
print ('Retrieving', address)
uh = urlopen(address)
data = uh.read()
js = json.loads(data.decode("utf-8"))
print ('Retrieved',len(data),'characters')
lst=js["comments"]
print ("count: ",len(lst))
sum=0
for i in lst:
    sum+=i["count"]
print (sum)