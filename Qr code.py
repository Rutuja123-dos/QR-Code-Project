import qrcode
from PIL import Image

#when we read PIL we have function called QRcode it changes qrcode functionality like border, version, error, etc
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

#add_data is funct is used to add the data of qrcode
qr.add_data("https://www.linkedin.com/in/rutuja-wagh-649430350/")

# make function is used to create a actual qrcode 
qr.make(fit=True)

# here the fill_colour is used to decide the colour of qr code and back_colour is for background of the image
img=qr.make_image(fill_colour="black",back_colour="white")

# to save image
img.save("linkedin.png")
