import cv2

face_cascade = cv2.CascadeClassifier("face_detection\\haarcascade_frontalface_default.xml") #To read the cascade xml file which has features

img = cv2.imread("face_detection\\chill_pic.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to gray

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor = 1.05,
minNeighbors = 5) # gives you array of face
# 'detectMultiscale'-->search for harrcascade xml file
# 'scaleFactor'--> Down scale the image by 5%
# 'minNeighbors'--> Serach for 5 faces around the window

for x,y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3) #For drawing rectagular box

print(type(faces)) 
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
# cv2.imwrite("photo_modi",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()