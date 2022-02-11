from ast import Import
import pyqrcode
import png
from pyqrcode import QRCode

link = "https://www.wikipedia.com"
url = pyqrcode.create(link)
url.png("qrcode.png", scale=6)