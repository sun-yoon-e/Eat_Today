import http.client

#맛집 : https://openapi.gg.go.kr/PlaceThatDoATasteyFoodSt?KEY=47d93cfef7644a4c8fe8144d1ac72638

server = "openapi.gg.go.kr"
KEY = "KEY=47d93cfef7644a4c8fe8144d1ac72638"

def SearchFamous():
    conn = http.client.HTTPSConnection(server)
    conn.request("GET", "/PlaceThatDoATasteyFoodSt?" + str(KEY), None)
    req = conn.getresponse()
    print(req.status, req.reason)
    temp = req.read().decode('utf-8')
    print(temp)

    #food = []
    #temp = req.read().decode('utf-8')
    #if int(req.status) == 200:
    #    print(3)
    #    tree = ElementTree.fromstring(temp)
    #    itemElements = tree.iter("list")
    #    for item in itemElements:
    #        temp = item.find("row")
    #        food.append(temp)

SearchFamous()