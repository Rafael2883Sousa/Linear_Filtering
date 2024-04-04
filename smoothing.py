import cv2 as cv

img = cv.imread('Images/cat_1.jpg')
cv.imshow('Img', img)

# Averaging
average = cv.blur(img, (3, 3))
# kernel size specify the center point on each surrounding pixel given the parameter (nxn)
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)