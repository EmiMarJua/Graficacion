import matplotlib.pyplot as plt
import numpy as np
# Triángulo original
tri = np.array([[0,0], [1,0], [0.5,1], [0,0]])
# Traslación
#tx, ty = 2, 1
#tri_t = tri + [tx, ty]
#plt.plot(tri[:,0], tri[:,1], 'g-', label="Original")
#plt.plot(tri_t[:,0], tri_t[:,1], 'k--', label="Trasladado")
#plt.legend(); plt.axis('equal'); plt.grid(True)
#plt.title("Traslación de un triángulo")
#plt.show()

#sx, sy = 2, 0.5
#tri_s = tri * [sx, sy]
#plt.plot(tri[:,0], tri[:,1], 'o-', label="Original")
#plt.plot(tri_s[:,0], tri_s[:,1], 'g--', label="Escalado")
#plt.legend(); plt.axis('equal'); plt.grid(True)
#plt.title("Escalamiento de un triángulo")
#plt.show()

theta = np.radians(210)
rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
[np.sin(theta), np.cos(theta)]])
tri_r = tri @ rot_matrix.T
plt.plot(tri[:,0], tri[:,1], 'o-', label="Original")
plt.plot(tri_r[:,0], tri_r[:,1], 'or--', label="Rotado 210°")
plt.legend(); plt.axis('equal'); plt.grid(True)
plt.title("Rotación de un triángulo")
plt.show()
