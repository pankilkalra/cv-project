from algorithms import *
import cv2
import random
  
filename = "img/multiple_obj.png"
im0 = cv2.imread(filename,0)
im = (im0[:,:]>128).astype(np.uint8)

# uncomment according to algo use
# im = thinningZS(im)
im = thinningGH(im)

cv2.imwrite('img/skeletonized.png', im*255)

for i in range(len(im)):
	for j in range(len(im[0])):
		if(im[i][j] == 1):
			im0[i][j] = 0

cv2.imwrite('img/object_with_skeleton.png',im0)