import numpy as np

from PIL import Image

img = Image.open("speed.jpg").convert("L") # escala de grises
arr = np.array(img)#convierte la imagen en un arreglo
negativo = 255 - arr #invierte el color del arreglo

Image.fromarray(negativo).show() 