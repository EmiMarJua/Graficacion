import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Vértices del cubo
vertices = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
                    [0,0,1],[1,0,1],[1,1,1],[0,1,1]])

caras = [[0,1,2,3],[4,5,6,7],[0,1,5,4],
        [2,3,7,6],[1,2,6,5],[0,3,7,4]]

# Matriz de sesgado (shear en X respecto a Y)
sh_xy = 0.5
sh_matrix = np.array([[1, sh_xy, 0],[0, 1, 0],[0, 0, 1]])

# Aplicar transformación
vertices_sesgados = vertices.dot(sh_matrix)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Cubo original (azul)
for c in caras:
    ax.add_collection3d(Poly3DCollection([vertices[c]], color='skyblue', alpha=0.5))
    
# Cubo sesgado (rojo)
for c in caras:
    ax.add_collection3d(Poly3DCollection([vertices_sesgados[c]], color='salmon', alpha=0.6))
    
ax.set_title("Sesgado 3D: Cubo original (azul) y sesgado (rojo)")
ax.set_xlabel("Eje X"); 
ax.set_ylabel("Eje Y");
ax.set_zlabel("Eje Z")
plt.show()
    


