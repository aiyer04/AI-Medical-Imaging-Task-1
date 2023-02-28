import cv2
import nibabel as nb
from pathlib import Path
from pprint import pprint
import numpy as np
from matplotlib import pyplot as plt
from nilearn import plotting as nlp
from scipy import ndimage as ndi
import nibabel.testing

data_dir = Path('/Users/IyerFamMac/Desktop')

fig = plt.figure(figsize=(10,7))
rows = 1 
columns = 3

img1 = nb.load(data_dir / 'opencv_project/original image.nii.gz').get_fdata()
img1.shape
test = img1[:,:,10]

img2 = nb.load(data_dir / 'opencv_project/Volume.nii.gz').get_fdata()
img2.shape
test1 = img2[:,:,10]

img3 = cv2.imread('Mask overlay.png')

fig.add_subplot(rows, columns, 1)
plt.imshow(ndi.rotate(test, 270), cmap='gray')
plt.axis('off')
plt.title('Original Image')

fig.add_subplot(rows, columns, 2)
plt.imshow(ndi.rotate(test1, 270), cmap='gray')
plt.axis('off')
plt.title('Overlaid Mask')

fig.add_subplot(rows, columns, 3)
plt.imshow(img3, cmap='gray')
plt.axis('off')
plt.title('Outlined Region')

plt.show()