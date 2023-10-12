import pyqrcode
from pyqrcode import QRCode
s = "image.jpeg"
img = pyqrcode.create(s)
img.svg("NewQRCode.svg", scale=10)