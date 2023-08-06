from tkinter import *
import random

screen = Tk()
screen.title("Game")
screen.geometry("720x480")
# screen.maxsize(720,480)
# screen.minsize(720,480)
screen.resizable(width="false",height="false")

compuert_select = StringVar()
result = StringVar()
u_score = int()
c_score = int()


def myLogic(userchoice):
    l1 = ["ROCK","PAPER","SISSOR"]
    c_select = random.choice(l1)
    compuert_select.set(c_select)
    # print(userchoice)

    if userchoice == c_select:
        print(" TIE ")
        result.set(" TIE ")
 
    elif (userchoice == "ROCK" and c_select == "PAPER") or (userchoice == "SISSOR" and c_select ==  "ROCK") or (userchoice == "PAPER" and c_select ==  "SISSOR") :
        print(" COMPUTER WON !!! ")
        result.set(" COMPUTER WON !!! ")
       
        
    elif (userchoice == "ROCK" and c_select ==  "SISSOR") or (userchoice == "SISSOR" and c_select == "PAPER") or (userchoice == "PAPER" and c_select == "ROCK"):
        print(" USER WON !!! ")
        result.set(" USER WON !!! ")

    elif userchoice == "Final":
        u_score
    



lable_heading= Label(screen,text= "ROCK-PAPER-SISSOR GAME",font=("arial",16,"bold"))
lable_heading.pack()

# lables

lable1 = Label(screen,text="User_Choice : ",font=("arial",12,"bold"))
lable1.place(x=10,y=50)

lable2 = Label(screen,text="Computer_Choice : ",font=("arial",12,"bold"))
lable2.place(x=10,y=80)

lable_computer = Label(screen,textvariable=compuert_select,font=("arial",10,"bold"))
lable_computer.place(x=200,y=80)

lable_result = Label(screen,text="Result : ",font=("arial",14,"bold"))
lable_result.place(x=100,y=120)

lable_resu = Label(screen,textvariable=result,font=("arial",14,"bold"))
lable_resu.place(x=200,y=120)

lable_result = Label(screen,text="Result : ",font=("arial",14,"bold"))
lable_result.place(x=100,y=120)


# button

btn_rock = Button(screen,text="ROCK",font=("arial",8,"bold"),command=lambda:myLogic("ROCK"))
btn_rock.place(x=150,y=50)

btn_paper = Button(screen,text="PAPER",font=("arial",8,"bold"),command=lambda:myLogic("PAPER"))
btn_paper.place(x=200,y=50)

btn_sissor = Button(screen,text="SISSOR",font=("arial",8,"bold"),command=lambda:myLogic("SISSOR"))
btn_sissor.place(x=255,y=50)

btn_final = Button(screen,text="Final",font=("arial",20,"bold"),command=lambda:myLogic("Final"))
btn_final.place(x=255,y=300)



screen.mainloop()