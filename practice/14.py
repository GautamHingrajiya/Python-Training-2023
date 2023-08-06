sum = 0


def avg():

    global sum
    for i in range(1,6):
        num=int(input("Enter Number :"))
        sum+=num
        avg1 = sum/5

    return avg1

print(avg())