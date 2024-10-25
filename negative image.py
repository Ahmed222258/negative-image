import cv2
import numpy as np


image=cv2.imread('img/image.png')
NegativeImage=255-image
cv2.imshow("NImag",NegativeImage)