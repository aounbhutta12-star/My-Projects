
import qrcode
data=input('Enter The URL Of The Website: ')
filename=input('Enter The Filename: ')

qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black',back_color='red')
image.save(filename)
print(f'QR Code Saved A {filename}')