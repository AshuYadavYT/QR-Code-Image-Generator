import pyqrcode
from pyqrcode import QRCode
import secrets


def qrstart():
    print("Hello There\nThis is QR Image Generator.\nEnter any link to create QR Code")
    link = input("Link: ")
    
    def qr_generate():
        url = pyqrcode.create(link)
        qr_img = f"qrimages/{secrets.token_urlsafe(6)}.png"
        url.png(qr_img, scale=6)
        print(f"You're QR Image is saved in qrimages folder")
    qr_generate()

qrstart()