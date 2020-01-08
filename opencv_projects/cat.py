import  cv2
import numpy as np
# types of images
image = cv2.imread('cat.jpeg')
cv2.imshow('cat',image)
cv2.waitKey(0)
b,g,r = cv2.split(image)
zeros = np.zeros(image.shape[:2],dtype = 'uint8')
red_image = cv2.merge([zeros,zeros,r])
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('cat', red_image)
cv2.waitKey(0)
#if k == 27:         # wait for ESC key to exit
# cv2.destroyAllWindows()
