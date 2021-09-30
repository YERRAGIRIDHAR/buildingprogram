import cv2
import time

video =cv2.VideoCapture(0) #Triggering camera

a=0
while True:
    a=a+1
    check, frame= video.read() #first frame of the video
    
    print(check)
    print(frame) #Printing first frame in an array
    print(frame.shape)


    color = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) 
    # time.sleep(3) #Script slept for 3 seconds

    cv2.imshow("Capturing",frame)#created a window with name Capturing name and hoding first frame

    key = cv2.waitKey(1) # wait for 3 seconds and goes for next screen

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()