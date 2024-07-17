import qrcode as qr

image = qr.make('https://www.youtube.com/@kaiqueryan7990')
image.save('qrcode_generator/meucanal.png')
