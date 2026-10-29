import numpy as np
import matplotlib.pyplot as plt
# Parámetros
width, height = 800, 600
max_iter = 100
# Rango complejo
x = np.linspace(-2.5, 1.5, width)
y = np.linspace(-1.5, 1.5, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.zeros_like(C)
M = np.full(C.shape, True, dtype=bool)

for i in range(max_iter):
        Z[M] = Z[M]**2 + C[M]
        M[np.abs(Z) > 2] = False
        
plt.imshow(M, extent=(-2.5,1.5,-1.5,1.5),
cmap='magma')
plt.title("Conjunto de Mandelbrot")
plt.xlabel("Re(c)"); plt.ylabel("Im(c)")
plt.show()