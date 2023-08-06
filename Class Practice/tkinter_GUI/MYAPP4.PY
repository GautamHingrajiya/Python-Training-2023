from tkinter import *
from random import *

screen = Tk()

screen.title("My Python")
screen.geometry("500x500")
screen.maxsize(720,480)
screen.minsize(720,480)
screen.config(bg = '#FFE873')

user_var = StringVar()
c_var = StringVar()
result = StringVar()
U_Score = int()
C_Score = int()
"""

Python Logic Here

"""
def myLogic(userchoice):
    global U_Score
    global C_Score

    l1 = ["ROCK","PAPER","SISSOR"]
    print("User Choice :",userchoice)
    c_choice = choice(l1)
    print("Computer Choice : ", c_choice )
    user_var.set(userchoice)
    c_var.set(c_choice)

    if userchoice == c_choice:
        print(" TIE ")
        result.set("TIE")
    elif userchoice == "ROCK" and c_choice == "PAPER" :
        print(" COMPUTER WON !!! ")
        result.set("COMPUTER WON !!!")
        C_Score += 1
    elif userchoice == "ROCK" and c_choice ==  "SCISSOR" :
        print(" USER WON !!! ")
        result.set("USER WON !!!")
        U_Score += 1
    elif userchoice == "SCISSOR" and c_choice == "PAPER" :
        print(" USER WON !!! ")
        result.set("USER WON !!!")
        U_Score += 1
    elif userchoice == "SCISSOR" and c_choice ==  "ROCK" :
        print(" COMPUTER WON !!! ")
        result.set("COMPUTER WON !!!")
        C_Score += 1
    elif userchoice == "PAPER" and c_choice == "ROCK" :
        print(" USER WON !!! ")
        result.set("USER WON !!!")
        U_Score += 1
    elif userchoice == "PAPER" and c_choice ==  "SCISSOR" :
        print(" COMPUTER WON !!! ")
        result.set("COMPUTER WON !!!")
        C_Score += 1


Label1 = Label(text="Rock-Paper-Sissor Game", font=("arial",15,"bold"))
Label1.pack()
btn = Button(screen,text="ROCK",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("ROCK"))
btn.place(x=150,y=40)

btn = Button(screen,text="PAPER",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("PAPER"))
btn.place(x=350,y=40)

btn = Button(screen,text="SISSOR",font=("arial",12,"bold"),bg="black",fg="white",activebackground="purple",activeforeground="white",command=lambda:myLogic("SISSOR"))
btn.place(x=550,y=40)


user_display = Label(screen,text="User : ",font=("arial",12,"bold"),fg= "blue")
user_display.place(x=10,y=80)
user_display = Label(screen,textvariable= user_var,font=("arial",12,"bold"),fg= "blue")
user_display.place(x=60,y=80)

c_display = Label(screen,text="computer : ",font=("arial",12,"bold"),fg= "red")
c_display.place(x=150,y=80)
c_display = Label(screen,textvariable= c_var,font=("arial",12,"bold"),fg= "red")
c_display.place(x=240,y=80)

user_score = Label(screen,text="U_Score : ",font=("arial",12,"bold"),fg= "blue")
user_score.place(x=500,y=80)
u_score = Label(screen,textvariable=U_Score,font=("arial",12,"bold"),fg= "red")
u_score.place(x=600,y=160)

result_display = Label(screen,textvariable=result,font=("Franklin Gothic Heavy",10))
result_display.place(x=400,y=150)


c_score = Label(screen,text="C_Score : ",font=("arial",12,"bold"),fg= "blue")
c_score.place(x=600,y=80)
c_score = Label(screen,textvariable=C_Score,font=("arial",12,"bold"),fg= "red")
c_score.place(x=600,y=160)
screen.mainloop()    