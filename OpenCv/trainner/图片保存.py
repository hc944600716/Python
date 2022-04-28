import cv2 as cv
num=1
flag=1
cap=cv.VideoCapture(0)
while (cap.isOpened()):
    re_flag,Vshow =cap.read()
    cv.imshow("capture_img",Vshow)
    k=cv.waitKey(1)
    if k== ord("k"):
        name=input("请输入录入人脸姓名：")
        cv.imwrite(r"C:\Code\opencv\face_info/"+str(num)+"."+name+".jpg",Vshow)
        print("成功保存图片"+str(num)+".jgp")
        print("..........................................")
        num+=1
    elif k==ord("q"):
        break
cv.destroyAllWindows()
cap.release()