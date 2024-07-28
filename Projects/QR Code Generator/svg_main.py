import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("hello world !", image_factory=factory)
svg_image.save("svg_qr.svg")
