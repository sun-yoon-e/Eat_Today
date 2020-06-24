from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random
import itertools


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

        self.PlayerMonth1 = []
        self.PlayerMonth2 = []
        self.PlayerMonth3 = []
        self.DealerMonth = []

        self.PlayerValue1 = []
        self.PlayerValue2 = []
        self.PlayerValue3 = []
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
        # 돈
        self.LbetMoney1 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney1.place(x=80, y=500)
        self.LbetMoney2 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney2.place(x=270, y=500)
        self.LbetMoney3 = Label(text="0만", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney3.place(x=460, y=500)
        self.LplayerMoney = Label(text="1000만원", width=15, height=1, font=self.fontstyle, bg="green", fg="pink")
        self.LplayerMoney.place(x=560, y=500)

        # 족보
        self.LplayerStatus1 = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LplayerStatus1.place(x=50, y=280)
        self.LplayerStatus2 = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LplayerStatus2.place(x=240, y=280)
        self.LplayerStatus3 = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LplayerStatus3.place(x=430, y=280)
        self.LdealerStatus = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LdealerStatus.place(x=250, y=10)

        # 승 / 패
        self.Lstatus1 = Label(text="", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus1.place(x=90, y=230)
        self.Lstatus2 = Label(text="", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus2.place(x=280, y=230)
        self.Lstatus3 = Label(text="", width=3, height=1, font=self.fontstyle, bg="green", fg="red")
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
            self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + (i + self.count) * 30, y=90)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer1(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player1.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer1.append(Label(self.window, image=p))

            # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LcardsPlayer1[self.player1.inHand() - 1].image = p
            self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + (i + self.count) * 30, y=350)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer2(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player2.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer2.append(Label(self.window, image=p))

            # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LcardsPlayer2[self.player2.inHand() - 1].image = p
            self.LcardsPlayer2[self.player2.inHand() - 1].place(x=250 + (i + self.count) * 30, y=350)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer3(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.player3.addCard(newCard)
            p = PhotoImage(file="GodoriCards/" + newCard.filename())
            self.LcardsPlayer3.append(Label(self.window, image=p))

            # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LcardsPlayer3[self.player3.inHand() - 1].image = p
            self.LcardsPlayer3[self.player3.inHand() - 1].place(x=450 + (i + self.count) * 30, y=350)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def printMonth(self):
        self.PlayerMonth1 = self.player1.returnMonth()
        self.PlayerMonth2 = self.player2.returnMonth()
        self.PlayerMonth3 = self.player3.returnMonth()

        for i in range(len(self.PlayerMonth1)):
            self.LplayerPts1 = Label(text=self.PlayerMonth1[i], width=2, height=1, font=self.fontstyle2, bg="green",
                                     fg="white")
            self.LplayerPts1.place(x=80 + i * 30, y=310)

        for i in range(len(self.PlayerMonth2)):
            self.LplayerPts2 = Label(text=self.PlayerMonth2[i], width=2, height=1, font=self.fontstyle2, bg="green",
                                     fg="white")
            self.LplayerPts2.place(x=280 + i * 30, y=310)

        for i in range(len(self.PlayerMonth3)):
            self.LplayerPts3 = Label(text=self.PlayerMonth3[i], width=2, height=1, font=self.fontstyle2, bg="green",
                                     fg="white")
            self.LplayerPts3.place(x=470 + i * 30, y=310)

    def pressedDeal(self):
        if self.count == 0:
            self.deal()
            self.count += 1
            self.printMonth()

        elif self.count == 1:
            self.hitDealer(3)
            self.hitPlayer1(3)
            self.hitPlayer2(3)
            self.hitPlayer3(3)
            self.count += 3
            self.printMonth()

        elif self.count == 4:
            self.hitDealer(1)
            self.hitPlayer1(1)
            self.hitPlayer2(1)
            self.hitPlayer3(1)
            self.printMonth()
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

        self.LdealerStatus.configure(text="")
        self.LplayerStatus1.configure(text="")
        self.LplayerStatus2.configure(text="")
        self.LplayerStatus3.configure(text="")
        self.Lstatus1.configure(text="")
        self.Lstatus2.configure(text="")
        self.Lstatus3.configure(text="")

        self.betMoney = 0
        self.LplayerMoney.configure(text=str(self.playerMoney) + "만원")
        self.LbetMoney1.configure(text=str(self.betMoney) + "만")
        self.LbetMoney2.configure(text=str(self.betMoney) + "만")
        self.LbetMoney3.configure(text=str(self.betMoney) + "만")

        for i in range(5):
            self.LplayerPts1 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LplayerPts1.place(x=80 + i * 30, y=310)
            self.LplayerPts2 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LplayerPts2.place(x=280 + i * 30, y=310)
            self.LplayerPts3 = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LplayerPts3.place(x=470 + i * 30, y=310)
            self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LdealerPts.place(x=280 + i * 30, y=40)

    def checkWinner(self):
        for i in range(5):
            p = PhotoImage(file="GodoriCards/" + self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        self.DealerMonth = self.dealer.returnMonth()
        for i in range(len(self.DealerMonth)):
            self.LdealerPts = Label(text="", width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            self.LdealerPts.place(x=280 + i * 30, y=40)

        self.dealer.score = self.made10(self.dealer, self.LcardsDealer, self.DealerMonth, self.LdealerStatus, 280, 40)
        self.player1.score = self.made10(self.player1, self.LcardsPlayer1, self.PlayerMonth1, self.LplayerStatus1, 80,
                                         310)
        self.player2.score = self.made10(self.player2, self.LcardsPlayer2, self.PlayerMonth2, self.LplayerStatus2, 280,
                                         310)
        self.player3.score = self.made10(self.player3, self.LcardsPlayer3, self.PlayerMonth3, self.LplayerStatus3, 470,
                                         310)

        self.Lstatus1.configure(text=self.check(self.dealer.score, self.player1.score))
        self.Lstatus2.configure(text=self.check(self.dealer.score, self.player2.score))
        self.Lstatus3.configure(text=self.check(self.dealer.score, self.player3.score))

        if self.check(self.dealer.score, self.player1.score) == "승":
            self.playerMoney += self.betMoney1 * 2
        if self.check(self.dealer.score, self.player2.score) == "승":
            self.playerMoney += self.betMoney2 * 2
        if self.check(self.dealer.score, self.player3.score) == "승":
            self.playerMoney += self.betMoney3 * 2

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

    def check(self, dealer, player):
        if player > dealer:
            return "승"
        elif player < dealer:
            return "패"
        else:
            return "무"

    def made10(self, Player, Cards, List, Status, x, y):  # score리턴
        made = False
        madelist = []
        L = List.copy()
        status = ""
        rest = ""
        score = 0
        for i in itertools.combinations(List, 3):
            if sum(list(i)) % 10 == 0:
                made = True
                madelist = sorted(list(i))
                if madelist == [1, 1, 8]:
                    status = "콩콩팔(1 1 8)"
                elif madelist == [1, 2, 7]:
                    status = "삐리칠(1 2 7)"
                elif madelist == [1, 3, 6]:
                    status = "물삼육(1 3 6)"
                elif madelist == [1, 4, 5]:
                    status = "빽새오(1 4 5)"
                elif madelist == [1, 9, 10]:
                    status = "삥구장(1 9 10)"
                elif madelist == [2, 2, 6]:
                    status = "니니육(2 2 6)"
                elif madelist == [2, 3, 5]:
                    status = "이삼오(2 3 5)"
                elif madelist == [2, 8, 10]:
                    status = "이판장(2 8 10)"
                elif madelist == [3, 3, 4]:
                    status = "심심새(3 3 4)"
                elif madelist == [3, 7, 10]:
                    status = "삼칠장(3 7 10)"
                elif madelist == [3, 8, 9]:
                    status = "삼빡구(3 8 9)"
                elif madelist == [2, 4, 4]:
                    status = "살살이(4 4 2)"
                elif madelist == [4, 6, 10]:
                    status = "사륙장(4 6 10)"
                elif madelist == [4, 7, 9]:
                    status = "사칠구(4 7 9)"
                elif madelist == [5, 5, 10]:
                    status = "꼬꼬장(5 5 10)"
                elif madelist == [5, 6, 9]:
                    status = "오륙구(5 6 9)"
                elif madelist == [5, 7, 8]:
                    status = "오리발(5 7 8)"
                elif madelist == [6, 6, 8]:
                    status = "쭉쭉팔(6 6 8)"
                elif madelist == [6, 7, 7]:
                    status = "철철육(7 7 6)"
                elif madelist == [4, 8, 8]:
                    status = "팍팍싸(8 8 4)"
                elif madelist == [2, 9, 9]:
                    status = "구구리(9 9 2)"
                else:
                    madelist = []
                    made = False
        if made == False:
            status = "노 메이드"
        elif made == True:
            for i in range(len(madelist)):
                L[L.index(madelist[i])] = ""

        # 월 출력
        for i in range(len(L)):
            if L[i] == "":
                Pts = Label(text=List[i], width=2, height=1, font=self.fontstyle2, bg="green", fg="orange")
                if Cards == self.LcardsDealer:
                    Cards[i].place(y=90 + 30)
                if Cards == self.LcardsPlayer1:
                    Cards[i].place(y=350 + 30)
                if Cards == self.LcardsPlayer2:
                    Cards[i].place(y=350 + 30)
                if Cards == self.LcardsPlayer3:
                    Cards[i].place(y=350 + 30)
            else:
                Pts = Label(text=List[i], width=2, height=1, font=self.fontstyle2, bg="green", fg="white")
            Pts.place(x=x + i * 30, y=y)

        # 자투리 계산
        if made == True:
            L = list(filter(None, L))
            L.sort()
            if L == [3, 8]:  # 38광땡
                rest = "1끗"
                score = 2
                for i in range(5):
                    if List[i] == 3 and Player.cards[i].filename() == "3.1.gif":
                        for j in range(5):
                            if List[i] == 8 and Player.cards[i].filename() == "8.1.gif":
                                rest = "38광땡"
                                score = 22
            elif L == [1, 8]:  # 18광땡
                rest = "9끗"
                score = 5
                for i in range(5):
                    if List[i] == 1 and Player.cards[i].filename() == "1.1.gif":
                        for j in range(5):
                            if List[i] == 8 and Player.cards[i].filename() == "8.1.gif":
                                rest = "18광땡"
                                score = 21
            elif L == [1, 3]:  # 13광땡
                rest = "4끗"
                score = 5
                for i in range(5):
                    if List[i] == 1 and Player.cards[i].filename() == "1.1.gif":
                        for j in range(5):
                            if List[i] == 3 and Player.cards[i].filename() == "3.1.gif":
                                rest = "13광땡"
                                score = 20
            elif L[0] == L[1]:  # 땡
                rest = str(L[0]) + "땡"
                score = 9 + L[0]
            elif L == [1, 9]:
                rest = "망통"
                score = 1
            elif L == [2, 8]:  # 28망통
                rest = "망통"
                score = 1
            elif L == [3, 7]:  # 37망통
                rest = "망통"
                score = 1
            elif L == [4, 6]:
                rest = "망통"
                score = 1
            elif L == [5, 5]:
                rest = "망통"
                score = 1
            else:  # 끗
                rest = str(sum(L) % 10) + "끗"
                score = 1 + sum(L) % 10

        # 메이드+자투리 출력
        Status.configure(text=status + " " + rest)

        return score


Gamble()