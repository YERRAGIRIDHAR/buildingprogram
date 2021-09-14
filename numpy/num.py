'''numpy'''

import numpy
n = numpy.arange(27)
print(n.reshape(3,3,3))
print("............................")
a=[[123,43,56,98],[],[]]
print(type(a))
print(a)

'''Creating an ndarray'''

b=numpy.array([a])
print(b)
print("..........")

'''converting image into numpy array'''

import cv2
im_g=cv2.imread("smallgray.png",0)
print(im_g)
print(".....................")

'''create an image from taken array'''

a = [[187, 158, 104, 121, 143,543,132,54,231],
     [198, 125, 255, 255, 147,324,154,24,432],
     [209, 134, 255,  97, 182,76,765,345,425,]]
a1 = numpy.asarray(a)
# print(a1)
# print(a1.reshape(3,3,3))
# import cv2
a3=cv2.imwrite("lion1.jpg", a1)
print(a3)
print("...............")

'''indexing, slicing, Iterating'''

img=cv2.imread("smallgray.png",0)
img2=img[0:2]
img3=img[0:2, 2:4]
img4=img[:,2:4]
print(img2)
print('.......')
print(img3)
print('.......')
print(img4)
print(".................")
for i in img:
    print(i)
print(".......................")
for i in img.T:
    print(i)
print('.......')
for i in img.flat:
    print(i)
print("....................")

'''stacking, splitting'''

img1 = numpy.hstack([img,img,img])
print(img1)
print("...........")
img2 = numpy.vstack([img,img,img])
print(img2)
print(".....................")
img3 = numpy.hsplit(img2,5)
print(img3)
print("..............")
img4 = numpy.vsplit(img2,3)
print(img4)
print("...........")
img5 = numpy.vsplit(img2,3)
print(img5[0])