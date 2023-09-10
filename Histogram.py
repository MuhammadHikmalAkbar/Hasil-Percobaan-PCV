import cv2
import numpy as np
from matplotlib import pyplot as plt

def HistogramGenerator (GrayImg):
    Histogram = np.zeros((256,1), np.int8)
    for i in range (0, GrayImg.shape[0]):
        for j in range (0, GrayImg.shape[1]):
            r = GrayImg[i,j]
            Histogram[r]=Histogram[r]+1
    return Histogram

OriImg = cv2.imread("Image.png", cv2.IMREAD_ANYCOLOR)
GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)

cv2.imshow ("Citra Asli", OriImg)
cv2.imshow ("Citra Abu-Abu", GrayImg)

Histogram = HistogramGenerator(GrayImg)
plt.bar(np.arange(0, 256, 1), Histogram[:, 0])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()