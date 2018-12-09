
import cv2
import numpy as np
from skimage import  exposure

def adjust_gamma_img(image, k):#对比度
    # k = [0,1],调亮  k 大于1，变暗
    gam1 = exposure.adjust_gamma(image, k)
    save_images(gam1,"gamma" +str(k))

def save_images(images_data, win_name):
        path = "G:/PyCharm/duanqiezhan/duan/pic_extend_data/"+ win_name +'.jpg'
        #print('path',path)
        #cv2.imshow( win_name,images_data)
        cv2.imwrite(path,images_data)

# 定义旋转Rot函数
def rotate(image, x):
    rows, cols, _ = image.shape
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), x, 1)
    shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    path = "Rot_" + str(x)
    save_images(shifted, path)
    """
    # x轴的剪切shear变换，角度45°
    theta = 45 * np.pi / 180
    M_shear = np.array([
        [1, np.tan(theta), 0],
        [0, 1, 0]
    ], dtype=np.float32)
    img_sheared = cv2.warpAffine(img, M_shear,(img.shape[1], img.shape[0]))
    cv2.imshow('img_sheared.jpg', img_sheared)

    # 顺时针旋转，角度45°
    M_rotate = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0]
    ], dtype=np.float32)

    img_rotated = cv2.warpAffine(img, M_rotate, (img.shape[1], img.shape[0]))
    cv2.imshow('img_rotated.jpg', img_rotated)
    """

def contrast_demo(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, chunnel = img1.shape
    blank = np.zeros([rows, cols, chunnel], img1.dtype)  # np.zeros(img1.shape, dtype=uint8)
    dst = cv2.addWeighted(img1, c, blank, 1 - c, b)
    cv2.imshow("con_bri_demo", dst)
    save_images(dst,"con_bri_demo")


if __name__=="__main__":
    img = cv2.imread('pic/1.png')
    img = cv2.resize(img,(224,224),interpolation=cv2.INTER_LINEAR)
    cv2.imshow("org",img)
    save_images(img,"1_Org.jpg")
    #旋转
    rotate(img,90)
    #rotate(img, 180)
    rotate(img, 270)
    #翻转
    # 水平翻转
    flip_horiz_img = cv2.flip(img, 1)
    save_images(flip_horiz_img,"horiz")
    # 垂直翻转
    flip_verti_img = cv2.flip(img, 0)
    save_images(flip_verti_img,"verti")
    # 水平垂直翻转
    flip_horver_img = cv2.flip(img, -1)
    save_images(flip_horver_img,"hor_ver")

    #调整对比度
    adjust_gamma_img(img,0.5)
    adjust_gamma_img(img, 0.7)
    adjust_gamma_img(img, 1.2)
    adjust_gamma_img(img, 1.5)
    #调整亮度
    contrast_demo(img, 1.3, 3)

    cv2.waitKey(0)


