import httplib
import json
from hashing import ConsistentHashRing
cr = ConsistentHashRing()



cr.__setitem__("server1","5001")
cr.__setitem__("server2","5002")
cr.__setitem__("server3","5003")

for i in xrange(1,11):
    port = cr.__getitem__(str(i))
    url = "localhost:" + str(port)
    print url
    connection = httplib.HTTPConnection(url)

    headers = {'Content-type': 'application/json'}

    foo = {
    "id": i,
    "category": "training",
    "description": "iPhone for training",
    "email": "foo1@bar.com",
    "estimated_costs": "6760",
    "link": "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "name": "Foo Bar",
    "submit_date": "09-08-2016"
    }
    json_foo = json.dumps(foo)
    url2 = "/v1/expenses"
    print url2
    connection.request('POST', url2, json_foo, headers)
    response = connection.getresponse()
    print(response.read().decode())

