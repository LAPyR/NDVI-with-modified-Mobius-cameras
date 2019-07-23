from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,glob
import math
import numpy as np
from tifffile import imsave

#Read both corrected orthomosaics (red and near-infrared)
red = cv2.imread("float_arrays/calibrated_r.tif",2)
red=red.astype('f4')
infrared = cv2.imread("float_arrays/aligned_nir.tif",2)
infrared= infrared.astype('f4')

#computation of the NDVI:
# NDVI= (nir-r)/(nir+r)
den = infrared + red + 0.000000000000000001 #this to avoid zero denominator if: infrared = red =0 
num= infrared - red
img_ndvi = (num/den)

#Save NDVI image as TIF
imsave('float_arrays/ndvi_corrected.tif',img_ndvi)

