import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises

img = cv2.imread("ejemplo2.jpg", cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Sobel en X y Y

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Magnitud del gradiente

sobel = cv2.magnitude(sobel_x, sobel_y)

# Mostrar resultados

plt.subplot(1,3,1), plt.imshow(img, cmap="gray"), plt.title("Original")
plt.subplot(1,3,2), plt.imshow(sobel_x, cmap="gray"),
plt.title("Sobel X")
plt.subplot(1,3,3), plt.imshow(sobel_y, cmap="gray"),
plt.title("Sobel Y")
plt.show()