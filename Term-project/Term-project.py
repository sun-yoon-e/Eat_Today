from tkinter import *
from tkinter import font

bgColor = 'lemon chiffon'

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x750+450-50') #윈도우 고정
        self.window.configure(background=bgColor) #RosyBrown1 thistle powder blue

        self.font = font.Font(self.window, size=20, weight='bold', family='resources/font/BMJU_ttf_0.ttf')
        self.font2 = font.Font(self.window, size=18, weight='bold', family='resources/font/BMJU_ttf_0.ttf')
        self.font3 = font.Font(self.window, size=16, weight='bold', family='resources/font/BMJU_ttf_0.ttf')

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
        self.mailButton = Button(self.window, cursor='heart', image=self.mailImage, background=bgColor, command=self.sendMail)
        self.mailButton.place(x=470, y=20)

    def sendMail(self):
        pass

    def initSearchListBox(self):
        global SearchList
        ListScrollbar = Scrollbar(self.window)
        ListScrollbar.pack()
        ListScrollbar.place(x=230, y=130)

        SearchList = Listbox(self.window, font=self.font3, activestyle='dotbox', width=15, height=1, bd=12,
                              cursor='heart', relief='ridge', yscrollcommand=ListScrollbar.set, fg='thistle4')

        SearchList.insert(1, "가평군")
        SearchList.insert(2, "고양시")
        SearchList.insert(3, "과천시")
        SearchList.insert(4, "광명시")
        SearchList.insert(5, "광주시")
        SearchList.insert(6, "구리시")
        SearchList.insert(7, "군포시")
        SearchList.insert(8, "김포시")
        SearchList.insert(9, "남양주시")
        SearchList.insert(10, "동두천시")
        SearchList.insert(11, "부천시")
        SearchList.insert(12, "성남시")
        SearchList.insert(13, "수원시")
        SearchList.insert(14, "시흥시")
        SearchList.insert(15, "안산시")
        SearchList.insert(16, "안성시")
        SearchList.insert(17, "안양시")
        SearchList.insert(18, "양주시")
        SearchList.insert(19, "양평군")
        SearchList.insert(20, "여주시")
        SearchList.insert(21, "연천군")
        SearchList.insert(22, "오산시")
        SearchList.insert(23, "용인시")
        SearchList.insert(24, "의왕시")
        SearchList.insert(25, "의정부시")
        SearchList.insert(26, "이천시")
        SearchList.insert(27, "파주시")
        SearchList.insert(28, "평택시")
        SearchList.insert(29, "포천시")
        SearchList.insert(30, "하남시")
        SearchList.insert(31, "화성시")

        SearchList.pack()
        SearchList.place(x=25, y=130)
        ListScrollbar.config(command=SearchList.yview)

    def initInputLabel(self):
        global InputLabel
        InputLabel = Entry(self.window, font=self.font3, width=18, bd=12, relief='ridge', cursor='heart', fg='thistle4')

        InputLabel.pack()
        InputLabel.place(x=263, y=130)

    def initSearchButton(self):
        SearchButton = Button(self.window, font=self.font2, text="검색", cursor='heart', command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=507, y=130)

    def SearchButtonAction(self):
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

    def pressedChina(self):
        self.setupButton()
        self.China['state'] = 'disabled'
        self.China['bg'] = 'RosyBrown1'
        self.ChinaImage = PhotoImage(file='resources/image/China.png')
        china = Label(self.window, image=self.ChinaImage, background=bgColor)
        china.place(x=15, y=590)

    def pressedJapan(self):
        self.setupButton()
        self.Japan['state'] = 'disabled'
        self.Japan['bg'] = 'RosyBrown1'
        self.JapanImage = PhotoImage(file='resources/image/Japan.png')
        japan = Label(self.window, image=self.JapanImage, background=bgColor)
        japan.place(x=15, y=590)

    def pressedItaly(self):
        self.setupButton()
        self.Italy['state'] = 'disabled'
        self.Italy['bg'] = 'RosyBrown1'
        self.ItalyImage = PhotoImage(file='resources/image/Italy.png')
        italy = Label(self.window, image=self.ItalyImage, background=bgColor)
        italy.place(x=15, y=590)

    def pressedCafe(self):
        self.setupButton()
        self.Cafe['state'] = 'disabled'
        self.Cafe['bg'] = 'RosyBrown1'
        self.CafeImage = PhotoImage(file='resources/image/Cafe.png')
        cafe = Label(self.window, image=self.CafeImage, background=bgColor)
        cafe.place(x=15, y=590)

    def pressedFamous(self):
        self.setupButton()
        self.Famous['state'] = 'disabled'
        self.Famous['bg'] = 'RosyBrown1'
        self.FamousImage = PhotoImage(file='resources/image/Famous.png')
        famous = Label(self.window, image=self.FamousImage, background=bgColor)
        famous.place(x=15, y=590)

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

    # 여기 위랑 밑에 스크롤 먼가 이상함 아직 내용이 없어서 그런가 왜 뭔가 다르지 !!!
    # 암튼 UI 끝~~~

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

    def initGraph(self):
        self.graphCanvas = Canvas(self.window, cursor='heart', width=300, height=90, bg='white')
        self.graphCanvas.pack()
        self.graphCanvas.place(x=165, y=630)
        pass

    def initMap(self):
        self.mapImage = PhotoImage(file='resources/image/map.png')
        self.mapButton = Button(self.window, cursor='heart', image=self.mapImage, background=bgColor, command=self.openMap)
        self.mapButton.place(x=480, y=630)

    def openMap(self):
        # 인터넷 창 뜨게 하기
        pass

    # x y 위치는 예쁘게 조정이 어렵다... 모르겠어 !!!!!!!!!!!!!!!

EatToday()