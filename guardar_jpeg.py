from PIL import Image   

img = Image.open("ejemplo.png")
img.save("ejemplo_convertido.jpg", "JPEG", quality=200)
