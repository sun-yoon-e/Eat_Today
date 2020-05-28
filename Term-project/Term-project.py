from tkinter import *
from tkinter import font

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x600')
        self.window.configure(bg='lemon chiffon') #RosyBrown1 thistle powder blue

        self.font = font.Font(self.window, size=20, weight='bold', family='resources/font/BMJU_ttf_0.ttf')
        self.font2 = font.Font(self.window, size=18, weight='bold', family='resources/font/BMJU_ttf_0.ttf')
        self.font3 = font.Font(self.window, size=16, weight='bold', family='resources/font/BMJU_ttf_0.ttf')

        #self.Logo #로고이미지
        self.initMail()
        self.initSearchListBox()
        self.initInputLabel()
        self.initSearchButton()
        self.setupButton()
        self.initEateryList()
        self.initInformation()
        self.FoodImage()
        self.initGraph()
        self.initMap()

        self.window.mainloop()

    def initMail(self):
        self.mailImage = PhotoImage(file='resources/image/gmail.png')
        self.mailButton = Button(self.window, image=self.mailImage, command=self.sendMail)
        self.mailButton.place(x=450, y=30)

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
        InputLabel = Entry(self.window, font=self.font3, width=18, bd=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=263, y=130)

    def initSearchButton(self):
        SearchButton = Button(self.window, font=self.font2, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=507, y=130)

    def SearchButtonAction(self):
        pass

    def setupButton(self):
        self.Korea = Button(self.window, text="한식", font=self.font, command=self.pressedKr)
        self.Korea.place(x=25, y=200)
        self.China = Button(self.window, text="중식", font=self.font, command=self.pressedCn)
        self.China.place(x=120, y=200)
        self.Japan = Button(self.window, text="일식", font=self.font, command=self.pressedJp)
        self.Japan.place(x=215, y=200)
        self.Italy = Button(self.window, text="양식", font=self.font, command=self.pressedIt)
        self.Italy.place(x=310, y=200)
        self.Cafe = Button(self.window, text="카페", font=self.font, command=self.pressedCf)
        self.Cafe.place(x=405, y=200)
        self.Famous = Button(self.window, text="맛집", font=self.font, command=self.pressedFm)
        self.Famous.place(x=500, y=200)

    def pressedKr(self):
        pass
    def pressedCn(self):
        pass
    def pressedJp(self):
        pass
    def pressedIt(self):
        pass
    def pressedCf(self):
        pass
    def pressedFm(self):
        pass

    def initEateryList(self):
        pass

    def initInformation(self):
        pass

    def FoodImage(self):
        pass

    def initGraph(self):
        pass

    def initMap(self):
        self.mapImage = PhotoImage(file='resources/image/map.png')
        self.mapButton = Button(self.window, image=self.mapImage, command=self.openMap)
        self.mapButton.place(x=480, y=450)

    def openMap(self):
        pass

    # x y 위치는 예쁘게 조정이 어렵다... 모르겠어 !!!!!!!!!!!!!!!

EatToday()