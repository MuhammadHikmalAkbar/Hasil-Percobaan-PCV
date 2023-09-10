import cv2
import copy
import numpy as np
from matplotlib import pyplot as plt


GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)
OrigrayImg = copy.deepcopy(GrayImg)

#Operasi untuk Citra Negatif
Negatif = 255 - GrayImg

#Menampikan Negatif dan Abu Abu 
cv2.imshow ("Citra Negatif", Negatif)
cv2.imshow ("Citra Abu-Abu", GrayImg)

x = np . arange (0 , 256 , 1 , dtype = np . float32 )

#Histogram untuk citra negatif
HistogramNeg = cv2.calcHist([Negatif], [0], None, [256], [0,256])
plt.bar(x, HistogramNeg[:, 0])
plt . title ("Histogram Negatif ", color ="k")
plt.show()

#Histogram untuk Citra Gray
HistogramGray = cv2.calcHist([GrayImg], [0], None, [256], [0,256])
plt.bar(x, HistogramGray[:, 0])
plt . title ("Histogram Gray ",)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()