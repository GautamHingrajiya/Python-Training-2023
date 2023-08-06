from tkinter import *
from random import *

screen = Tk()

screen.geometry("500x500")
screen.title("My Python")
"""

Python Logic Here

"""
def myLogic(userchoice):
    l1 = ["ROCK","PAPER","SISSOR"]
    print("User Choice :",userchoice)
    c_choice = choice(l1)
    print("Computer Choice : ", c_choice )

btn = Button(screen,text="ROCK",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("ROCK"))
btn.place(x=10,y=20)

btn = Button(screen,text="PAPER",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("PAPER"))
btn.place(x=80,y=20)

btn = Button(screen,text="SISSOR",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("SISSOR"))
btn.place(x=150,y=20)


screen.mainloop()    