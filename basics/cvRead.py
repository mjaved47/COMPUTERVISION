import cv2 as cv

# reading an image
dog = cv.imread('images\happydog.jpg')
cv.imshow('Dog', dog)

# converting an image to grayscale
dogGrayscale = cv.cvtColor(dog, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', dogGrayscale)

cv.waitKey(0)