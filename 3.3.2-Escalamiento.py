import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
#xfrom mpl_toolkits.mplot3d.art3d import Poly3DCollection

#Vértices del cubo original
#vertices = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
#[0,0,1], [1,0,1], [1,1,1], [0,1,1]])

# Caras del cubo
#caras = [[0,1,2,3], [4,5,6,7], [0,1,5,4],
#[2,3,7,6], [1,2,6,5], [0,3,7,4]]

# Factores de escala
#Sx, Sy, Sz = 1.5, 0.5, 2.0

# Aplicar escalamiento
#matriz_escala = np.array([[Sx,0,0],
#[0,Sy,0],
#[0,0,Sz]])
#vertices_escalados = vertices.dot(matriz_escala)

# Graficar
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# Cubo original (azul)
#for c in caras:
 #ax.add_collection3d(Poly3DCollection([vertices[c]],
#color='skyblue', alpha=0.5))

# Cubo escalado (rojo)
#for c in caras:
# ax.add_collection3d(Poly3DCollection([vertices_escalados[c]],
#color='salmon', alpha=0.5))
# ax.set_title("Escalamiento 3D: Cubo original (azul) y escalado(rojo)")
 
#ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
#plt.show()

#segundo codigo

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# Crear una malla de puntos para un cubo
#X, Y, Z = np.meshgrid(np.linspace(0, 1, 5),
#np.linspace(0, 1, 5),
#np.linspace(0, 1, 5))

# Escalamiento uniforme
#S1 = np.array([1.5, 1.5, 1.5])
#ax.scatter(X*S1[0], Y*S1[1], Z*S1[2], color='blue', label='Uniforme')

# Escalamiento no uniforme
#S2 = np.array([1.0, 0.5, 2.0])
#ax.scatter(X*S2[0], Y*S2[1], Z*S2[2], color='red', label='No uniforme')

#ax.set_title("Escalamiento uniforme vs. no uniforme")
#ax.legend()
#plt.show()

##Tercer Codigo



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Puntos base
cube = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],
[0,0,1],[1,0,1],[1,1,1],[0,1,1]])

scat = ax.scatter(cube[:,0], cube[:,1], cube[:,2], color='red')

def update(frame):
    S = 1 + frame/20
    scaled = cube * S
    scat._offsets3d = (scaled[:,0], scaled[:,1], scaled[:,2])
    return scat, 
    ani = FuncAnimation(fig, update, frames=20, interval=150)
    ax.set_xlim(0,5); ax.set_ylim(0,5); ax.set_zlim(0,5)
    ax.set_title("Animación: Escalamiento progresivo en 3D")
    
plt.show()


