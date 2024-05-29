/* A digital clock project in Python utilizes the `tkinter` library to create a 
GUI application that displays the current time, updating every second. It leverages the 
`time` module to fetch and format the system time continuously. */


from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("CLOCK")

def time():
    string = strftime(' %H:%M:%S %p  ')
    label.config(text=string)
    label.after(1000, time)

frame = Frame(root, borderwidth=5, relief="solid", padding=(10, 10))
frame.pack(padx=20, pady=20, anchor='center')

label = Label(frame, font=("ds-digital", 80), background="grey", foreground="black")
label.pack()

time()
mainloop()
