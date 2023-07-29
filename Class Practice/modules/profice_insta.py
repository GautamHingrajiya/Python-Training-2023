import instaloader

insta_id = input("Enter Instagram Id : ")
insta = instaloader.Instaloader()
insta.download_profile(insta_id,profile_pic_only = False)
print("Download Successfull")