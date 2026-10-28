import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Puntos de control
P = np.array([[0, 0], [1, 2], [3, 3], [4, 0]])

# Cálculo de la curva Bézier

def bezier_curve(P, n=100):
    t= np.linspace(0,1,n)
    n_points = len(p) - 1
    curve = np.zeros((n, 2))
    for i in range(n_points + 1): 
        b = comb(n_points, i) * ((1 - t) ** \
            (n_points - i)) * (t ** i)
        curve += np.outer(b, P[i])
    return curve

# Curva y visualización
curve = bezier_curve(P)
plt.plot(P[:,0], P[:,1], 'k--o', label='Polígono de control')
plt.plot(curve[:,0], curve[:,1], 'r', label='Curva Bézier')
plt.legend(); 
plt.axis('equal'); 
plt.grid(True)
plt.title("Curva Bézier cúbica")
plt.show()