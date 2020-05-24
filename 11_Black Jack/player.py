class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        #ace는 1혹은 11로 모두 사용 가능
        #일단 11로 계산한 후 21이 넘어가면 1로 정정
        total = 0
        ace = 0
        for i in range(self.N):
            total += self.cards[i].getValue()
            if self.cards[i].getValue() ==1:
                pass
            if self.cards[i].getValue() == 2:
                pass
            if self.cards[i].getValue() == 3:
                pass
            if self.cards[i].getValue() == 4:
                pass
            if self.cards[i].getValue() == 5:
                pass
            if self.cards[i].getValue() == 6:
                pass
            if self.cards[i].getValue() == 7:
                pass
            if self.cards[i].getValue() == 8:
                pass
            if self.cards[i].getValue() == 9:
                pass
            if self.cards[i].getValue() == 10:
                pass