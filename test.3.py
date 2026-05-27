import cv2

img = cv2.imread("face_1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

a = cv2.resize(gray, (400, 400))

cv2.imshow("My Image", a)

cv2.waitKey(0)

cv2.destroyAllWindows()

