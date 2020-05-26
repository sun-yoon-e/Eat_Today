from tkinter import *

class EatToday:
    def __init__(self):
        self.window = Tk()
        self.window.title('오늘 뭐 먹지~?')
        self.window.geometry('600x800')
        self.window.configure(background='lemon chiffon')
        self.window.mainloop()

EatToday()