import cv2
import numpy as np
from matplotlib import pyplot as plt


OriImg = cv2.imread("Image.png", cv2.IMREAD_ANYCOLOR)
GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow ("Citra Asli", OriImg)
cv2.imshow ("Citra Abu-Abu", GrayImg)

Histogram = cv2.calcHist([GrayImg], [0], None, [256], [0,256])
plt.bar(np.arange(0, 256, 1), Histogram[:, 0])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()