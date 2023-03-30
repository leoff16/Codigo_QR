import qrcode

input = 'https://instagram.com/novillos_cerveceria?igshid=YmMyMTA2M2Y='

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black',back_color='white')
img.save('qr_novilloff.png')