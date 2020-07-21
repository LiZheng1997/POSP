
import cv2
import matplotlib.pyplot as plt
#载入原图
img_original=cv2.imread('/home/lizheng/Documents/Pick_Out_Single_package/data/test_data/0003_Color.png',0)
# change the image to bgr if the raw one is bgr format
bgr_image = cv2.cvtColor(img_original.copy(), cv2.COLOR_RGB2BGR)
#高斯滤波
img_blur=cv2.GaussianBlur(bgr_image,(5,5),5)
# covert the image to gray
color_image = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
sub_mask = backsub.apply(bgr_image.copy())

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
th = cv2.threshold(sub_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
eroded = cv2.erode(th, es, iterations=3)
dilated = cv2.dilate(eroded, es, iterations=1)  # 形态学
#自适应阈值分割
# img_thresh=cv2.adaptiveThreshold(img_original,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,3)
# img_thresh_blur=cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,3)
#显示图像
imgs=[img_thresh,img_thresh_blur,img_original]
titles=['img_thresh','img_thresh_blur', 'raw_image']
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
