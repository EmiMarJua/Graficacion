from PIL import Image
# Abrir imagen
img = Image.open("foto.jpg")
# Guardar en diferentes formatos
img.save("foto.png", "PNG")
img.save("foto.gif", "GIF")
img.save("foto.tiff", "TIFF")