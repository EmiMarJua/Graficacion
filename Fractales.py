import matplotlib.pyplot as plt
import numpy as np
def sierpinski(p1, p2, p3, level):
    if level == 0:
        x = [p1[0], p2[0], p3[0], p1[0]]
        y = [p1[1], p2[1], p3[1], p1[1]]
        plt.plot(x, y, 'r')
    else:
        mid12 = (p1 + p2) / 2
        mid23 = (p2 + p3) / 2
        mid31 = (p3 + p1) / 2
        sierpinski(p1, mid12, mid31, level-1)
        sierpinski(mid12, p2, mid23, level-1)
        sierpinski(mid31, mid23, p3, level-1)

p1 = np.array([0, 0])
p2 = np.array([1, 0])
p3 = np.array([0.5, np.sqrt(3)/2])
plt.figure(figsize=(6,6))
sierpinski(p1, p2, p3, 5)
plt.axis('equal'); 
plt.axis('off')
plt.title("Triángulo de Sierpiński")
plt.show()