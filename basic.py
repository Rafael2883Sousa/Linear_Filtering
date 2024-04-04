import cv2 as cv

img = cv.imread('Images/cat_1.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur (removes noises that exist in a image)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (canny detector)
canny = cv.Canny(blur, 125, 175)  # edges present in the image
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
#cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
#cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# Cropping
cropped = img[50: 200, 200:400]
#cv.imshow('Cropped', cropped)

cv.waitKey(0)