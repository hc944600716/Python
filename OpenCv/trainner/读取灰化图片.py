import cv2 as cv
# 导入图
img = cv.imread("1.JPG")
# 灰度转换
# 查看图片
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 查看灰度照片
cv.imshow("grey",gray_img)
# 保存灰化图片
cv.imwrite("grey_face1.jpg",img)
cv.imshow("face1",img)
# 等待
cv.waitKey(0)
# 内存释放
cv.destroyAllWindows()