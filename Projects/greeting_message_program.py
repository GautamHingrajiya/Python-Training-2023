# greeting message program

import time
timestamp = time.strftime("%H:%M:%S")
hours = int(time.strftime("%H"))
minuts = int(time.strftime("%M"))
seconds = int(time.strftime("%S"))

# hours = int(input("etern hours"))     # manual input for checking

if hours >=0 and hours <5 :
    print("good night sir")
elif hours >=5 and hours <11 :
    print("good mornig sir")
elif hours>=11 and hours <14 :
    print("good noon sir")
elif hours >=14 and hours <19 :
    print("good afternoon sir")
elif hours>=19 and hours <22 :
    print("good evening sir")
else :
    print("good night sir")

