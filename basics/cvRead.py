import cv2 as cv
cv.destroyAllWindows()

# reading an image
dog = cv.imread('images\happydog.jpg')

# getting size of an image
height = dog.shape[0]
width = dog.shape[1]
print('height =' + str(height))
print('width =' + str(width))
# cv.imshow('Dog', dog)#--------------------------------------------showing the image in its original dimensions   

# resizing an image
small_size = (int(width/4), int(height/4))#-----------------------resizing the original image to the quarter of its original size.
dog_small_linear = cv.resize(dog, small_size, cv.INTER_LINEAR)#---LINEAR Interpolation
cv.imshow('Resize Linear Interpolation', dog_small_linear)

dog_small_cubic = cv.resize(dog, small_size, cv.INTER_CUBIC)#------CUBIC Interpolation
cv.imshow('Resize Cubic Interpolation', dog_small_cubic)

# converting an image to grayscale
dogGrayscale = cv.cvtColor(dog, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', dogGrayscale)



cv.waitKey(0)