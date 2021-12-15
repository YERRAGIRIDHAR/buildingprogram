import cv2

img = cv2.imread("Moon sinking, sun rising.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2))) # for resizing image
cv2.imshow("G7_image", resized_image) # for disply resized image
cv2.imwrite("G7_image.jpg",resized_image) # for creating resized image
cv2.waitKey(10000) # to hold the displaced image
cv2.destroyAllWindows() # for closing button
