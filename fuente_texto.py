'''
Rotar y escalar geométricamente el contorno (vector
real)Usa TextPath (convierte el texto a un path
vectorial), y sobre ese se aplica Affine2D (rotación
+ escala + traslación):
'''

import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.transforms import Affine2D
from matplotlib.font_manager import FontProperties

fig, ax = plt.subplots(figsize=(8,4))
ax.set_xlim(-1,10); ax.set_ylim(-2,4)
ax.set_aspect('equal'); ax.axis('off')
fp = FontProperties(weight='bold', size=0.5) 

#fuente base
tp = TextPath((0,0), "GRAFICACIÓN", prop=fp, usetex=False)#genera las palabras
# Transformación geométrica real: rotar 20°, escalar
#1.2x en X y 0.8x en Y, y mover a (1,1)
T = Affine2D().rotate_deg(20).scale(1.2,
0.8).translate(1, 1) + ax.transData

patch = PathPatch(tp, transform=T, facecolor='navy',
edgecolor='none')
ax.add_patch(patch)

plt.title("Texto como vector (rotación + escalado afín)")
plt.show()