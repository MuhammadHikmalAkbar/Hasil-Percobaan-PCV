import cv2
import copy
import numpy as np
from matplotlib import pyplot as plt


GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)
OrigrayImg = copy.deepcopy(GrayImg)
GrayImg_float = (GrayImg.astype(np.double)) / 255

Intensity = float(100) / 255 #Changeable

BrightIMG = GrayImg_float + Intensity

print (BrightIMG)

if (BrightIMG > 1).any() :
    BrightIMG [BrightIMG > 1] = 1

BrightIMG_int8 = (BrightIMG*255).astype(np.uint8)

cv2.imshow ("Gray Image Ori", OrigrayImg)
cv2.imshow ("Brighness", BrightIMG_int8)

x = np . arange (0 , 256 , 1 , dtype = np . float32 )
HistogramBright = cv2.calcHist([BrightIMG_int8], [0], None, [256], [0,256])
plt.bar(x, HistogramBright[:, 0])
plt . title ("Histogram bright ", color ="k")
plt.show()


HistogramGray = cv2.calcHist([GrayImg], [0], None, [256], [0,256])
plt.bar(x, HistogramGray[:, 0])
plt . title ("Histogram Gray ",)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()