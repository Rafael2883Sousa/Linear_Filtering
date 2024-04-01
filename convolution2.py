import cv2
import numpy as np

img = cv2.imread('Images/cat_1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Img', img)
cv2.imshow('Gray', gray)

def conv(img, kernel):

    img_h = img.shape[0]
    img_w = img.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h//2 # to get integer value
    w = kernel_w//2

    img_conv = np.zeros(img.shape)

    for i in range(h, img_h-h):
        for j in range(w, img_w-w):
            sum = 0

            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum += kernel[m, n] * img[i - h + m, j - w + n]

            img_conv[i, j] = sum
    return img_conv

kernel = np.ones((3, 3), dtype=np.float32) / 1000
img_convolution = conv(gray, kernel)

cv2.imshow('Img Convolved', img_convolution)
cv2.waitKey(0)
