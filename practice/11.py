import random

list1 = ["RED","GREEN","YELLOW","GREEN"]

light= random.choice(list1)

if light == "RED":
    print("Stop")
elif light == "YELLOW" :
    print("Stop and Then Go")
else:
    print("Go")