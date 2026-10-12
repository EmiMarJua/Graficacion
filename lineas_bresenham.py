import matplotlib.pyplot as plt

def Bresenham(x0, y0, x1, y1):
    puntos = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        puntos.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return puntos

# Ejemplo
pts = Bresenham(2, 3, 15, 8)
xs, ys = zip(*pts)
plt.plot(xs, ys, "bo-")  # azul con puntos
plt.title("Trazado de línea con Bresenham")
plt.grid(True)
plt.show()
