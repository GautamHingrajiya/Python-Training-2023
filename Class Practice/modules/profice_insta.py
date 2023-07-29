import instaloader

insta_id : input("Enter Instagram Id : ")
a = instaloader.instaloader()
a.download_profile(insta_id,profile_pic_only = True)
print("Download Successfull")