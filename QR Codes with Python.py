import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8)

#To generate QR Codes with Python you need to install only one Python library for this task:

#pip install pyqrcode
