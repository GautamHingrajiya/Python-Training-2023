import pyttsx3
engine = pyttsx3.init() # object creation
status = True
rate=0
while status == True:
    voice1 = input("Enter You Want to Speak : ")
    engine.setProperty('rate', 105)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    # print (volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

    engine.say(voice1)
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(voice1, 'test.mp3')
    # engine.runAndWait()

check = input("Do you want to Continue ? Press Y for yes or N of no : ")

if check == 'y' or check =="yes":
    status= True
else:
    status= False