import cv2

image1 = cv2.imread('original image 0001.png')
image2 = cv2.imread('T2W 1 masked.png')
image3 = cv2.imread('outline image.png')

cv2.imshow('Original image', image1)
cv2.imshow('Segment that displays only the prostate', image2)
cv2.imshow('Outline on region of interest', image3)

cv2.waitKey(0)

cv2.destroyAllWindows("Original image")
cv2.destroyAllWindows("Segment that displays on the prostate")
cv2.destroyAllWindows("Outline on region of interest")