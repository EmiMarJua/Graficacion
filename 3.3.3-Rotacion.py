import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation

# Vértices del cubo
#vertices = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
 #                   [0,0,1],[1,0,1],[1,1,1],[0,1,1]])

#caras = [[0,1,2,3],[4,5,6,7],[0,1,5,4],
 #       [2,3,7,6],[1,2,6,5],[0,3,7,4]]

# Ángulo de rotación (en radianes)
#theta = np.radians(45)

#Rx = np.array([[1,0,0],
 #               [0,np.cos(theta),-np.sin(theta)],
  #              [0,np.sin(theta),np.cos(theta)]])
#Ry = np.array([[np.cos(theta),0,np.sin(theta)],
 #           [0,1,0],
  #          [-np.sin(theta),0,np.cos(theta)]])
#Rz = np.array([[np.cos(theta),-np.sin(theta),0],
 #           [np.sin(theta),np.cos(theta),0],
  #          [0,0,1]])

# Aplicar rotación combinada
#vertices_rotados = vertices.dot(Rx).dot(Ry).dot(Rz)

# Graficar
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# Cubo original (azul)
#for c in caras:
 #   ax.add_collection3d(Poly3DCollection([vertices[c]], color='skyblue', alpha=0.5))
    
# Cubo rotado (rojo)
#for c in caras:
 #   ax.add_collection3d(Poly3DCollection([vertices_rotados[c]],color='salmon', alpha=0.5))
    
#ax.set_title("Rotación 3D: Cubo original (azul) y rotado (rojo)")
#ax.set_xlabel("Eje X"); ax.set_ylabel("Eje Y"); ax.set_zlabel("Eje Z")
#plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vértices del cubo
cube = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
                [0,0,1],[1,0,1],[1,1,1],[0,1,1]])
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)]
lines = [ax.plot([], [], [], color='red')[0] for _ in edges]

def update(frame):
    theta = np.radians(frame)
    Ry = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
    rot = cube.dot(Ry)

    for i, e in enumerate(edges):
        lines[i].set_data(rot[e,0], rot[e,1])
        lines[i].set_3d_properties(rot[e,2]) 
        
        return lines

ani = FuncAnimation(fig, update, frames=range(0,360,5), interval=100, blit=True)
ax.set_xlim(-2,2); 
ax.set_ylim(-2,2); 
ax.set_zlim(-2,2)
ax.set_title("Animación: Rotación continua sobre el eje Y")
plt.show()



