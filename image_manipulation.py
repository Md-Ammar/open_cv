import cv2

img = cv2.imread('assets/img.jpg', -1)
print(img.shape)

#cpoying pixels

tag = img[0:200, 800:1200]
img[0:200, 0:400] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()