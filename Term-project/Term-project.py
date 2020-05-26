from tkinter import *
from tkinter import font

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x800')
        self.window.configure(background='lemon chiffon') #RosyBrown1 thistle powder blue

        self.fontstyle = font.Font(self.window, size=20, weight='bold', family='resources/font/BMJU_ttf_0.ttf')
        #self.Logo

        self.initMail()
        self.setupButton()


        self.window.mainloop()

    def initMail(self):
        self.mailImage = PhotoImage(file='resources/image/gmail.png')
        self.mailButton = Button(self.window, image=self.mailImage, command=self.sendMail)

    def sendMail(self):
        pass

    def setupButton(self):
        self.Korea = Button(self.window, text="한식", font=self.fontstyle, command=self.pressedKr)
        self.Korea.place(x=25, y=200)
        self.China = Button(self.window, text="중식", font=self.fontstyle, command=self.pressedCn)
        self.China.place(x=120, y=200)
        self.Japan = Button(self.window, text="일식", font=self.fontstyle, command=self.pressedJp)
        self.Japan.place(x=215, y=200)
        self.Italy = Button(self.window, text="양식", font=self.fontstyle, command=self.pressedIt)
        self.Italy.place(x=310, y=200)
        self.Cafe = Button(self.window, text="카페", font=self.fontstyle, command=self.pressedCf)
        self.Cafe.place(x=405, y=200)
        self.Famous = Button(self.window, text="맛집", font=self.fontstyle, command=self.pressedFm)
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


EatToday()