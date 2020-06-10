from tkinter import *
from tkinter import font
import folium
import webbrowser
import Food
import Gmail

bgColor = 'lemon chiffon'
CategoryButton = 0
CategoryNum = 0
width, height = 300, 120
barWidth = (width - 20) / 6
MailList = []

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x750+450-50')  # 윈도우 고정
        self.window.configure(background=bgColor)  # misty rose RosyBrown1 thistle powder blue

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
        self.mailButton = Button(self.window, cursor='heart', image=self.mailImage, bg=bgColor, command=self.sendMail)
        self.mailButton.place(x=470, y=20)

    def sendMail(self):
        global MailList
        Gmail.sendMail(MailList)

    def initCityListBox(self):  # 시(군) 선택창
        global Search
        ListScrollbar = Scrollbar(self.window)
        ListScrollbar.place(x=230, y=130)

        Search = Listbox(self.window, font=self.font3, activestyle='dotbox', width=13, height=1, bd=12,
                         cursor='heart', relief='ridge', yscrollcommand=ListScrollbar.set, fg='thistle4')

        for i in range(31):
            Search.insert(i, Food.CityList[i])

        Search.pack()
        Search.place(x=25, y=130)
        ListScrollbar.config(command=Search.yview)

    def initInputLabel(self):  # 검색 창
        global InputLabel
        InputLabel = Entry(self.window, font=self.font3, width=15, bd=12, relief='ridge', cursor='heart', fg='thistle4')

        InputLabel.pack()
        InputLabel.place(x=263, y=130)

    def initSearchButton(self):
        SearchButton = Button(self.window, font=self.font2, bg='lavender blush', text="검색", cursor='heart',
                              command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=507, y=130)

    def SearchButtonAction(self):  # 검색 버튼
        global CategoryButton, InfoText, InputLabel

        InfoText.configure(state='normal')
        # InfoText.delete(0, InfoText.size())
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
        self.Korea['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def pressedChina(self):
        self.setupButton()
        self.China['state'] = 'disabled'
        self.China['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def pressedJapan(self):
        self.setupButton()
        self.Japan['state'] = 'disabled'
        self.Japan['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def pressedItaly(self):
        self.setupButton()
        self.Italy['state'] = 'disabled'
        self.Italy['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def pressedCafe(self):
        self.setupButton()
        self.Cafe['state'] = 'disabled'
        self.Cafe['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def pressedFamous(self):
        self.setupButton()
        self.Famous['state'] = 'disabled'
        self.Famous['bg'] = 'misty rose'
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

        self.initGraph()
        self.drawGraph()

    def InsertEatery(self, CategoryNum, CityNum):
        global EateryText

        List = Food.getList(CategoryNum)
        count = 1
        for i in range(len(List)):
            if Food.CityList[CityNum] == List[i][0]:
                EateryText.insert(INSERT, "[")
                EateryText.insert(INSERT, count)
                EateryText.insert(INSERT, "] ")
                EateryText.insert(INSERT, List[i][1] + "\n\n")
                count += 1

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

    def InsertInformation(self, CategoryNum, StoreName):
        global InfoText, Search, Name, Lat, Long, MailList

        List = Food.getList(CategoryNum)
        MailList.clear()

        for i in range(len(List)):
            for j in range(len(List[i])):
                if List[i][j] == None:
                    List[i][j] = ""
            if StoreName == List[i][1] and Food.CityList[Search.curselection()[0]] == List[i][0]:
                InfoText.insert(INSERT, "사업장명 : " + List[i][1] + "\n\n")
                MailList.append("사업장명 : " + List[i][1])

                if CategoryNum == 5:
                    InfoText.insert(INSERT, "대표메뉴 : " + List[i][7] + "\n\n")
                    InfoText.insert(INSERT, "전화번호 : " + List[i][8] + "\n\n")

                    MailList.append("대표메뉴 : " + List[i][7])
                    MailList.append("전화번호 : " + List[i][8])

                else:
                    InfoText.insert(INSERT, "허가일자 : " + List[i][7] + "\n\n")
                    MailList.append("허가일자 : " + List[i][7])

                InfoText.insert(INSERT, "도로명주소 : " + List[i][2] + "\n\n")
                InfoText.insert(INSERT, "지번주소 : " + List[i][3] + "\n\n")
                InfoText.insert(INSERT, "우편번호 : " + List[i][4] + "\n\n")

                MailList.append("도로명주소 : " + List[i][2])
                MailList.append("지번주소 : " + List[i][3])
                MailList.append("우편번호 : " + List[i][4])

                Name = List[i][1]
                Lat = List[i][5]
                Long = List[i][6]

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
        self.graphCanvas = Canvas(self.window, cursor='heart', width=300, height=120, bg='floral white')
        self.graphCanvas.pack()
        self.graphCanvas.place(x=165, y=610)

        self.graphCanvas.create_text(25 + (1 / 2) + 0 * barWidth + 10, height - 5, text="한식", tags='graph')
        self.graphCanvas.create_text(25 + (1 / 2) + 1 * barWidth + 10, height - 5, text="중식", tags='graph')
        self.graphCanvas.create_text(25 + (1 / 2) + 2 * barWidth + 10, height - 5, text="일식", tags='graph')
        self.graphCanvas.create_text(25 + (1 / 2) + 3 * barWidth + 10, height - 5, text="양식", tags='graph')
        self.graphCanvas.create_text(25 + (1 / 2) + 4 * barWidth + 10, height - 5, text="카페", tags='graph')
        self.graphCanvas.create_text(25 + (1 / 2) + 5 * barWidth + 10, height - 5, text="맛집", tags='graph')

    def drawGraph(self):
        global Search, CityList

        Index = Search.curselection()[0]

        AllList = []  # 해당 도시 리스트
        counts = [] * 6
        for i in range(6):
            AllList.append([])
            for j in range(len(Food.getList(i))):
                if Food.CityList[Index] == Food.getList(i)[j][0]:
                    AllList[i].append(Food.getList(i)[j][1])

        for i in range(len(AllList)):
            counts.append(len(AllList[i]))

        maxCount = max(counts)
        for i in range(6):
            self.graphCanvas.create_rectangle(10+i*barWidth, height-(height-10)*counts[i]/maxCount,
                                              10+(i+1)*barWidth, height-10, tags='graph')
            self.graphCanvas.create_text(25+i*barWidth+10, height-110, text=counts[i], tags='graph')

    def initMap(self):
        self.mapImage = PhotoImage(file='resources/image/map.png')
        self.mapButton = Button(self.window, cursor='heart', image=self.mapImage, bg=bgColor, command=self.openMap)
        self.mapButton.place(x=480, y=630)

    def openMap(self):
        global Name, Lat, Long
        map = folium.Map(location=[Lat, Long], zoom_start=15)  # 위도, 경도 지정
        icon = folium.Icon(icon='glyphicon glyphicon-cutlery', color='pink')
        folium.Marker([Lat, Long], popup=Name, icon=icon).add_to(map)  # 마커 지정
        map.save('Eat_Today_Map.html')  # html 파일로 저장
        webbrowser.open_new('Eat_Today_Map.html')


EatToday()