class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.months = []
        self.values = []
        self.N = 0
        self.score = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()
        self.months.clear()
        self.values.clear()

    def returnMonth(self):
        self.months = []
        for i in range(len(self.cards)):
            self.months.append(self.cards[i].getMonth())
        return self.months

    def returnValue(self):
        self.values = []
        for i in range(len(self.cards)):
            self.values.append(self.cards[i].getValue())
        return self.values