import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d .art3d import Poly3DCollection

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#vertice del cubo
#vertices = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0], [0,0,1], [1,0,1], [1,1,1], [0,1,1] ])

#caras = [[vertices[j] for j in [0,1,2,3]],
 #        [vertices[j] for j in [4,5,6,7]],
  #       [vertices[j] for j in [0,1,5,4]],
   #      [vertices[j] for j in [2,3,7,6]],
    #     [vertices[j] for j in [1,2,6,5]],
     #    [vertices[j] for j in [4,7,3,0]]]

#ax.add_collection3d(Poly3DCollection(caras,facecolors = 'skyblue', linewidths = 1, edgecolors = 'black', alpha = 0.7))
#ax.set_title("superificie plana: Cubo 3d")
#plt.show()

# Supericie curva  Esferica

#u = np.linspace(0,2 * np.pi, 50)
#v = np.linspace(0, np.pi, 50)
#x = np.outer(np.cos(u), np.sin(v))
#y =  np.outer(np.sin(u), np.sin(v))
#z = np.outer(np.ones(np.size(u)), np.cos(v))

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#ax.plot_surface(x,y,z, color = 'orange', alpha = 0.8)
#ax.set_title("superificie curva: Esfera")
#plt.show()

# Superficie Curca Cilindrica

#u = np.linspace(0,2 * np.pi, 50)
#v = np.linspace(0, 2, 50)
#U,V =  np.meshgrid(u,v)
#X = np.cos(U)
#Y = np.sin(U)
#Z = V

#fig = plt.figure()
#ax = fig.add_subplot(111, projection = '3d')
#ax.plot_surface(X,Y,Z, color = 'lightgreen', alpha = 0.8)
#ax.set_title("SUperficie Curva: Cilindro")
#plt.show()

