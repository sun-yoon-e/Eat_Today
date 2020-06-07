from tkinter import *
from tkinter import font
import Food

CityList = ['가평군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시',
            '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시',
            '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시',
            '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시']

bgColor = 'lemon chiffon'
CategoryButton = 0
CategoryNum = 0
GraphData = [0 for i in range(6)]

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x750+450-50')  # 윈도우 고정
        self.window.configure(background=bgColor)  # RosyBrown1 thistle powder blue

        self.font = font.Font(self.window, size=20, weight='bold', family="메이플스토리")
        self.font2 = font.Font(self.window, size=18, weight='bold', family="메이플스토리")
        self.font3 = font.Font(self.window, size=16, weight='bold', family="메이플스토리")

        self.initLogo()
        self.initMail()
        self.initCityListBox()
        self.initInputLabel()
        self.initSearchButton()
        self.setupButton()
        self.initEateryList()
        self.initInformation()
        self.initGraph()
        self.initMap()

        for CategoryNum in range(6):
            Food.URLbuilder(CategoryNum)

        self.window.mainloop()

    def initLogo(self):
        self.logoImage = PhotoImage(file='resources/image/logo.png')
        logo = Label(self.window, image=self.logoImage, background=bgColor)
        logo.place(x=25, y=5)

    def initMail(self):
        self.mailImage = PhotoImage(file='resources/image/gmail.png')
        self.mailButton = Button(self.window, cursor='heart', image=self.mailImage, command=self.sendMail)
        self.mailButton.place(x=470, y=20)

    def sendMail(self):
        pass

    def initCityListBox(self):    #시(군) 선택창
        global Search
        ListScrollbar = Scrollbar(self.window)
        ListScrollbar.place(x=230, y=130)

        Search = Listbox(self.window, font=self.font3, activestyle='dotbox', width=13, height=1, bd=12,
                             cursor='heart', relief='ridge', yscrollcommand=ListScrollbar.set, fg='thistle4')

        for i in range(31):
            Search.insert(i, CityList[i])

        Search.pack()
        Search.place(x=25, y=130)
        ListScrollbar.config(command=Search.yview)

    def initInputLabel(self):   #검색 창
        global InputLabel
        InputLabel = Entry(self.window, font=self.font3, width=15, bd=12, relief='ridge', cursor='heart', fg='thistle4')

        InputLabel.pack()
        InputLabel.place(x=263, y=130)

    def initSearchButton(self):
        SearchButton = Button(self.window, font=self.font2, text="검색", cursor='heart', command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=507, y=130)

    def SearchButtonAction(self): #검색 버튼
        global CategoryButton, InfoText, InputLabel

        InfoText.configure(state='normal')
        InfoText.delete(1.0, END)
        Store = InputLabel.get()

        if CategoryButton == 0:  # 한식
            self.InsertInformation(0, Store)
        if CategoryButton == 1:  # 중식
            self.InsertInformation(1, Store)
        if CategoryButton == 2:  # 일식
            self.InsertInformation(2, Store)
        if CategoryButton == 3:  # 양식
            self.InsertInformation(3, Store)
        if CategoryButton == 4:  # 카페
            self.InsertInformation(4, Store)
        if CategoryButton == 5:  # 맛집
            self.InsertInformation(5, Store)

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

        global CategoryButton, EateryText, SearchIndex, Search

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 0
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(0, i)
        self.drawGraph()

    def pressedChina(self):
        self.setupButton()
        self.China['state'] = 'disabled'
        self.China['bg'] = 'RosyBrown1'
        self.ChinaImage = PhotoImage(file='resources/image/China.png')
        china = Label(self.window, image=self.ChinaImage, background=bgColor)
        china.place(x=15, y=590)

        global CategoryButton, EateryText, SearchIndex, Search

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 1
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(1, i)

    def pressedJapan(self):
        self.setupButton()
        self.Japan['state'] = 'disabled'
        self.Japan['bg'] = 'RosyBrown1'
        self.JapanImage = PhotoImage(file='resources/image/Japan.png')
        japan = Label(self.window, image=self.JapanImage, background=bgColor)
        japan.place(x=15, y=590)

        global CategoryButton, EateryText, SearchIndex, Search

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 2
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(2, i)

    def pressedItaly(self):
        self.setupButton()
        self.Italy['state'] = 'disabled'
        self.Italy['bg'] = 'RosyBrown1'
        self.ItalyImage = PhotoImage(file='resources/image/Italy.png')
        italy = Label(self.window, image=self.ItalyImage, background=bgColor)
        italy.place(x=15, y=590)

        global CategoryButton, EateryText, SerachIdex, SerachList

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 3
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(3, i)

    def pressedCafe(self):
        self.setupButton()
        self.Cafe['state'] = 'disabled'
        self.Cafe['bg'] = 'RosyBrown1'
        self.CafeImage = PhotoImage(file='resources/image/Cafe.png')
        cafe = Label(self.window, image=self.CafeImage, background=bgColor)
        cafe.place(x=15, y=590)

        global CategoryButton, EateryText, SearchIndex, Search

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 4
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(4, i)

    def pressedFamous(self):
        self.setupButton()
        self.Famous['state'] = 'disabled'
        self.Famous['bg'] = 'RosyBrown1'
        self.FamousImage = PhotoImage(file='resources/image/Famous.png')
        famous = Label(self.window, image=self.FamousImage, background=bgColor)
        famous.place(x=15, y=590)

        global CategoryButton, EateryText, SearchIndex, Search

        EateryText.configure(state='normal')
        EateryText.delete(1.0, END)
        SearchIndex = Search.curselection()[0]

        CategoryButton = 5
        for i in range(31):
            if SearchIndex == i:
                self.InsertEatery(5, i)

    def InsertEatery(self, CategoryNum, CityNum):
        global EateryText

        List = Food.getList(CategoryNum)
        count = 1
        maxcount = 0
        for i in range(len(List)):
            if CityList[CityNum] == List[i][0]:
                EateryText.insert(INSERT, "[")
                EateryText.insert(INSERT, count)
                EateryText.insert(INSERT, "] ")
                EateryText.insert(INSERT, List[i][1] + "\n\n")
                count += 1
        if count > maxcount:
            maxcount = count - 1
        GraphData[CategoryNum] = maxcount
        print(GraphData)

    def initEateryList(self):   #검색용 리스트
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
        #    global EateryText
        #    EateryText.delete(0, EateryText.size())
        pass

    def InsertInformation(self, CategoryNum, StoreName):
        global InfoText, Search, CityList

        List = Food.getList(CategoryNum)

        for i in range(len(List)):
            for j in range(len(List[i])):
                if List[i][j] == None:
                    List[i][j] = ""
            if StoreName == List[i][1] and CityList[Search.curselection()[0]] == List[i][0]:
                InfoText.insert(INSERT, "시군명 : " + List[i][0] + "\n\n")
                InfoText.insert(INSERT, "사업장명 : " + List[i][1] + "\n\n")
                InfoText.insert(INSERT, "도로명주소 : " + List[i][2] + "\n\n")
                InfoText.insert(INSERT, "지번주소 : " + List[i][3] + "\n\n")
                InfoText.insert(INSERT, "우편번호 : " + List[i][4] + "\n\n")

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
        #    global InfoText
        #    InfoText.delete('1.0', END)
        pass

    def initGraph(self):
        self.graphCanvas = Canvas(self.window, cursor='heart', width=300, height=90, bg='white')
        self.graphCanvas.pack()
        self.graphCanvas.place(x=165, y=630)

    def drawGraph(self):
        global Search, CityList
        width, height = 300, 90

        Index = Search.curselection()[0]

        List = []
        List.append(Food.getList(0))
        List.append(Food.getList(1))
        List.append(Food.getList(2))
        List.append(Food.getList(3))
        List.append(Food.getList(4))
        List.append(Food.getList(5))

        # counts = [0] * 6
        # for i in range(len(List)):
        #     for j in range(len(List[i])):
        #         if CityList[Index] == List[i][0]:
        #             counts[i] += 1
        # barWidth = (width - 20) / 6
        # maxCount = max(counts)
        # for i in range(len(List)):
        #     self.graphCanvas.create_rectangle(5 + i * barWidth, height - (height - 5) * counts[i] / maxCount,
        #                                       5 + (i + 1) * barWidth, height - 5, tags='graph')
        #     self.graphCanvas.create_text(5 + i * barWidth + 7, height - 2, text=str(i), tags='graph')
        #     self.graphCanvas.create_text(5 + i * barWidth + 7, height - (height - 5) * counts[i] / maxCount - 2,
        #                                  text=str(counts[i]), tags='graph')

    def initMap(self):
        self.mapImage = PhotoImage(file='resources/image/map.png')
        self.mapButton = Button(self.window, cursor='heart', image=self.mapImage, command=self.openMap)
        self.mapButton.place(x=480, y=630)

    def openMap(self):
        # 인터넷 창 뜨게 하기
        pass


EatToday()