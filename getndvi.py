from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os,glob
import math
import numpy as np
from tifffile import imsave

#Read the tif images related to the orthomosaic's bands (near-infrared, red, green, and blue)
red = cv2.imread("float_arrays/calibrated_r.tif",2)
red = red.astype('f4')
infrared = cv2.imread("float_arrays/aligned_nir.tif",2)
infrared = infrared.astype('f4')
green = cv2.imread("float_arrays/calibrated_g.tif",2)
green = green.astype('f4')
blue = cv2.imread("float_arrays/calibrated_b.tif",2)
blue = blue.astype('f4')

non_zero_div_term = 0.000000000000000001 #term to avoid division / 0

#computation of the NDVI:
# NDVI= (nir-r)/(nir+r)
den = infrared + red + non_zero_div_term
num= infrared - red
img_ndvi = (num/den)
#Save NDVI image as TIF
imsave('float_arrays/ndvi.tif',img_ndvi)

#computation of the GCI:
# GCI = (NIR / G) - 1
img_gci = (infrared / (green + non_zero_div_term)) - 1.0 
#Save GCI image as TIF
imsave('float_arrays/gci.tif',img_gci)

#computation of the VARI:
# VARI = (G - R) / (G + R - B)
img_vari = (green - red) / (green + red - blue + non_zero_div_term)
#Save VARI image as TIF
imsave('float_arrays/vari.tif',img_vari)

#computation of the EVI:
# EVI = C * (NIR - R) / (NIR + (c1 * R - c2 * B) + L) with:
C = 2.5
c1 = 6.0
c2 = 7.5 
L = 1.0
img_evi = C * (infrared - red) / (infrared + (c1 * red - c2 * blue) + L + non_zero_div_term)
#Save EVI image as TIF
imsave('float_arrays/evi.tif',img_evi)

#computation of the OSAVI:
# OSAVI = (NIR - R) / (NIR + R + J) with:
J = 0.16
img_osavi = (infrared - red) / (infrared + red + J + non_zero_div_term)
#Save OSAVI image as TIF
imsave('float_arrays/osavi.tif',img_osavi)

# MCARI1 = 1.2(2.5(NIR-R)-1.3(NIR-G)) with:
img_mcari1 = 1.2 * (2.5 * (infrared-red)-1.3*(infrared-green))
#Save MCARI1 image as TIF
imsave('float_arrays/mcari1.tif',img_mcari1)

# GVI = R- G / (R+ G)
img_gvi = (red - green) / (red + green + non_zero_div_term)
#Save gvi image as TIF
imsave('float_arrays/gvi.tif',img_gvi)

