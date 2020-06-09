from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random


class Poker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        self.cardDeck = [i for i in range(52)]

        self.count = 0
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.table = Player("table")
        self.betMoney = 10
        self.playerMoney = 990
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.LcardsTable = []
        self.PlayerValue = []
        self.DealerValue = []
        self.PlayerSuit = []
        self.DealerSuit = []
        self.TableValue = []
        self.TableSuit = []
        self.deckN = 0
        self.window.mainloop()

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)

        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $990", width=15, height=1, font=self.fontstyle, bg="green",
                                  fg="orange")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerStatus = Label(text="", width=20, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerStatus.place(x=220, y=400)
        self.LdealerStatus = Label(text="", width=20, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LdealerStatus.place(x=220, y=100)
        self.Lstatus = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=500, y=300)

    def pressedCheck(self):
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"
        PlaySound('sounds/chip.wav', SND_FILENAME)

        if self.count == 6:
            self.checkWinner()

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def pressedBx1(self):
        money = self.betMoney
        self.betMoney += self.betMoney
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= money * 1
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= self.betMoney

        if self.count == 6:
            self.checkWinner()

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def pressedBx2(self):
        money = self.betMoney
        self.betMoney += self.betMoney * 2
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= money * 2
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= self.betMoney

        if self.count == 6:
            self.checkWinner()

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

    def deal(self):
        self.player.reset()
        self.dealer.reset()  # 카드 덱 52 장 셔플링 0,1,,.51
        self.table.reset()
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer(0)  # 플레이어 카드 한장
        self.hitDealer(0)  # 딜러 카드 한장
        self.hitPlayer(1)  # 플레이어 카드 한장 더
        self.hitDealer(1)  # 딜러 카드 한장 더

        self.Check['state'] = 'active'
        self.Check['bg'] = 'light gray'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'light gray'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'light gray'

    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))

        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 80, y=50)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + n * 80, y=350)

        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

    def hitTable(self, n):
        for i in range(n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.table.addCard(newCard)
            p = PhotoImage(file="cards/" + newCard.filename())
            self.LcardsTable.append(Label(self.window, image=p))

            # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LcardsTable[self.table.inHand() - 1].image = p
            self.LcardsTable[self.table.inHand() - 1].place(x=70 + self.count * 80, y=200)
            self.count += 1

            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

            self.Check['state'] = 'active'
            self.Check['bg'] = 'light gray'
            self.Bx1['state'] = 'active'
            self.Bx1['bg'] = 'light gray'
            self.Bx2['state'] = 'active'
            self.Bx2['bg'] = 'light gray'

    def pressedDeal(self):
        if self.count == 0:
            self.deal()
            self.count += 1
        elif self.count == 1:
            self.hitTable(3)
        elif self.count == 4 or self.count == 5:
            self.hitTable(1)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

    def pressedAgain(self):
        self.Check['state'] = 'active'
        self.Check['bg'] = 'light gray'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'light gray'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'light gray'

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        for item in self.LcardsDealer:
            item.image = None
            item.destroy()

        for item in self.LcardsPlayer:
            item.image = None
            item.destroy()

        for item in self.LcardsTable:
            item.image = None
            item.destroy()

        # 카드 초기화
        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()
        self.LcardsTable.clear()
        self.deckN = 0
        self.count = 0

        self.LdealerStatus.configure(text="")
        self.LplayerStatus.configure(text="")
        self.Lstatus.configure(text="")

        self.betMoney = 10
        self.playerMoney -= 10
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p0 = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        p1 = PhotoImage(file="cards/" + self.dealer.cards[1].filename())
        self.LcardsDealer[0].configure(image=p0)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p0  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[1].configure(image=p1)
        self.LcardsDealer[1].image = p1

        self.TableSuit = self.table.returnSuit()
        self.DealerSuit = self.dealer.returnSuit() + self.TableSuit
        self.PlayerSuit = self.player.returnSuit() + self.TableSuit
        self.TableValue = self.table.returnValue()
        self.DealerValue = self.dealer.returnValue() + self.TableValue
        self.PlayerValue = self.player.returnValue() + self.TableValue

        # 딜러 카드 7장 체크---------------------------------------------
        dealerScore = []
        dealerPair = 0  # 딜러 페어
        dealerStraight = 1  # 딜러 스트레이트
        dealerMaxNopair = 0  # 노페어일때 카드 최댓값
        dealerValuePair = []  # 페어일때 밸류값
        dealerMaxPair = 0  # 페어일때 카드 최댓값

        # 페어 체크
        for i in range(0, len(self.DealerValue) - 1):
            for j in range(i + 1, len(self.DealerValue)):
                if self.DealerValue[i] == self.DealerValue[j]:
                    dealerPair += 1
                    if dealerPair > 0:
                        dealerValuePair.append(self.DealerValue[i])

        self.DealerValue = list(set(self.DealerValue))
        self.DealerValue.sort()

        # 같은 무늬 5장(플러쉬) 체크
        dcounts = []
        dcounts.append(self.DealerSuit.count("Clubs"))
        dcounts.append(self.DealerSuit.count("Spades"))
        dcounts.append(self.DealerSuit.count("Hearts"))
        dcounts.append(self.DealerSuit.count("Diamonds"))
        dcount = max(dcounts)
        if dcount == 5:
            dealerScore.append(6)

        # 스트레이트 체크
        for j in range(1, len(self.DealerValue)):
            if (self.DealerValue[j - 1] == self.DealerValue[j] - 1):
                dealerStraight += 1
            else:
                dealerStraight = 1
            if (dealerStraight == 5):
                dealerScore.append(5)

        # 노페어
        if dealerPair == 0:
            dealerScore.append(1)
        # 원페어
        elif dealerPair == 1:
            dealerScore.append(2)
        # 투페어
        elif dealerPair == 2:
            dealerScore.append(3)
        # 트리플
        elif dealerPair == 3:
            dealerScore.append(4)
        # 풀하우스
        elif dealerPair == 4:
            dealerScore.append(7)
        # 포카드
        elif dealerPair == 6:
            dealerScore.append(8)

        # 카드 최댓값 계산
        dScore = max(dealerScore)
        if dScore == 1:  # 노페어일때
            dealerMaxNopair = max(self.DealerValue)
            self.LdealerStatus.configure(text="No pair" + str(dealerMaxNopair))
        elif dScore == 7:
            self.LdealerStatus.configure(text="Full House" + str(dealerMaxNopair))
        elif dScore == 8:
            self.LdealerStatus.configure(text="Four Card" + str(dealerMaxNopair))

        elif 1 < dScore < 5 or dScore == 7 or dScore == 8:
            dealerMaxPair = max(dealerValuePair)
            if dScore == 2:
                self.LdealerStatus.configure(text="One Pair" + str(dealerMaxPair))
            elif dScore == 3:
                self.LdealerStatus.configure(text="Two Pair" + str(dealerMaxPair))
            elif dScore == 4:
                self.LdealerStatus.configure(text="Triple" + str(dealerMaxPair))

        elif dScore == 5:
            self.LdealerStatus.configure(text="Straight")
        elif dScore == 6:
            self.LdealerStatus.configure(text="Flush")

        # 플레이어 카드 7장 체크---------------------------------------------
        playerScore = []
        playerPair = 0  # 딜러 페어
        playerStraight = 1  # 딜러 스트레이트
        playerMaxNopair = 0  # 노페어일때 카드 최댓값
        playerValuePair = []  # 페어일때 밸류값
        playerMaxPair = 0  # 페어일때 카드 최댓값

        # 페어 체크
        for i in range(0, len(self.PlayerValue) - 1):
            for j in range(i + 1, len(self.PlayerValue)):
                if self.PlayerValue[i] == self.PlayerValue[j]:
                    playerPair += 1
                    if playerPair > 0:
                        playerValuePair.append(self.PlayerValue[i])

        self.PlayerValue = list(set(self.PlayerValue))
        self.PlayerValue.sort()

        # 같은 무늬 5장(플러쉬) 체크
        pcounts = []
        pcounts.append(self.PlayerSuit.count("Clubs"))
        pcounts.append(self.PlayerSuit.count("Spades"))
        pcounts.append(self.PlayerSuit.count("Hearts"))
        pcounts.append(self.PlayerSuit.count("Diamonds"))
        pcount = max(pcounts)
        if pcount == 5:
            playerScore.append(6)

        # 스트레이트 체크
        for j in range(1, len(self.PlayerValue)):
            if (self.PlayerValue[j - 1] == self.PlayerValue[j] - 1):
                playerStraight += 1
            else:
                playerStraight = 1
            if (playerStraight == 5):
                playerScore.append(5)

        # 노페어
        if playerPair == 0:
            playerScore.append(1)
        # 원페어
        elif playerPair == 1:
            playerScore.append(2)
        # 투페어
        elif playerPair == 2:
            playerScore.append(3)
        # 트리플
        elif playerPair == 3:
            playerScore.append(4)
        # 풀하우스
        elif playerPair == 4:
            playerScore.append(7)
        # 포카드
        elif playerPair == 6:
            playerScore.append(8)

        # 카드 최댓값 계산
        pScore = max(playerScore)
        if pScore == 1:  # 노페어일때
            playerMaxNopair = max(self.PlayerValue)
            self.LplayerStatus.configure(text="No pair" + str(playerMaxNopair))
        elif pScore == 7:
            self.LplayerStatus.configure(text="Full House" + str(playerMaxNopair))
        elif pScore == 8:
            self.LplayerStatus.configure(text="Four Card" + str(playerMaxNopair))

        elif 1 < pScore < 5 or pScore == 7 or pScore == 8:
            playerMaxPair = max(playerValuePair)
            if pScore == 2:
                self.LplayerStatus.configure(text="One Pair" + str(playerMaxPair))
            elif pScore == 3:
                self.LplayerStatus.configure(text="Two Pair" + str(playerMaxPair))
            elif pScore == 4:
                self.LplayerStatus.configure(text="Triple" + str(playerMaxPair))

        elif pScore == 5:
            self.LplayerStatus.configure(text="Straight")
        elif pScore == 6:
            self.LplayerStatus.configure(text="Flush")

        # 위너 체크
        if dScore > pScore:
            self.Lstatus.configure(text="Lose")

        if dScore == pScore:
            if dScore == 1 or dScore == 5 or dScore == 6:  # 노페어일때 맥스값 비교
                if dealerMaxNopair > playerMaxNopair:
                    self.Lstatus.configure(text="Lose")
                elif dealerMaxNopair == playerMaxNopair:
                    self.Lstatus.configure(text="Push")
                    self.playerMoney += self.betMoney
                elif dealerMaxNopair < playerMaxNopair:
                    self.Lstatus.configure(text="Win")
                    self.playerMoney += self.betMoney * 2
            else:  # 페어일때 맥스값 비교
                if dealerMaxPair > playerMaxPair:
                    self.Lstatus.configure(text="Lose")
                elif dealerMaxPair == playerMaxPair:
                    self.Lstatus.configure(text="Push")
                    self.playerMoney += self.betMoney
                elif dealerMaxPair < playerMaxPair:
                    self.Lstatus.configure(text="Win")
                    self.playerMoney += self.betMoney * 2

        if dScore < pScore:
            self.Lstatus.configure(text="Win")
            self.playerMoney += self.betMoney * 2

        self.betMoney = 0
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'


Poker()