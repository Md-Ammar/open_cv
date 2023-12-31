import cv2
import time

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.flip(frame, cv2.cv2.ROTATE_180)
    img = cv2.putText(img, time.ctime(), (0, height - 20), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

    # img = cv2.line(cv2.cv2.flip(frame, cv2.cv2.ROTATE_180), (0, 0), (width, height), (255, 255, 0), 10)
    # img = cv2.rectangle(img, (100, 100), (200, 200), (100, 100, 100), 10)
    # img = cv2.circle(img, (200, 200), 60, (0, 0, 255), -1)
    # img = cv2.putText(img, "Hello this is ammar", (0, height - 20), font, 2, (0, 0, 0), 1, cv2.LINE_AA)

    # cv2.imshow('frame', img)
    cv2.imwrite("image.png", img)

    time.sleep(1)
    break
    # if cv2.waitKey(1) == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()
