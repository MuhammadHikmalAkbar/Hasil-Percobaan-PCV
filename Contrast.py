import cv2
import numpy as np
from matplotlib import pyplot as plt

def Transform(r,r1,s1,r2,s2):
    s=0 
    if (0<r)&(r<r1):
        s = s1/r1*r 
    elif (r1<=r)&(r<r2): 
        s =(s2-s1) /(r2-r1)*(r-r1)+s1 
    elif (r2<=r)&(r<=255)&(r2<255): 
        s =(255-s2)/(255-r2)*(r-r2)+s2 
    else: 
        s = s2
    s= np.uint8(np.floor(s))
    return  s 

GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)

a = GrayImg.shape[0]
b = GrayImg.shape[1]
im = np.zeros((a,b), np.uint8)

r1 = 25
s1 = 0
r2 = 150
s2 = 255

for i in range(a) :
    for j in range (b):
        r = GrayImg[i,j]
        im[i,j] = Transform(r, r1, s1, r2, s2)
    #end
#end

cv2.imshow('Citra Contrast', im)
cv2.imshow('Citra Asli', GrayImg)

    
Histogram = cv2.calcHist([im], [0], None, [256], [0,256])
plt.bar(np.arange(0, 256, 1), Histogram[:, 0])
plt . title ("Histogram Contrast")
plt.show()

HistogramGray = cv2.calcHist([GrayImg], [0], None, [256], [0,256])
plt.bar(np.arange(0, 256, 1), HistogramGray[:, 0])
plt . title ("Histogram Gray ")
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()

