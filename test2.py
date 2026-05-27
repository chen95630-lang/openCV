import cv2

img = cv2.imread("face_1.jpg")

a = cv2.resize(img, (400, 400))  # resize可設定顯示圖片的大小

cv2.imshow("My Image", a)

cv2.waitKey(0)

cv2.destroyAllWindows()