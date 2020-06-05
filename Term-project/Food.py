import http.client
from xml.etree import ElementTree

KoreaList = []
ChinaList = []
JapanList = []
ItalyList = []
CafeList = []
FamousList = []

AllList =[]     #그래프용 모든 카테고리 리스트
SearchList = [] #검색용 리스트

def URLbuilder(Category):   #카테고리별 URL
    if Category == "Korea":
        KEY = "/Genrestrtsoup?KEY=eacb09e4cc1e4b5f9bf7f14ebe87291b"
    elif Category == "China":
        KEY = "/Genrestrtchifood?KEY=062afd00409748bfbeedbd63d2851b62"
    elif Category == "Japan":
        KEY = "/Genrestrtjpnfood?KEY=55e63a8c30644642b07f671996903252"
    elif Category == "Italy":
        KEY = "/Genrestrtfastfood?KEY=308a1836ded941e69da26b59698c3c68"
    elif Category == "Cafe":
        KEY = "/Genrestrtcate?KEY=46c5a83322734a8b83ae785069ca6619"
    elif Category == "Famous":
        KEY = "/PlaceThatDoATasteyFoodSt?KEY=de547a5cf35444bb9e49043ce00f4115"

    URLrequest(Category, KEY)

def URLrequest(Category, KEY):   #카테고리별 파싱
    conn = http.client.HTTPSConnection("openapi.gg.go.kr")
    conn.request("GET", KEY)
    req = conn.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        print("Data Downloading Complete!")
        if Category == "Famous":
            return XmlToList2(Category, temp)
        else: return XmlToList1(Category, temp)
    else:
        print("OpenAPI request Failed!")

def XmlToList1(Category, xml):  # xml → 카테고리별(맛집 외) 리스트로
    tree = ElementTree.fromstring(xml)

    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')  # 시군명(1)
        Name = restaurant.find('BIZPLC_NM')  # 사업장명(3)
        RoadAdress = restaurant.find('REFINE_ROADNM_ADDR')  # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')  # 지번 주소(20)
        Post = restaurant.find('REFINE_ZIP_CD')  # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')  # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')  # 경도(23)

        if Category == "Korea":
            KoreaList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])
        elif Category == "China":
            ChinaList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])
        elif Category == "Japan":
            JapanList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])
        elif Category == "Italy":
            ItalyList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])
        elif Category == "Cafe":
            CafeList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])

def XmlToList2(Category, xml):  # xml → 맛집 리스트로
    tree = ElementTree.fromstring(xml)

    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')  # 시군명(1)
        Name = restaurant.find('RESTRT_NM')  # 사업장명(3)
        RoadAdress = restaurant.find('REFINE_ROADNM_ADDR')  # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')  # 지번 주소(20)
        Post = restaurant.find('REFINE_ZIP_CD')  # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')  # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')  # 경도(23)

        FamousList.append([City.text, Name.text, RoadAdress.text, Address.text, Post.text, Lat.text, Long.text])

URLbuilder("Korea")
URLbuilder("China")
URLbuilder("Japan")
URLbuilder("Italy")
URLbuilder("Cafe")
URLbuilder("Famous")

print(KoreaList)
print(ChinaList)
print(JapanList)
print(ItalyList)
print(CafeList)
print(FamousList)
