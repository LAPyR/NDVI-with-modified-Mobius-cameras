import cv2
import numpy as np

#camera matrix for the normal camera (rgb camera)
camera_matrix = np.array([[890.466928, 0.000000, 654.432761], [0.000000, 1001.004648, 430.778816], [0.000000, 0.000000, 1.000000]])
#distortion coefficients vector
distortion_coefficients = np.array([-0.401918, 0.165729, -0.004397, -0.004102, 0.000000])

#number of images to undistort
n = 42

#for loop to undistort and save new images
for i in range (1,n+1):
	if i<10:
		img = cv2.imread("normal/img_nor0"+str(i)+".jpg")
		dst = cv2.undistort(img, camera_matrix, distortion_coefficients, None, camera_matrix)
		cv2.imwrite("undistorted_nor/undistorted_nor0"+str(i)+".jpg",dst)
	else:
		img = cv2.imread("normal/img_nor"+str(i)+".jpg")
		dst = cv2.undistort(img, camera_matrix, distortion_coefficients, None, camera_matrix)
		cv2.imwrite("undistorted_nor/undistorted_nor"+str(i)+".jpg",dst)
