import colorsys # biblioteca de python para convertir colores entre diferenteces modelos
import matplotlib.pyplot as plt

# definicion de los colores HSV

H = 30/360
S = 1.0
V = 1.0

r, g, b = colorsys.hsv_to_rgb(H, S, V)

plt.figure(figsize=(5, 3))
plt.gca().set_facecolor((r, g, b))



plt.xlim = (0, 1)
plt.ylim = (0, 1)
plt.xticks([])
plt.yticks([])
plt.title("Color HSV")
plt.show()