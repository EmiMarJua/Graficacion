import colorsys # biblioteca de python para convertir colores entre diferenteces modelos
import matplotlib.pyplot as plt

# definicion de los colores HSV

H = 250/360
S = 0.80
V = 0.55

r, g, b = colorsys.hsv_to_rgb(H, S, V)

plt.figure(figsize=(5, 3))
plt.gca().set_facecolor((r, g, b))
#configuracion del eje
plt.xlim = (0, 1)
plt.ylim = (0, 1)
#elimina marcas y etiquetas
plt.xticks([])
plt.yticks([])
#establece el titulo
plt.title("Color HSV")
plt.show()