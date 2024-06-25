from tkinter import *
from tkinter import messagebox

Player1 = 'X'
stop_game = False

def clicked(r, c):
    global Player1, stop_game
    if states[r][c] == 0 and not stop_game:
        b[r][c].config(bg='black')  # Change background color to black
        if Player1 == 'X':
            b[r][c].config(text=Player1, fg='white', font=("Helvetica", 24, "bold"))  # Change text color to white
            states[r][c] = Player1
            Player1 = 'O'
        else:
            b[r][c].config(text=Player1, fg='purple', font=("Helvetica", 24, "bold"))  # Purple for 'O' remains the same
            states[r][c] = Player1
            Player1 = 'X'
        check_if_win()

def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0 or states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            messagebox.showinfo("Winner", f"{states[i][0] if states[i][0] != 0 else states[0][i]} Won")
            return
    if states[0][0] == states[1][1] == states[2][2] != 0 or states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        messagebox.showinfo("Winner", f"{states[1][1]} Won")
        return
    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "It's a Tie")

root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

b = [[0] * 3 for _ in range(3)]
states = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(root, height=4, width=8, font=("Helvetica", 20, "bold"), bd=4, command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

mainloop()
