import cv2 as cv
img = cv.imread("1.JPG")
resize_img=cv.resize(img,(200,200))
x,y,w,h =100,100,100,100
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
face_detect = cv.CascadeClassifier("C:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml")
face = face_detect.detectMultiScale(gray_img)
for x, y, w, h in face:
    cv.rectangle(img, (x + y), (x + w, y + h), color=(0, 0, 255), thickness=2)
# cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=1)
cv.imshow("re.img",img)
# 等待退出
while True:
    if ord("q") == cv.waitKey(0):
        break

cv.destroyAllWindows()