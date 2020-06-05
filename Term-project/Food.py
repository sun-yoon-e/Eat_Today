import http.client
from xml.etree import ElementTree

KoreaList = []
ChinaList = []
JapanList = []
ItalyList = []
CafeList = []
FamousList = []

AllList = []  # 그래프용 모든 카테고리 리스트
SearchList = []  # 검색용 리스트

City = "&SIGUN_NM="
SIGUN_NM = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']


def URLrequest(Category):  # 카테고리별 파싱
    conn = http.client.HTTPSConnection("openapi.gg.go.kr")
    conn.request("GET", Category)
    req = conn.getresponse()

    if req.status == 200:
        temp = req.read().decode('utf-8')
        # print(temp)
        print("Data Downloading Complete!")
        return putXmlToList(temp)
    else:
        print("OpenAPI request Failed!")


def putXmlToList(xml):  # xml->카테고리별 리스트로
    tree = ElementTree.fromstring(xml)
    for restaurant in tree.findall('./row'):
        City = restaurant.find('SIGUN_NM')  # 시군명(1)
        Name = restaurant.find('BIZPLC_NM')  # 사업장명(3)
        RoadAdress = restaurant.find('REFINE_ROADNM_ADDR')  # 도로명 주소(19)
        Address = restaurant.find('REFINE_LOTNO_ADDR')  # 지번 주소(20)
        Post = restaurant.find('REFINE_ZIP_CD')  # 우편 번호(21)
        Lat = restaurant.find('REFINE_WGS84_LAT')  # 위도(22)
        Long = restaurant.find('REFINE_WGS84_LOGT')  # 경도(23)

        print(City.text)
        print(Name.text)
        print(RoadAdress.text)
        print(Address.text)
        print(Post.text)
        print(Lat.text)
        print(Long.text)