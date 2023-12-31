import cv2
import time
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

ret, frame = cap.read()
width = int(cap.get(3))
height = int(cap.get(4))

img = cv2.flip(frame, cv2.ROTATE_180)
img = cv2.putText(img, time.ctime(), (0, height - 20), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

# cv2.imshow('frame', img)
name = time.ctime().replace(" ", "_").replace(":", "_") + ".png"
print(name)
cv2.imwrite(name, img)

cap.release()
# cv2.destroyAllWindows()
