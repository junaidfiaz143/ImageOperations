#While processing a video feed, it is important to detect edges in order to recognise certain shapes in an image. 
#Also when we work with depth analysis, it is very important that we understand the video feed, that is a stream of images. 
#This is done by taking gradient in every frame and is the prime focus of this short post.
import cv2

img_name = ""
img = cv2.imread(img_name)

lap = cv2.Laplacian(img, cv2.CV_64F) #here cv2.CV_64F is just the datatype used to create lap
cv2.imshow("Laplace", lap)

sobx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow("sobx", sobx)

soby = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("soby", soby)

edges = cv2.Canny(img, 100, 150) #100, 150 determines the size of the region we want to consider, let’s try with a 150,200 area
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

#https://medium.com/themlblog/image-operations-gradients-and-edge-detection-c4279049a3ad