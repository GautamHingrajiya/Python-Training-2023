from tkinter import *

screen = Tk()

screen.geometry("500x500")
screen.title("My Python")
title = Label(screen,text="Welcome to GUI App Python",font= ('arial',20,'bold'))
title.pack()

screen.mainloop()