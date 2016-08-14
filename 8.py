import json
from urllib.request import urlopen
from urllib.parse import urlencode
serviceurl="http://python-data.dr-chuck.net/geojson?"
address=input("Enter Location: ")
url = serviceurl + urlencode({'sensor': 'false', 'address': address})
print('Retrieving', url)
uh = urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
js=json.loads(data.decode("utf-8"))
print ("place id: ",js["results"][0]["place_id"])