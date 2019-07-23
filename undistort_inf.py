import cv2
import numpy as np

#camera matrix for the modified camera (infrared camera)
camera_matrix = np.array([[920.477592, 0.000000, 648.429290], [0.000000, 1027.078406, 425.516900], [0.000000, 0.000000, 1.000000]])
#distortion coefficients vector
distortion_coefficients = np.array([-0.433488, 0.185713, -0.019241, 0.009154, 0.000000])

#number of images to undistort
n = 42

#for loop to undistort and save new images
for i in range (1,n+1):
	if i<10:
		img = cv2.imread("infrared/img_inf0"+str(i)+".jpg")
		dst = cv2.undistort(img, camera_matrix, distortion_coefficients, None, camera_matrix)
		cv2.imwrite("undistorted_inf/undistorted_inf0"+str(i)+".jpg",dst)
	else:
		img = cv2.imread("infrared/img_inf"+str(i)+".jpg")
		dst = cv2.undistort(img, camera_matrix, distortion_coefficients, None, camera_matrix)
		cv2.imwrite("undistorted_inf/undistorted_inf"+str(i)+".jpg",dst)		
