import cv2
import cv2 as cv,os,time
# haarcascade_frontalface_default.xml
# 图片大小调整
def save_img():
    num=1
    flag=1
    cpa=cv.VideoCapture(0)
    while (cap.isOpened()):
        re_flag,Vshow =cap.read()
        k=cv2.waitKey(1)
        if k== ord("k"):
            cv.imwrite("./face/"+str(num)+".name"+".jpg",Vshow)
            print("成功保存图片"+str(num)+".jgp")
            print("..........................................")
            num+=1
        elif k==ord("q"):
            break

def resize(img):
    resize_img = cv.resize(img, (20, 20))
    # cv.imshow("face1", resize_img)
    cv.imwrite("resize_face.jpg", img)
    img = cv.imread("resize_face.jpg")
def face_detect_demo(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect =cv.CascadeClassifier(r"C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
    face= face_detect.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        pass
    resize(img)
    # time.sleep(60)
    #
    cv.imshow("result",img)
    os.remove("resize_face.jpg")

# 视频读取
cap = cv.VideoCapture(0)
# 循环获取
while True:
    flag,frame =cap.read()
    if not flag:
        break
        pass

    face_detect_demo(frame)
    if ord("q") ==cv.waitKey(0):
        break
        pass
cv.destroyAllWindows()
cap.release()