import cv2

img = cv2.imread("face_1.jpg")

blur = cv2.GaussianBlur(img, (21, 21), 0)

a = cv2.resize(blur, (400, 400))

cv2.imshow("My Image", a)

cv2.waitKey(0)

cv2.destroyAllWindows()

