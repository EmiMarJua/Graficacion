from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np


img = Image.open("ejemplo2.jpg")
rotada = img.rotate(210) # rota 45 grados

ig, axes = plt.subplots(1, 2)
axes[0].imshow(img); 
axes[0].set_title("Imagen Original"); 
axes[0].axis('off')
axes[1].imshow(rotada); 
axes[1].set_title("Imagen Rotada"); 
axes[1].axis('off')
plt.tight_layout(); 
plt.show()   

