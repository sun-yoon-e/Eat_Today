class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.suits = []
        self.values = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()
        self.suits.clear()
        self.values.clear()

    def returnValue(self):
        for i in range(len(self.cards)):
            self.values.append(self.cards[i].getValue())
        return self.values

    def returnSuit(self):
        for i in range(len(self.cards)):
            self.suits.append(self.cards[i].getSuit())
        return self.suits
