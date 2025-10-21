import qrcode
import os
from datetime import datetime

def generate_qr(name, desc, slogan):
  data= f"Tên: {name}\nMô tả: {desc}\nSlogan: {slogan}"
  qr=qrcode.make(data)

  os.makedirs("data/qrcodes", exist_ok=True)
  filename=f"data/qrcodes/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
  qr.save(filename)
  return filename
