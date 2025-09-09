import cv2
import numpy as np
import matplotlib.pyplot as plt

original_image = cv2.imread('image_formation/images/original_image.jpg')
transformed_image = cv2.imread('image_formation/images/transformed_image.jpg')

transX = 50
transY = 30
angle = 15
scale = 1.1

rows, cols = original_image.shape[:2]

M_translation = np.float32([[1, 0, transX], [0, 1, transY]])
translated = cv2.warpAffine(original_image, M_translation, (cols, rows))

print(f"Applied translation: tx={transX}, ty={transY}")

M_rotation = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, scale)
rotated = cv2.warpAffine(original_image, M_rotation, (cols, rows))

print(f"Applied rotation: angle={angle}, scale={scale}")

orig_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
transformed_rgb = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
reverse_engineered_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(orig_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(transformed_rgb)
plt.title('Transformed Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(reverse_engineered_rgb)
plt.title('Reverse Engineered Image')
plt.axis('off')

plt.tight_layout()
plt.show()