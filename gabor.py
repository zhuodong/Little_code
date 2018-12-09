import numpy as np
import cv2 as cv
import imutils


src_f = 0
kernel_size = 31
pos_sigma = 5
pos_lm = kernel_size-2
pos_th = 0
pos_gam = 100
pos_psi = 90

def Process():
    sig = pos_sigma
    lm = pos_lm+2
    th = pos_th*np.pi/180.
    gm = pos_gam/100.
    ps = (pos_psi-180)*np.pi/180
    print('kern_size=' + str(kernel_size) + ', sig=' + str(sig) + ', th=' + str(th) + ', lm=' + str(lm) +', gm=' + str(gm) + ', ps=' + str(ps))
    kernel = cv.getGaborKernel((kernel_size,kernel_size),sig,th,lm,gm,ps)
    kernelimg = kernel/2.+0.5
    global src_f
    dest = cv.filter2D(src_f, cv.CV_32F,kernel)
    dst = imutils.resize(dest, width=1000)
    cv.imshow('Process window', dst)
    cv.imshow('Kernel', cv.resize(kernelimg, (kernel_size*20,kernel_size*20)))
    cv.imshow('Mag', np.power(dest,2))

def cb_sigma(pos):
    global pos_sigma
    if pos > 0:
        pos_sigma = pos
    else:
        pos_sigma = 1
    Process()

def cb_lm(pos):
    global pos_lm
    pos_lm = pos
    Process()

def cb_th(pos):
    global pos_th
    pos_th = pos
    Process()

def cb_psi(pos):
    global pos_psi
    pos_psi = pos
    Process()

def cb_gam(pos):
    global pos_gam
    pos_gam = pos
    Process()

if __name__ == '__main__':
    image = cv.imread("C:\\Users\\zhuodong\\Desktop\\1271.bmp",1);
    cv.imshow('Src',image)
    src = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #global src_f
    src_f = np.array(src, dtype=np.float32)
    src_f /= 255.
    if not kernel_size%2:
        kernel_size += 1
    cv.namedWindow('Process window',1)
    cv.createTrackbar('Sigma','Process window',pos_sigma,int(kernel_size/2),cb_sigma)
    cv.createTrackbar('Lambda', 'Process window', pos_lm, kernel_size-2, cb_lm)
    cv.createTrackbar('Theta', 'Process window', pos_th, 360, cb_th)
    cv.createTrackbar('gamma', 'Process window', pos_psi, 300, cb_gam)
    cv.createTrackbar('Psi', 'Process window', pos_psi, 360, cb_psi)
    Process()
    cv.waitKey(0)
    cv.destroyAllWindows()
