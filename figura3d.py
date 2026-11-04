#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
# Coordenadas de un cubo
#r = [-1, 1]

#for s, e in [(x,y) for x in r for y in r]:
 #   ax.plot([s, s], [e, e], r, color='b')
    
#ax.set_title("Modelo alámbrico 3D")
#plt.show()

#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
#import numpy as np
#fig = plt.figure()
#ax = fig.add_subplot(111,
#projection='3d')
# Crear puntos de una caja
#X, Y = np.meshgrid(range(2), range(2))
#Z = np.zeros_like(X)
#ax.plot_surface(X, Y, Z, alpha=0.3)
#ax.view_init(30, 45) # Vista isométrica
#ax.set_title("Proyección isométrica")
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#x = np.linspace(-5, 5, 100)
#y = np.linspace(-5, 5, 100)
#X, Y = np.meshgrid(x, y)
#Z = np.sin(np.sqrt(X**2 + Y**2))

#fig = plt.figure()
#ax = fig.add_subplot(111,
#projection='3d')
#ax.plot_surface(X, Y, Z, cmap='viridis')

#ax.set_title("Superficie 3D - Función seno radial")
#plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vértices del cubo
vertices = np.array([[0,0,0], [1,0,0], [1,1,0], [0,1,0],
                    [0,0,1], [1,0,1], [1,1,1], [0,1,1]])
# Caras del cubo (índices)
caras = [[vertices[j] for j in [0,1,2,3]],
        [vertices[j] for j in [4,5,6,7]],
        [vertices[j] for j in [0,1,5,4]],
        [vertices[j] for j in [2,3,7,6]],
        [vertices[j] for j in [1,2,6,5]],
        [vertices[j] for j in [4,7,3,0]]]

ax.add_collection3d(Poly3DCollection(caras,
facecolors='skyblue', linewidths=1,
edgecolors='k', alpha=0.7))
ax.set_title("Superficie plana: Cubo 3D")
plt.show()