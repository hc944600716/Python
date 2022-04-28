import cv2 as cvQ
img=cv.imread("1.JPG")
# 显示原图
cv.imshow("face",img)
print("原图大小:",img.shape)
# 修改尺寸
resize_img=cv.resize(img,(200,200))
cv.imshow("face1",resize_img)
cv.imwrite("resize_face.jpg",img)
cv.imshow(" ",resize_img)
# 等待退出
while True:
    if ord("q") == cv.waitKey(0):
        break

cv.destroyAllWindows()