from tkinter import *


screen = Tk()
screen.title("Billing Software")
screen.geometry("1366x768")
screen.configure(bg="#ABEBC6")
screen.state('zoomed')
# screen.maxsize(width=1366,height=768)
# screen.minsize(width=1300,height=700)

# Frame Section
frame_header = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE)
frame_header.pack(fill="x",side="top")

frame_footer = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE)
frame_footer.pack(fill="x",side="bottom")

frame_Cdetails = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE,pady= 5)
frame_Cdetails.pack(fill="x")

frame_Billmenu = Frame(screen,bg="#2C3E50",borderwidth=4,relief=GROOVE)
frame_Billmenu.pack(side="bottom",fill= "x")

frame_Cosmetic = Frame(screen,bg="#2C3E50",borderwidth=4,relief= GROOVE,pady= 2)
frame_Cosmetic.pack(side= "left")

frame_Grocery = Frame(screen,bg="#2C3E50",borderwidth=4,relief= GROOVE,pady= 2)
frame_Grocery.pack(side= "left")

frame_Other = Frame(screen,bg="#2C3E50",borderwidth=4,relief= GROOVE,pady= 2)
frame_Other.pack(side= "left")

frame_Billviwe = Frame(screen,bg="#2C3E50",borderwidth=4,relief= GROOVE,pady= 2)
frame_Billviwe.pack(side= "bottom" )

# lable section

lable_Cdetails = Label(screen,text="Customer Details : ",font=("Candara",12,"bold"),fg="red",padx= 2,pady= 1,borderwidth= 2,bg="#2C3E50")
lable_Cdetails.place(x= 10,y=40)

# lable_Billmenu = Label(screen,text="Bill Menu : ",font=("Candara",12,"bold"),fg="red",padx= 2,pady= 1,borderwidth= 2,bg="#2C3E50")
# lable_Billmenu.place(x=10, y= 530)

lable_heading = Label(frame_header,text="Billing Software",font=("Baufra",20,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_heading.pack()


lable_Billno = Label(frame_Cdetails,text="Bill No. : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Billno.pack(side= LEFT)

lable_Cname = Label(frame_Cdetails,text="Customer Name : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Cname.pack(side= LEFT)

lable_Cmno = Label(frame_Cdetails,text="Mobile No. : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_Cmno.pack(side= LEFT)

lable_Bathsoap = Label(frame_Cosmetic,text="Bath Soap : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Bathsoap.pack()

lable_Facecream = Label(frame_Cosmetic,text="Face Cream : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Facecream.pack()

lable_Facewash = Label(frame_Cosmetic,text="Face Wash : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Facewash.pack()

lable_Hairspary = Label(frame_Cosmetic,text="Hair Spray : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Hairspary.pack()

lable_Bodylotion = Label(frame_Cosmetic,text="Body Lotion : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Bodylotion.pack()

lable_Rise = Label(frame_Grocery,text="Rise : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Rise.pack()

lable_Foodoil = Label(frame_Grocery,text="Food Oil : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Foodoil.pack()

lable_Daal = Label(frame_Grocery,text="Daal : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Daal.pack()

lable_Wheat = Label(frame_Grocery,text="Wheat : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Wheat.pack()

lable_Sugar = Label(frame_Grocery,text="Sugar : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Sugar.pack()

lable_Maza = Label(frame_Other,text="Maza : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Maza.pack()

lable_Coke = Label(frame_Other,text="Coke : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Coke.pack()

lable_Frooti = Label(frame_Other,text="Frooti : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Frooti.pack()

lable_Namkeens = Label(frame_Other,text="Namkeens : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Namkeens.pack()

lable_Biscuits = Label(frame_Other,text="Biscuits : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Biscuits.pack()

lable_Cosmeticstotal = Label(frame_Billmenu,text="Cosmetics Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Cosmeticstotal.place(x=20,y=1)

lable_Grocerystotal = Label(frame_Billmenu,text="Grocerys Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
lable_Grocerystotal.place(x=20,y=6)

# lable_Otherstotal = Label(frame_Billmenu,text="Others Total : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
# lable_Otherstotal.place(x=20,y=9)

# lable_Cosmeticstax = Label(frame_Billmenu,text="Cosmetics Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
# lable_Cosmeticstax.pack()

# lable_Grocerystax = Label(frame_Billmenu,text="Grocerys Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
# lable_Grocerystax.pack()

# lable_Otherstax = Label(frame_Billmenu,text="Others Tax : ",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 10,borderwidth= 2,bg="#2C3E50")
# lable_Otherstax.pack()







lable_footer = Label(frame_footer,text="By : Lionize Developers LLP",font=("Candara",10,"bold"),fg="white",padx= 5,pady= 5,borderwidth= 2,bg="#2C3E50")
lable_footer.pack()



screen.mainloop()