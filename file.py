import random
import qrcode
import qrcode.constants
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Nos="0123456789"
sym="!@#$%^&*()_-+[]"

allchar = lower + upper + Nos + sym
length=int(input("Enter the length: "))
hello = ''.join(random.choices(allchar, k=length))
print('Generated password:',hello)

data=hello
qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black",back_color="white")
img.save("qrcode.png","PNG")
img.show()