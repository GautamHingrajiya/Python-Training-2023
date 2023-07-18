import os

if os.path.exists("Myfolder"):
    print("Already Folder Created")

else:
    os.mkdir("Myfolder")
    print("Folder Created Sucssesfully")