import random
Teams = """
            1.CHENNAI SUPER KINGS,
            2.DELHI CAPITALS
            3.GUJARAT TITANS
            4.KOLKATA KNIGHT RIDERS
            5.LUCKNOW SUPER GIANTS
            6.MUMBAI INDIANS
            7.PUNJAB KINGS
            8.RAJASTHAN ROYALS
            9.ROYAL CHALLANGE BANGALORE
            10.SUNRISE HYDERABAD

        """

print(Teams)
print("\n ------------- Team Selection-------------\n")

team_list = ["CHENNAI SUPER KINGS","DELHI CAPITALS","GUJARAT TITANS","KOLKATA KNIGHT RIDERS","LUCKNOW SUPER GIANTS","MUMBAI INDIANS","PUNJAB KINGS","RAJASTHAN ROYALS","ROYAL CHALLANGE BANGALORE","1SUNRISE HYDERABAD"]
status = True
score = 0
c_score = 0
wicket = 0
c_wicket = 0
ball_list = ["1","2","3","4","5","6","No Ball","Wicket"]

while status :
    
    my_team = input("Enter Your Team Name :").upper()
    c_team = random.choice(team_list)
    print("Computer Team Name :", c_team)
   
    if my_team == c_team :
        print("Both Select Same Team Please Select Diff Team")
    
    print("\n ------------- It's Time for TOSS !!!! -------------\n")
    
    print("TOSS TIME")
    tosslist = ["HEAD", "TAILS"]
    toss_computer = random.choice(tosslist)
    toss = input("Please Select HEAD/TAILS : ").upper()
    
    if toss == toss_computer :
        
        print("You Won Toss")
        toss_select = input("What to want to Chose : BATTING OR BOLLING" ).upper()
        
        if toss_select == "BATTING":
            
            
            
            for i in range(1,7):
                print ("\n---------------------------Press Enter to Start-------------------------------\n ")
                auto_ball = random.choice(ball_list)
                input("Press Enter For Next Ball")
                if auto_ball == "1":
                    score+=1
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")
                    
                elif auto_ball == "2":
                    score+=2
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "3":
                    score+=3
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "4":
                    score+=4
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "5":
                    score+=5
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "6":
                    score+=6
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "Wicket":
                    score+=0
                    wicket+=1
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "No Ball":
                    score+=1
                    wicket+=0
                    i=-1
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Final Score")

            print("Final Score",score,"/",wicket)

        else :
            
            for i in range(1,7):
                print ("\n---------------------------Press Enter to Start-------------------------------\n ")
                auto_ball = random.choice(ball_list)
                input("Press Enter For Next Ball")
                if auto_ball == "1":
                    c_score +=1
                    c_wicket+=0

                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")
                    
                elif auto_ball == "2":
                    c_score+=2
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "3":
                    c_score+=3
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "4":
                    c_score+=4
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "5":
                    c_score+=5
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "6":
                    c_score+=6
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "Wicket":
                    c_score+=0
                    c_wicket+=1
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "No Ball":
                    c_score+=1
                    c_wicket+=0
                    i=-1
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Final Score")

            print("Final Computer Score",c_score,"/",c_wicket)

    else:
        print("You Loss Toss")
        
        c_team_select_list = ["BATTING","BOLLING"]
        c_team_select= random.choice(c_team_select_list)
        print("Computer Select : ",c_team_select)
        
        if c_team_select == "BATTING":
            
            for i in range(1,7):
                print ("\n---------------------------Press Enter to Start-------------------------------\n ")
                auto_ball = random.choice(ball_list)
                input("Press Enter For Next Ball")
                if auto_ball == "1":
                    c_score +=1
                    c_wicket+=0

                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")
                    
                elif auto_ball == "2":
                    c_score+=2
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "3":
                    c_score+=3
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "4":
                    c_score+=4
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "5":
                    c_score+=5
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "6":
                    c_score+=6
                    c_wicket+=0
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "Wicket":
                    c_score+=0
                    c_wicket+=1
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "No Ball":
                    c_score+=1
                    c_wicket+=0
                    i=-1
                    print("Score : ", c_score ,"/",c_wicket)
                    input("Press Enter For Final Score")

            print("Final Computer Score",c_score,"/",c_wicket)
        else:
            
            for i in range(1,7):

                print ("\n---------------------------Press Enter to Start-------------------------------\n ")
                auto_ball = random.choice(ball_list)
                input("Press Enter For Next Ball")
                if auto_ball == "1":
                    score+=1
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "2":
                    score+=2
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "3":
                    score+=3
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "4":
                    score+=4
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "5":
                    score+=5
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "6":
                    score+=6
                    wicket+=0
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "Wicket":
                    score+=0
                    wicket+=1
                    print("Score : ", score ,"/",wicket)
                    input("Press Enter For Next Ball")

                elif auto_ball == "No Ball":
                    score+=1
                    wicket+=0
                    i=-1
                    print("Score : ", score ,"/",wicket)
            input("Press Enter For Final Score")

            print("Final Score",score,"/",wicket)
    print("\n ------------- now sceond team turn -------------\n")



    
    
    choice = input(" Want to Play Again Enter Y for Yes N for No : ")
    if choice == "n" : 
        status = False
    








