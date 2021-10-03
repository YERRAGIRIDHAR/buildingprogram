from datetime import datetime
import cv2, time
import pandas

first_frame = None
status_list =[None, None] #recording the movement of an object moved 1 or moving 0
times = []
df = pandas.DataFrame(columns=["Start", "End"]) # To record the data

video = cv2.VideoCapture(0) #Triggering camera

while True:
    check,frame = video.read() #first frame of the video
    status = 0


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0) #To in increas the accuracy

    if first_frame is None:
        first_frame  = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame,gray) #comparing first frame and blured image gray
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] #Black and white image
    thresh_frame = cv2.dilate(thresh_frame, None, iterations= 2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #Finding the points for moving objet

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        
        (x,y ,w,h) =cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),3) # Joing the points in rectangular shape
    status_list.append(status)


    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())#recording the time when stsus changes from 1 to 0
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())#recording the time when stsus changes from 0 to 1

    cv2.imshow("Gray", gray) #created a window with name Capturing name and hoding first frame
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame",  frame)


    key = cv2.waitKey(1) #wait for 3 seconds and goes for next screen
    # print(gray)
    # print(delta_frame)

    if key == ord('q'):
        if status ==1:
            times.append( datetime.now()) #To record exit time
        break 


    print(status_list)
    print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows