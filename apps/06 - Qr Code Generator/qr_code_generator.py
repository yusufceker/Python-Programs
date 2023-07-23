# Import Libraries
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# You can create a qrcode for which website what do you want
s = "www.mebbis.com"
  
# Create qr code
url = pyqrcode.create(s)

# Create a png file on your computer
url.png('mebbis.png',scale=6)
