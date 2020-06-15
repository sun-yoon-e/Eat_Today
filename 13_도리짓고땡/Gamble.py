from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random


class Gamble:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=13, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        self.cardDeck = [i for i in range(40)]

        self.count = 0
        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")
        self.dealer = Player("dealer")

        self.betMoney1 = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.playerMoney = 1000

        self.LcardsPlayer1 = []
        self.LcardsPlayer2 = []
        self.LcardsPlayer3 = []
        self.LcardsDealer = []

        self.Player1Month = []
        self.Player2Month = []
        self.Player3Month = []
        self.DealerMonth = []

        self.Player1Value = []
        self.Player2Value = []
        self.Player3Value = []
        self.DealerValue = []

        self.deckN = 0
        self.window.mainloop()

    def setupButton(self):
        self.p1_5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressed15)
        self.p1_5.place(x=50, y=550)
        self.p1_1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressed11)
        self.p1_1.place(x=130, y=550)

        self.p2_5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressed25)
        self.p2_5.place(x=240, y=550)
        self.p2_1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressed21)
        self.p2_1.place(x=320, y=550)

        self.p3_5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressed35)
        self.p3_5.place(x=430, y=550)
        self.p3_1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressed31)
        self.p3_1.place(x=510, y=550)

        self.Deal = Button(self.window, text="Deal", width=5, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=620, y=550)
        self.Again = Button(self.window, text="Again", width=5, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=550)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney1 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney1.place(x=80, y=500)
        self.LbetMoney2 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney2.place(x=270, y=500)
        self.LbetMoney3 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney3.place(x=460, y=500)
        self.LplayerMoney = Label(text="1000만원", width=15, height=1, font=self.fontstyle, bg="green", fg="pink")
        self.LplayerMoney.place(x=560, y=500)

        # 족보
        self.LplayerStatus1 = Label(text="가나다(1 1 2) 3땡", width=20, height=1, font=self.fontstyle3, bg="green",
                                    fg="cyan")
        self.LplayerStatus1.place(x=50, y=280)
        self.LplayerStatus2 = Label(text="가나다(1 1 2) 3땡", width=20, height=1, font=self.fontstyle3, bg="green",
                                    fg="cyan")
        self.LplayerStatus2.place(x=240, y=280)
        self.LplayerStatus3 = Label(text="가나다(1 1 2) 3땡", width=20, height=1, font=self.fontstyle3, bg="green",
                                    fg="cyan")
        self.LplayerStatus3.place(x=430, y=280)
        self.LdealerStatus = Label(text="가나다(1 1 2) 3땡", width=20, height=1, font=self.fontstyle3, bg="green",
                                   fg="cyan")
        self.LdealerStatus.place(x=250, y=10)

        # 월

        # 승 / 패
        self.Lstatus1 = Label(text="승", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus1.place(x=90, y=230)
        self.Lstatus2 = Label(text="패", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus2.place(x=280, y=230)
        self.Lstatus3 = Label(text="승", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus3.place(x=470, y=230)

    def pressed15(self):
        self.betMoney1 += 5
        if self.betMoney1 <= self.playerMoney:
            self.LbetMoney1.configure(text=str(self.betMoney1) + "만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney1 -= 5

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressed25(self):
        self.betMoney2 += 5
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text=str(self.betMoney2) + "만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 5

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressed35(self):
        self.betMoney3 += 5
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text=str(self.betMoney3) + "만")
            self.playerMoney -= 5
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 5

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressed11(self):
        self.betMoney1 += 1
        if self.betMoney1 <= self.playerMoney:
            self.LbetMoney1.configure(text=str(self.betMoney1) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney1 -= 1

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressed21(self):
        self.betMoney2 += 1
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text=str(self.betMoney2) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 1

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressed31(self):
        self.betMoney3 += 1
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text=str(self.betMoney3) + "만")
            self.playerMoney -= 1
            self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 1

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def deal(self):
        self.player1.reset()
        self.player2.reset()
        self.player3.reset()
        self.dealer.reset()  # 카드 덱 40 장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        # 카드 나눠주기 딜러 1장, 플레이어 각각 1장 - 총 3장
        self.hitDealer(1)
        self.hitPlayer1(1)
        self.hitPlayer2(1)
        self.hitPlayer3(1)

    def hitDealer(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.dealer.addCard(newCard)
            p = PhotoImage(file="GodoriCards/cardback.gif")
            self.LcardsDealer.append(Label(self.window, image=p))

            self.LcardsDealer[self.dealer.inHand() - 1].image = p
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + (i + self.count) * 30, y=110)

            # PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer1(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player1.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer1.append(Label(self.window, image=p))

            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + (i + self.count) * 30, y=380)

            # PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer2(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player2.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer2.append(Label(self.window, image=p))

            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=250 + (i + self.count) * 30, y=380)

            # PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer3(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player3.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer3.append(Label(self.window, image=p))

            self.LcardsPlayer3[self.player3.inHand() - 1].image = p
            self.LcardsPlayer3[self.player3.inHand() - 1].place(x=450 + (i + self.count) * 30, y=380)

            # PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
    def printPts(self):
        self.Player1Month = self.player1.returnMonth()
        self.Player2Month = self.player2.returnMonth()
        self.Player3Month = self.player3.returnMonth()
        self.DealerMonth = self.dealer.returnMonth()

        for i in range(len(self.Player1Month)):
            self.LplayerPts1 = Label(text=self.Player1Month[i], width=2, height=1, font=self.fontstyle2, bg="green",fg="white")
            self.LplayerPts1.place(x=80 + i * 30, y=310)
        for i in range(len(self.Player2Month)):
            self.LplayerPts2 = Label(text=self.Player2Month[i], width=2, height=1, font=self.fontstyle2, bg="green",fg="white")
            self.LplayerPts2.place(x=280 + i * 30, y=310)
        for i in range(len(self.Player3Month)):
            self.LplayerPts3 = Label(text=self.Player3Month[i], width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LplayerPts3.place(x=470 + i * 30, y=310)
        for i in range(len(self.DealerMonth)):
            self.LdealerPts = Label(text=self.DealerMonth[i], width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LdealerPts.place(x=280 + i * 30, y=40)

    def pressedDeal(self):
        if self.count == 0:
            self.deal()
            self.count += 1
            self.printPts()

        elif self.count == 1:
            self.hitDealer(3)
            self.hitPlayer1(3)
            self.hitPlayer2(3)
            self.hitPlayer3(3)
            self.count += 3
            self.printPts()

        elif self.count == 4:
            self.hitDealer(1)
            self.hitPlayer1(1)
            self.hitPlayer2(1)
            self.hitPlayer3(1)
            self.printPts()
            self.checkWinner()

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

    def pressedAgain(self):
        self.p1_5['state'] = 'active'
        self.p1_5['bg'] = 'white'
        self.p1_1['state'] = 'active'
        self.p1_1['bg'] = 'white'

        self.p2_5['state'] = 'active'
        self.p2_5['bg'] = 'white'
        self.p2_1['state'] = 'active'
        self.p2_1['bg'] = 'white'

        self.p3_5['state'] = 'active'
        self.p3_5['bg'] = 'white'
        self.p3_1['state'] = 'active'
        self.p3_1['bg'] = 'white'

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        for item in self.LcardsDealer:
            item.image = None
            item.destroy()

        for item in self.LcardsPlayer1:
            item.image = None
            item.destroy()

        for item in self.LcardsPlayer2:
            item.image = None
            item.destroy()

        for item in self.LcardsPlayer3:
            item.image = None
            item.destroy()

        # 카드 초기화
        self.LcardsPlayer1.clear()
        self.LcardsPlayer2.clear()
        self.LcardsPlayer3.clear()
        self.LcardsDealer.clear()
        self.deckN = 0
        self.count = 0

        # self.LdealerStatus.configure(text="")
        # self.LplayerStatus.configure(text="")
        # self.Lstatus.configure(text="")

        self.betMoney = 0
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
        self.LbetMoney1.configure(text=str(self.betMoney) + "만")
        self.LbetMoney2.configure(text=str(self.betMoney) + "만")
        self.LbetMoney3.configure(text=str(self.betMoney) + "만")

    def make10(self):
        pass


    def checkWinner(self):
        for i in range(5):
            p = PhotoImage(file="GodoriCards/" + self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        # self.LdealerPts1.configure(fg='thistle') -> 메이드 만든 카드 숫자는 색 변경 해주기

        self.betMoney1 = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
        self.LbetMoney1.configure(text=str(self.betMoney1) + "만")
        self.LbetMoney2.configure(text=str(self.betMoney2) + "만")
        self.LbetMoney3.configure(text=str(self.betMoney3) + "만")

        self.p1_5['state'] = 'disabled'
        self.p1_5['bg'] = 'gray'
        self.p1_1['state'] = 'disabled'
        self.p1_1['bg'] = 'gray'

        self.p2_5['state'] = 'disabled'
        self.p2_5['bg'] = 'gray'
        self.p2_1['state'] = 'disabled'
        self.p2_1['bg'] = 'gray'

        self.p3_5['state'] = 'disabled'
        self.p3_5['bg'] = 'gray'
        self.p3_1['state'] = 'disabled'
        self.p3_1['bg'] = 'gray'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


Gamble()