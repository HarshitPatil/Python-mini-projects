import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def encodeqr(data, back_color = "white", color = "black"):
    qr = qrcode.QRCode(version=1, box_size=50, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = color, back_color = back_color)
    img.save("myqrcode.png")


def decodeqr(path):
    image = Image.open(path)

    result = decode(image)
    print(result) 


encodeqr("I am a good Boi!")

decodeqr("myqrcode.png")
#during entering path for other images use double back slash or single front slash. 
