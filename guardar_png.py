from PIL import Image
img = Image.open("ejemplo_convertido.jpg")
img.save("ejemplo_convertido.png",
"PNG")