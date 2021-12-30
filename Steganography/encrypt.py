#encoding
from LSBSteg import *

steg = LSBSteg(cv2.imread("Attack_image.jpg"))
img_encoded = steg.encode_text(" I Love coding in Python")
cv2.imwrite("my_new_image.png", img_encoded)