import cv2 as cv

# reading an image
dog = cv.imread('images\happydog.jpg')

# getting size of an image
height = dog.shape[0]
width = dog.shape[1]
print('height =' + str(height))
print('width =' + str(width))
cv.imshow('Dog', dog)                    #---------------------showing the image in its original dimensions   

# resizing an image
smallSize = (int(width/4), int(height/4))#---------------------resizing the original image to the quarter of its original size.
dogSmall = cv.resize(dog, smallSize, cv.INTER_LINEAR )
cv.imshow('Resize', dogSmall)

# converting an image to grayscale
dogGrayscale = cv.cvtColor(dog, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', dogGrayscale)



cv.waitKey(0)