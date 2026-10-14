from PIL import Image, ImageFilter

img = Image.open("ejemplo2.jpg")
suave = img.filter(ImageFilter.BLUR)
suave.show()