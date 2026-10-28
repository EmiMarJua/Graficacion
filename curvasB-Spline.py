from scipy.interpolate import BSpline
import numpy as np
import matplotlib.pyplot as plt

# Puntos de control
P = np.array([[0, 0], [1, 2], [3, 3], [4, 0],
[5, 2]])
x, y = P[:,0], P[:,1]
# Vector de nudos (para orden k=3)
k = 3
t = np.concatenate(([0,0,0], np.linspace(0,1,len(P)
-k+1), [1,1,1]))
# Curva B-spline
spl_x = BSpline(t, x, k)
spl_y = BSpline(t, y, k)
tt = np.linspace(0,1,100)
curve = np.vstack((spl_x(tt), spl_y(tt))).T
# Visualización
plt.plot(x, y, 'k--o', label='Polígono de control')
plt.plot(curve[:,0], curve[:,1], 'b', label='Curva B-spline')
plt.legend(); plt.axis('equal'); plt.grid(True)
plt.title("Curva B-spline cúbica")
plt.show()
