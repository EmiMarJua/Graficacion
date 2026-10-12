import matplotlib.pyplot as plt

def DDA(x0, y0, x1, y1):
    puntos = []
    dx = x1 - x0
    dy = y1 - y0
    pasos = int(max(abs(dx), abs(dy)))
    x_inc = dx / pasos
    y_inc = dy / pasos
    x, y = x0, y0
    for _ in range(pasos + 1):
        puntos.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return puntos

pts = DDA(2, 3, 15, 8)
xs, ys = zip(*pts)
plt.plot(xs, ys, 'ro-')
plt.title("Línea con algoritmo DDA")
plt.grid(True)
plt.show()
