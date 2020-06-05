import http.client

KoreaKEY = "KEY=eacb09e4cc1e4b5f9bf7f14ebe87291b"
ChinaKEY = "KEY=062afd00409748bfbeedbd63d2851b62"
JapanKEY = "KEY=55e63a8c30644642b07f671996903252"
ItalyKEY = "KEY=308a1836ded941e69da26b59698c3c68"
CafeKEY = "KEY=46c5a83322734a8b83ae785069ca6619"
FamousKEY = "KEY=de547a5cf35444bb9e49043ce00f4115"

City = "&SIGUN_NM="
SIGUN_NM = ["가평군", '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
        '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
        '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
        '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

def SearchFamous():
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    #for i in range(31):
    con.request("GET", "/PlaceThatDoATasteyFoodSt?"+KEY+pIndex+pSize, None)
    req = con.getresponse()
    #print(req.status, req.reason)
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

    #print(food)

SearchFamous()