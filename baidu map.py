import json
from urllib.request import urlopen
from urllib.parse import urlencode
serviceurl="http://api.map.baidu.com/place/v2/suggestion?"
while True:
    address=input("Enter Location: ")
    if len(address)<1: break
    url=serviceurl+urlencode({"query":address,"region":131,"output":"json","ak":"nFsfdYhtApLgU6pj7M3qQ5ptKF2KByGI"})
    print ("Retrieving",url)
    data=urlopen(url).read()
    print ("Retrieved",len(data),"characters")
    try:
        js = json.loads(data.decode("utf-8"))
    except:
        js = None
    if 'status' not in js or js['status'] != 0:
        print ('==== Failure To Retrieve ====')
        continue
    #print (js)
    for i in js["result"]:
        print (" Name: ",i["name"]," City: ",i["city"]," District: ",i["district"])
        #print ("\n")
