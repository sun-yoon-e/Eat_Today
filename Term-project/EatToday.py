from tkinter import *
from tkinter import font
import Food

bgColor = 'lemon chiffon'
MailList = []
KoreaList = []
ChinaList = []
JapanList = []
ItalyList =[]
CafeList = []
FamousList = []
CityList = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
        '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
        '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
        '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

CategoryButton = 0
KoreaKEY = "/Genrestrtsoup?KEY=eacb09e4cc1e4b5f9bf7f14ebe87291b"
ChinaKEY = "/Genrestrtchifood?KEY=062afd00409748bfbeedbd63d2851b62"
JapanKEY = "/Genrestrtjpnfood?KEY=55e63a8c30644642b07f671996903252"
ItalyKEY = "/Genrestrtfastfood?KEY=308a1836ded941e69da26b59698c3c68"
CafeKEY = "/Genrestrtcate?KEY=46c5a83322734a8b83ae785069ca6619"
FamousKEY = "/PlaceThatDoATasteyFoodSt?KEY=de547a5cf35444bb9e49043ce00f4115"


class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x750+450-50') #윈도우 고정
        self.window.configure(background=bgColor) #RosyBrown1 thistle powder blue

        self.font = font.Font(self.window, size=20, weight='bold', family="메이플스토리")
        self.font2 = font.Font(self.window, size=18, weight='bold', family="메이플스토리")
        self.font3 = font.Font(self.window, size=16, weight='bold', family="메이플스토리")

        self.initLogo()
        self.initMail()
        self.initSearchListBox()
        self.initInputLabel()
        self.initSearchButton()
        self.setupButton()
        self.initEateryList()
        self.initInformation()
        self.initGraph()
        self.initMap()

        self.window.mainloop()

    def initLogo(self):
        self.logoImage = PhotoImage(file='resources/image/logo.png')
        logo = Label(self.window, image=self.logoImage, background=bgColor)
        logo.place(x=25,y=5)

    def initMail(self):
        self.mailImage = PhotoImage(file='resources/image/gmail.png')
        self.mailButton = Button(self.window, cursor='heart', image=self.mailImage, command=self.sendMail)
        self.mailButton.place(x=470, y=20)

    def sendMail(self):
        pass

    def initSearchListBox(self):
        global SearchList
        ListScrollbar = Scrollbar(self.window)
        ListScrollbar.pack()
        ListScrollbar.place(x=230, y=130)

        SearchList = Listbox(self.window, font=self.font3, activestyle='dotbox', width=13, height=1, bd=12,
                              cursor='heart', relief='ridge', yscrollcommand=ListScrollbar.set, fg='thistle4')

        for i in range(31):
            SearchList.insert(i, CityList[i])

        SearchList.pack()
        SearchList.place(x=25, y=130)
        ListScrollbar.config(command=SearchList.yview)

    def initInputLabel(self):
        global InputLabel
        InputLabel = Entry(self.window, font=self.font3, width=15, bd=12, relief='ridge', cursor='heart', fg='thistle4')

        InputLabel.pack()
        InputLabel.place(x=263, y=130)

    def initSearchButton(self):
        SearchButton = Button(self.window, font=self.font2, text="검색", cursor='heart', command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=507, y=130)

    def SearchButtonAction(self):
        global CategoryButton, EateryText

        EateryText.configure(state='normal')
        EateryText.delete(0.0, END)

        if CategoryButton == 0: #한식
            Food.URLrequest(KoreaKEY)
        if CategoryButton == 1: #중식
            Food.URLrequest(ChinaKEY)
        if CategoryButton == 2: #일식
            Food.URLrequest(JapanKEY)
        if CategoryButton == 3: #양식
            Food.URLrequest(ItalyKEY)
        if CategoryButton == 4: #카페
            Food.URLrequest(CafeKEY)
        if CategoryButton == 5: #맛집
            pass

    def setupButton(self):
        self.Korea = Button(self.window, cursor='heart', text="한식", font=self.font, command=self.pressedKorea)
        self.Korea.place(x=25, y=200)
        self.China = Button(self.window, cursor='heart', text="중식", font=self.font, command=self.pressedChina)
        self.China.place(x=120, y=200)
        self.Japan = Button(self.window, cursor='heart', text="일식", font=self.font, command=self.pressedJapan)
        self.Japan.place(x=215, y=200)
        self.Italy = Button(self.window, cursor='heart', text="양식", font=self.font, command=self.pressedItaly)
        self.Italy.place(x=310, y=200)
        self.Cafe = Button(self.window, cursor='heart', text="카페", font=self.font, command=self.pressedCafe)
        self.Cafe.place(x=405, y=200)
        self.Famous = Button(self.window, cursor='heart', text="맛집", font=self.font, command=self.pressedFamous)
        self.Famous.place(x=500, y=200)

        self.Korea['state'] = 'active'
        self.China['state'] = 'active'
        self.Japan['state'] = 'active'
        self.Italy['state'] = 'active'
        self.Cafe['state'] = 'active'
        self.Famous['state'] = 'active'

    def pressedKorea(self):
        self.setupButton()
        self.Korea['state'] = 'disabled'
        self.Korea['bg'] = 'RosyBrown1'
        self.KoreaImage = PhotoImage(file='resources/image/Korea.png')
        korea = Label(self.window, image=self.KoreaImage, background=bgColor)
        korea.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 0

    def pressedChina(self):
        self.setupButton()
        self.China['state'] = 'disabled'
        self.China['bg'] = 'RosyBrown1'
        self.ChinaImage = PhotoImage(file='resources/image/China.png')
        china = Label(self.window, image=self.ChinaImage, background=bgColor)
        china.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 1

    def pressedJapan(self):
        self.setupButton()
        self.Japan['state'] = 'disabled'
        self.Japan['bg'] = 'RosyBrown1'
        self.JapanImage = PhotoImage(file='resources/image/Japan.png')
        japan = Label(self.window, image=self.JapanImage, background=bgColor)
        japan.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 2

    def pressedItaly(self):
        self.setupButton()
        self.Italy['state'] = 'disabled'
        self.Italy['bg'] = 'RosyBrown1'
        self.ItalyImage = PhotoImage(file='resources/image/Italy.png')
        italy = Label(self.window, image=self.ItalyImage, background=bgColor)
        italy.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 3

    def pressedCafe(self):
        self.setupButton()
        self.Cafe['state'] = 'disabled'
        self.Cafe['bg'] = 'RosyBrown1'
        self.CafeImage = PhotoImage(file='resources/image/Cafe.png')
        cafe = Label(self.window, image=self.CafeImage, background=bgColor)
        cafe.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 4

    def pressedFamous(self):
        self.setupButton()
        self.Famous['state'] = 'disabled'
        self.Famous['bg'] = 'RosyBrown1'
        self.FamousImage = PhotoImage(file='resources/image/Famous.png')
        famous = Label(self.window, image=self.FamousImage, background=bgColor)
        famous.place(x=15, y=590)

        global CategoryButton
        CategoryButton = 5

    def initEateryList(self):
        Escrollbar = Scrollbar(self.window)
        Escrollbar.pack()
        Escrollbar.place(x=277, y=270)

        global EateryText
        EateryText = Text(self.window, width=32, height=22, borderwidth=12, relief='ridge',
                          cursor='heart', yscrollcommand=Escrollbar.set)

        EateryText.pack()
        EateryText.place(x=25, y=270)

        Escrollbar.config(command=EateryText.yview)
        Escrollbar.pack()
        Escrollbar.place(x=277, y=270)

        EateryText.configure(state='disabled')

    def clearEateryData(self):
        global EateryText
        EateryText.delete(0, EateryText.size())

    def initInformation(self):
        Iscrollbar = Scrollbar(self.window)
        Iscrollbar.pack()
        Iscrollbar.place(x=563, y=270)

        global InfoText
        InfoText = Text(self.window, width=32, height=22, borderwidth=12, relief='ridge',
                        cursor='heart', yscrollcommand=Iscrollbar.set)
        InfoText.pack()
        InfoText.place(x=310, y=270)

        Iscrollbar.config(command=InfoText.yview)
        Iscrollbar.pack()
        Iscrollbar.place(x=563, y=270)

        InfoText.configure(state='disabled')

    def clearInfoData(self):
        global InfoText
        InfoText.delete('1.0', END)

    def initGraph(self):
        self.graphCanvas = Canvas(self.window, cursor='heart', width=300, height=90, bg='white')
        self.graphCanvas.pack()
        self.graphCanvas.place(x=165, y=630)
        pass

    def initMap(self):
        self.mapImage = PhotoImage(file='resources/image/map.png')
        self.mapButton = Button(self.window, cursor='heart', image=self.mapImage, command=self.openMap)
        self.mapButton.place(x=480, y=630)

    def openMap(self):
        # 인터넷 창 뜨게 하기
        pass


EatToday()