import qrcode

# import qrcode.constants

features = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=40,
    border=2,
)
features.add_data("https://pypi.org/project/qrcode/")
features.make(fit=True)
img = features.make_image(fill_color="red", back_color="white")
img.save("image.png")