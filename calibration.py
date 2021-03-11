from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os,glob
import math

import numpy as np
from tifffile import imsave

# Read RGB image of the calibration reflectance panel
im = cv2.imread("crprgb.jpg")   
# Select a ROI from that image
r = cv2.selectROI(im)   
# Crop the RGB image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] 
cv2.imwrite("SelectedArea.jpg",imCrop)
CroppedROI = cv2.imread("SelectedArea.jpg")
avg_color_per_row = np.average(CroppedROI, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)

# Read NIR image of the calibration reflectance panel 
im2 = cv2.imread("crpnir.jpg")    
# Select a ROI from that image
r2 = cv2.selectROI(im2)
# Crop the NIR image
imCrop2 = im2[int(r2[1]):int(r2[1]+r2[3]), int(r2[0]):int(r2[0]+r2[2])]
cv2.imwrite("SelectedArea2.jpg",imCrop2)
CroppedROI2 = cv2.imread("SelectedArea2.jpg")
avg_color_per_row2 = np.average(CroppedROI2, axis=0)
avg_color2 = np.average(avg_color_per_row2, axis=0)

#calculation of the average pixel values of the CRP ROI's (RGB and NIR)
Lvalues = np.array([avg_color.item(0), avg_color.item(1), avg_color.item(2), avg_color2.item(2)], dtype=np.float)
#calculation of average reflectance values of the CRP ROI's 
Pvalues = np.array([0.5457, 0.5453, 0.5428, 0.4863],dtype=np.float)  # B G R NIR
print("   Blue         Green         Red            NIR")
print(Lvalues)

#calculation of the reflectance calibration factor 
Fvalues = Pvalues/Lvalues
print (Fvalues)

#both TIF orthomosaics (rgb and nir) are openned and splitted into individual channels:
#RGB= Red, Green, Blue 
#NIR= x, x, Near-infrared
img = cv2.imread("odm_orthophoto_nor.tif")
img = img.astype(float)
b, g, r = cv2.split(img)
img2 = cv2.imread("odm_orthophoto_inf.tif")
img2 = img2.astype(float)
nir, g2, r2 = cv2.split(img2)

#new empty matrix for corrected reflectance images
rnew = np.zeros((img.shape[0], img.shape[1],1),np.float32)
nirnew = np.zeros((img.shape[0], img.shape[1],1),np.float32)
gnew = np.zeros((img.shape[0], img.shape[1],1),np.float32)
bnew = np.zeros((img.shape[0], img.shape[1],1),np.float32)

#computation of the corrected reflectance values of the image intended to be calibrated (red and near-infrared bands)
rnew= r*Fvalues.item(2)
nirnew= nir*Fvalues.item(3)
bnew= b*Fvalues.item(0)
gnew= g*Fvalues.item(1)


#Save image bands as TIF 
imsave('float_arrays/calibrated_r.tif',rnew.astype(float))
imsave('float_arrays/calibrated_nir.tif',nirnew.astype(float))
imsave('float_arrays/calibrated_g.tif',gnew.astype(float))
imsave('float_arrays/calibrated_b.tif',bnew.astype(float))

# Read corrected orthomosaics (red and near-infrared) now to align both images
calib_r = cv2.imread('float_arrays/calibrated_r.tif',2)   
calib_nir = cv2.imread('float_arrays/calibrated_nir.tif',2) 

calib_r = calib_r.astype('f4')
calib_nir = calib_nir.astype('f4')  

# Find size of image1
sz = rnew.shape
# Define the motion model
warp_mode = cv2.MOTION_TRANSLATION
# Define 2x3 or 3x3 matrices and initialize the matrix to identity
if warp_mode == cv2.MOTION_HOMOGRAPHY :
    warp_matrix = np.eye(3, 3, dtype=np.float32)
else :
    warp_matrix = np.eye(2, 3, dtype=np.float32)
# Specify the number of iterations.
number_of_iterations = 5000;
# Specify the threshold of the increment in the correlation coefficient between two iterations
termination_eps = 1e-10;
# Define termination criteria
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations,  termination_eps)
 
def align_pair(base_im, sec_im, matrix, mode, params):
    # Run the ECC algorithm. The results are stored in warp_matrix.
    (cc, warp_matrix) = cv2.findTransformECC(base_im, sec_im, matrix, mode, params)
    if mode == cv2.MOTION_HOMOGRAPHY :
    # Use warpPerspective for Homography 
        aligned_im = cv2.warpPerspective (sec_im, matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
    else :
    # Use warpAffine for Translation, Euclidean and Affine
        aligned_im = cv2.warpAffine(sec_im, matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP);
    return aligned_im

#alignment is done with this function
im_b_aligned = align_pair(calib_r, calib_nir, warp_matrix, warp_mode, criteria)
#aligned image is saved
imsave('float_arrays/aligned_nir.tif',im_b_aligned.astype(float))
cv2.waitKey(0)
