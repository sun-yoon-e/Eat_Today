class Card:
    def __init__(self, temp):
        self.month = temp // 4 + 1
        self.value = temp % 4 + 1

    def getMonth(self):
        return self.month

    def getValue(self):
        return self.value

    def filename(self):
        return str(self.month) + "." + str(self.value) + ".gif"