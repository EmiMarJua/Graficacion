import matplotlib.pyplot as plt
import math

def plot_point(x, y, c):
    """Dibuja un punto en matplotlib con opacidad proporcional"""
    plt.plot(x, y, 's', color=(0, 0, 0, c), markersize=6)

def fpart(x):
    return x - math.floor(x)

def rfpart(x):
    return 1 - fpart(x)

def XiaolinWu(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steep = abs(dy) > abs(dx)
    
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    
    dx = x1 - x0
    dy = y1 - y0
    gradient = dy / dx if dx != 0 else 1
    
    # primer punto
    xend = round(x0)
    yend = y0 + gradient * (xend - x0)
    xpxl1 = xend
    ypxl1 = math.floor(yend)
    
    if steep:
        plot_point(ypxl1, xpxl1, rfpart(yend))
        plot_point(ypxl1 + 1, xpxl1, fpart(yend))
    else:
        plot_point(xpxl1, ypxl1, rfpart(yend))
        plot_point(xpxl1, ypxl1 + 1, fpart(yend))
    
    # puntos intermedios
    intery = yend + gradient
    for x in range(xpxl1 + 1, int(round(x1))):
        if steep:
            plot_point(math.floor(intery), x, rfpart(intery))
            plot_point(math.floor(intery) + 1, x, fpart(intery))
        else:
            plot_point(x, math.floor(intery), rfpart(intery))
            plot_point(x, math.floor(intery) + 1, fpart(intery))
        intery += gradient

# Dibujar
plt.figure(figsize=(6,4))
XiaolinWu(2, 3, 15, 8)
plt.title("Trazado de línea con Xiaolin Wu (Antialiasing)")
plt.gca().invert_yaxis()
plt.show()
