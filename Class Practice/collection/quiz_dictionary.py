quiz = {
    1 : {
        "Que" : "most popular programing language ?",
        "ans" : "python"
    },
    2 : {
        "Que" : "most popular cricketer ?",
        "ans" : "ms dhoni"
    },
    3 : {
        "Que" : "prime minister of india ?",
        "ans" : "narendra modi"
    }
}

score = 0

for i in range (1,len(quiz)+1):
    print(f"Que. {i} {quiz[i]['Que']} ")
    
    ans = input("Enter Your Ans : ").lower()
    if quiz[i]['ans'] == ans:
        score+=50
        print("Right Answer")
    else:
        score-=20
        print("wrong Answer")
print(f"score = {score}")