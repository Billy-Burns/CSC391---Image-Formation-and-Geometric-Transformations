import cv2
import numpy as np
import matplotlib.pyplot as plt


original_image = cv2.imread('image_formation/images/original_image.jpg')
transformed_image = cv2.imread('image_formation/images/transformed_image.jpg')

rows, cols = original_image.shape[:2]


pts_orig = np.float32([[0, 0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
pts_trans = np.float32([[300, 100], [900, 500], [800, 1300], [1300, 1500]])



M_perspective = cv2.getPerspectiveTransform(pts_orig, pts_trans)
reverse_engineered = cv2.warpPerspective(original_image, M_perspective, (cols, rows))


orig_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
transformed_rgb = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
reverse_engineered_rgb = cv2.cvtColor(reverse_engineered, cv2.COLOR_BGR2RGB)


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
