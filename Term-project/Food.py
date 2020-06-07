import http.client
from tkinter import INSERT
from xml.etree import ElementTree

KoreaList = []
ChinaList = []
JapanList = []
ItalyList = []
CafeList = []
FamousList = []

AllList = []        # 그래프용 모든 카테고리 리스트
SearchList = []     # 검색용 리스트

City = "&SIGUN_NM="
SIGUN_NM = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']


def URLbuilder(Category):   #카테고리별 URL
    global KEY
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
    URLrequest(Category, KEY + str("&pSize=300"))

def URLrequest(Category, KEY):  # 카테고리별 파싱
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    con.request("GET", KEY)
    req = con.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        #print(temp)
        print(Category + "Data Downloading Complete!")
        if Category == "Famous":
            return XmlToList2(Category, temp)
        else:
            return XmlToList1(Category, temp)
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

def getList(Category):
    if Category == "Korea":
        return KoreaList
    elif Category == "China":
        return ChinaList
    elif Category == "Japan":
        return JapanList
    elif Category == "Italy":
        return ItalyList
    elif Category == "Cafe":
        return CafeList
    elif Category == "Famous":
        return FamousList