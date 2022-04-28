import os,cv2 as cv,numpy as np
from PIL import Image
def getImageAndLables(path):
    faceSamples=[]
    ids=[]  #储存姓名
    # 储存人脸信息
    imagePaths=[os.path.join(path,f) for f in os.listdir(path) ]
    # 加载分类器
    face_datector = cv.CascadeClassifier(r"C:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml")
    # 遍历列表中的图片
    for imagePath in imagePaths:
        # 打开图片，深度化PIL
        PIL_img=Image.open(imagePath).covert("L")
        img_numpy=np.array(PIL_img,"uint8")
        # 获取人脸特征
        faces = face_datector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = int(os.path.split(imagePath[1].split(".")[0]))
        # 防止wu面容图片
        for x,y,w,h in faces:
            ids.append(id)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            pass
        print("id:",id)
        print("fs:",faceSamples)
        return faceSamples,ids
if __name__ == "__main__":
    path="../face_info/"
    faces,ids=getImageAndLables(path)
    # 加载识别器
    recognizer=cv.face.LBPHFaceRecognizer_create()
    #训练
    recognizer.train(faces,np.array(ids))
    recognizer.write("trainer/trainer.yml")