import RPi.GPIO as GPIO
from gpiozero import LED, Button
from time import sleep
import cv2 
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
#vid2 = cv2.VideoCapture(1)
#vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
vid.set(cv2.CAP_PROP_CONVERT_RGB, False)

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def my_callback(channel):
    cv2.imwrite("/home/pi/Desktop/folder1/1frame%d.jpg" % count, frame)
    #cv2.imwrite("/home/pi/Desktop/folder2/2frame%d.jpg" % count, frame2) 
    #f = open('/home/pi/Desktop/New/{0}{1}.txt'.format('test_text', count), ('w+'))
    #f.close()
    print('rising pulse')
    
count = 0    
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)

    
while True:
     # Capture the video frame 
    # by frame
    ret, frame = vid.read()
    #ret2, frame2 = vid2.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame)
    #cv2.imshow('frame2', frame2) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice
    count = count + 1
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release()
#vid2.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 