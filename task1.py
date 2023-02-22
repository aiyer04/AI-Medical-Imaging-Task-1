import cv2

def resize(fname, name, width, height):
   image = cv2.imread(fname)
   cv2.imshow(name, image)
   cv2.waitKey(0)
   height, width = image.shape[0:2]

   if width >= height:
    new_image = cv2.resize(image, (width, height))
   else:
    new_image = cv2.resize(image, (height, width))
   return new_image

image1 = cv2.imread('original image 0001.png')
image2 = cv2.imread('T2W 1 masked.png')
image3 = cv2.imread('outline image.png')

cv2.imshow('Original image', image1)
cv2.imshow('Mask overlaid to display only the prostate', image2)
cv2.imshow('Outline of segment', image3)

cv2.waitKey(0)
cv2.destroyAllWindows()



