import cv2 as cv
import os,time

# C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml
#
def resize(img):
    resize_img = cv.resize(img, (200, 200))
    # cv.imshow("face1", resize_img)
    cv.imwrite("resize_face.jpg", img)
    img = cv.imread("resize_face.jpg")
def face_detect_demo():
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect =cv.CascadeClassifier(r"C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")
    face= face_detect.detectMultiScale(gray,1.01,1,10)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        pass
    cv.imshow("result",img)


img =cv.imread("3.JPG")
resize(img)
face_detect_demo()
# os.remove("resize_face.jpg")
# 等待退出
while True:
    if ord("q") == cv.waitKey(0):
        break

cv.destroyAllWindows()
