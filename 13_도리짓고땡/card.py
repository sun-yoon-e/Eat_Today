class Card:
    def __init__(self, temp):
        #랜덤 넘버 0...41 값을 입력받아서 카드 객체 생성
        self.value = temp % 4 + 1 #1...4
        self.x = temp // 4 + 1

    def getValue(self):
        return self.value

    def getSuit(self):
        #카드 무늬 결정
        if self.x == 1:
            self.suit = "1"
        elif self.x == 2:
            self.suit = "2"
        elif self.x == 3:
            self.suit = "3"
        elif self.x == 4:
            self.suit = "4"
        elif self.x == 5:
            self.suit = "5"
        elif self.x == 6:
            self.suit = "6"
        elif self.x == 7:
            self.suit = "7"
        elif self.x == 8:
            self.suit = "8"
        elif self.x == 9:
            self.suit = "9"
        elif self.x == 10:
            self.suit = "10"

        return self.suit

    def filename(self):
        #카드 이미지 파일 이름
        return self.getSuit() + "." + str(self.value) + ".gif"