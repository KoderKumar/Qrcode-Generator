import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=11, border=3)
qr.add_data("https://medium.com/@coderarth")

qr.make(fit=True)
img = qr.make_image(back_color="#FDFAF3")
img.save("qrgen.png")
