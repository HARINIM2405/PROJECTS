from tkinter import *
from tkinter import font

class Info(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.configure(width=500, height=100)
        police = font.Font(self, size=20, family='Arial')
        self.t = Label(self, text="Yellow's Turn", font=police)
        self.t.grid(sticky=NSEW, pady=20)

class Token(object):
    def __init__(self, x, y, can, color="white", bg="red"):
        self.can = can
        self.x = x
        self.y = y
        self.color = color
        self.turn = 1
        self.r = 30
        self.token = self.can.create_oval(self.x + 10, self.y + 10, self.x + 61, self.y + 61, fill=color, outline="black")
        
    def changeColor(self, color):
        self.can.itemconfigure(self.token, fill=color)
        self.color = color

class Board(Canvas):
    def __init__(self, master=None):
        Canvas.__init__(self)
        self.configure(width=500, height=400, bg="black")

        self.player = 1
        self.color = "yellow"
        self.p = []
        self.perm = True
        
        for i in range(0, 340, int(400 / 6)):
            row_list = []
            for j in range(0, 440, int(500 / 7)):
                row_list.append(Token(j, i, self))
                
            self.p.append(row_list)
        
        self.bind("<Button-1>", self.detCol)

    def detCol(self, event):
        if self.perm:
            col = int(event.x / 71)
            row = 0
            
            while row < len(self.p):            
                if self.p[0][col].color == "grey" or self.p[0][col].color == "yellow":
                    break
                
                if self.p[row][col].color == "grey" or self.p[row][col].color == "yellow":
                    self.p[row - 1][col].changeColor(self.color)
                    break
                
                elif row == len(self.p) - 1:
                    self.p[row][col].changeColor(self.color)
                    break
                
                if self.p[row][col].color != "grey" and self.p[row][col].color != "yellow":
                    row += 1

            if self.player == 1:
                self.player = 2
                info.t.config(text="Grey's Turn")
                self.color = "grey"

            elif self.player == 2:
                self.player = 1
                info.t.config(text="Yellow's Turn")
                self.color = "yellow"

class Game(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.pack()
        global info
        info = Info(self)
        info.pack()
        self.board = Board(self)
        self.board.pack()

if __name__ == "__main__":
    root = Tk()
    root.title("Connect Four")
    game = Game(root)
    root.mainloop()
