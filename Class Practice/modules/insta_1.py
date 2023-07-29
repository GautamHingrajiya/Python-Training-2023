import instaloader

name = input("Enter Instagram Id : ")

insta = instaloader.instaloader()

insta.download_profile(name,profile_pic_only=True)

# insta.download_profile(name,profile_pic_only=False)

print("Download Successful !")