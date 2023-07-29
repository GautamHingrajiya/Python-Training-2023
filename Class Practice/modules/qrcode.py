import qrcode
img = qrcode.make("https://www.tops-int.com/")
img.save("tops.png")