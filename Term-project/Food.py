import http.client
from tkinter import INSERT
from xml.etree import ElementTree

KoreaList = []
ChinaList = []
JapanList = []
ItalyList = []
CafeList = []
FamousList = []

def URLbuilder(CategoryNum):   #카테고리별 URL
    global KEY
    if CategoryNum == 0:
        KEY = "/Genrestrtsoup?KEY=eacb09e4cc1e4b5f9bf7f14ebe87291b"
    elif CategoryNum == 1:
        KEY = "/Genrestrtchifood?KEY=062afd00409748bfbeedbd63d2851b62"
    elif CategoryNum == 2:
        KEY = "/Genrestrtjpnfood?KEY=55e63a8c30644642b07f671996903252"
    elif CategoryNum == 3:
        KEY = "/Genrestrtfastfood?KEY=308a1836ded941e69da26b59698c3c68"
    elif CategoryNum == 4:
        KEY = "/Genrestrtcate?KEY=46c5a83322734a8b83ae785069ca6619"
    elif CategoryNum == 5:
        KEY = "/PlaceThatDoATasteyFoodSt?KEY=de547a5cf35444bb9e49043ce00f4115"
    URLrequest(CategoryNum, KEY + str("&pSize=300"))

def URLrequest(CategoryNum, KEY):  # 카테고리별 파싱
    con = http.client.HTTPSConnection("openapi.gg.go.kr")
    con.request("GET", KEY)
    req = con.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        #print(temp)
        print("카테고리",CategoryNum + 1, "Data Downloading Complete!")
        if CategoryNum == 5:
            return XmlToList2(temp)
        else:
            return XmlToList1(CategoryNum, temp)
    else:
        print("OpenAPI request Failed!")

def XmlToList1(CategoryNum, xml):  # xml → 카테고리별(맛집 외) 리스트로
    tree = ElementTree.fromstring(xml)

    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')  # 시군명(1)
        Name = restaurant.find('BIZPLC_NM')  # 사업장명(3)
        RoadAddress = restaurant.find('REFINE_ROADNM_ADDR')  # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')  # 지번 주소(20)
        Post = restaurant.find('REFINE_ZIP_CD')  # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')  # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')  # 경도(23)

        if CategoryNum == 0:
            KoreaList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text])
        elif CategoryNum == 1:
            ChinaList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text])
        elif CategoryNum == 2:
            JapanList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text])
        elif CategoryNum == 3:
            ItalyList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text])
        elif CategoryNum == 4:
            CafeList.append([City.text, Name.text, RoadAddress.text, Address.text, Post.text, Lat.text, Long.text])

def XmlToList2(xml):  # xml → 맛집 리스트로
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

def getList(CategoryNum):
    if CategoryNum == 0:
        return KoreaList
    elif CategoryNum == 1:
        return ChinaList
    elif CategoryNum == 2:
        return JapanList
    elif CategoryNum == 3:
        return ItalyList
    elif CategoryNum == 4:
        return CafeList
    elif CategoryNum == 5:
        return FamousList