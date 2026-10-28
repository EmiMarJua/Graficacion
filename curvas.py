import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
# Puntos de control
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 3, 1, 4, 2, 5])

# Interpolación cúbica
spl = make_interp_spline(x, y, k=3)
x_new = np.linspace(0, 5, 200)
y_new = spl(x_new)
# Visualización
plt.plot(x, y, 'ko--', label="Puntos de control")
plt.plot(x_new, y_new, 'r', label="Curva interpolada")
plt.legend(); 
plt.title("Trazo de línea curva mediante interpolación cúbica")
plt.grid(True); 
plt.axis('equal')
plt.show()