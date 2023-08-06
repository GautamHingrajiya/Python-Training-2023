from tkinter import * 
import random

screen = Tk()
screen.title("Game")
screen.geometry("720x480")
screen.maxsize(720,480)
screen.minsize(720,480)
screen.config(bg = '#FFE873')


user_select = StringVar()
computer_select = StringVar()
result = StringVar()
u_score = int()
c_score = int()


def myLogic(userchoice):
    user_select.set(userchoice)
    list1 = ["ROCK","PAPER","SISSOR"]
    c_select = random.choice(list1)
    computer_select.set(c_select)

    if user_select == computer_select:
        print("TIE")
        result1 = "TIE"
        result.set(result1)
        print(result)

    elif user_select == "ROCK" and computer_select == "PAPER" :
        result.set("COMPUTER WON !!!")
        c_Score += 1
    elif user_select == "ROCK" and computer_select ==  "SCISSOR" :
        result.set("USER WON !!!")
        u_score += 1
    elif user_select == "SCISSOR" and computer_select == "PAPER" :
        result.set("USER WON !!!")
        u_score += 1
    elif user_select == "SCISSOR" and computer_select ==  "ROCK" :
        result.set("COMPUTER WON !!!")
        c_score += 1
    elif user_select == "PAPER" and computer_select == "ROCK" :
        result.set("USER WON !!!")
        u_score += 1
    elif user_select == "PAPER" and computer_select ==  "SCISSOR" :
        result.set("COMPUTER WON !!!")
        c_Score += 1
    





# heading
head_lable = Label(screen,text="Rock-Paper-Sissor Game",font=("Arial",18,"bold"))
head_lable.pack()

# user select lable
lable_user_select = Label(screen,text="User_Select : ",font=("Franklin Gothic Heavy",10))
lable_user_select.place(x=10,y=55)

#user selected Display
# lable_user_display = Label(screen,textvariable = user_select,font=("Franklin Gothic Heavy",12))
# lable_user_display.place(x=380,y= 55)

# user score lable
lable_user_score = Label(screen,text="User_Score : ",font=("Franklin Gothic Heavy",10))
lable_user_score.place(x=10,y=150)
# user score display


# button
btn_rock=Button(screen,text="ROCK",font=("Tahoma",12,"bold"),activeforeground="red",activebackground="blue",command=lambda : myLogic("ROCK"))
btn_rock.place(x=130 , y=50)
btn_paper=Button(screen,text="PAPER",font=("Tahoma",12,"bold"),activeforeground="red",activebackground="blue",command=lambda : myLogic("PAPER"))
btn_paper.place(x=200 , y=50)
btn_sissor=Button(screen,text="SISSOR",font=("Tahoma",12,"bold"),activeforeground="red",activebackground="blue",command=lambda : myLogic("SISSOR"))
btn_sissor.place(x=280 , y=50)

# computer select lable
lable_computer_select = Label(screen,text="Computer_Select : ",font=("Franklin Gothic Heavy",10))
lable_computer_select.place(x=10,y=100)

# computer selected display
lable_computer_display = Label(screen,textvariable = computer_select,font=("Franklin Gothic Heavy",12))
lable_computer_display.place(x=200,y= 100)

# computer score lable
lable_computer_score = Label(screen,text="Computer_Score : ",font=("Franklin Gothic Heavy",10))
lable_computer_score.place(x=200,y=150)
#  computer score display

# result_str
result_display = Label(screen,textvariable=result,font=("Franklin Gothic Heavy",10))
result_display.place(x=400,y=150)



screen.mainloop()