import cv2
import copy

GrayImg = cv2.imread("Image.png", cv2.IMREAD_GRAYSCALE)

IMG = copy.deepcopy(GrayImg)
cv2.imshow ("citra linier", IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()