import cv2
import numpy as np
import time
from performance_measures import ThinningRate, ThinningSpeed
from name import name

# name = "big_dog.png"
def thinningZS(im):
	img = np.copy(im)
	prev = np.zeros(img.shape,np.uint8)
	while True:
		img = thinningZSIteration(img,0)
		img = thinningZSIteration(img,1)
		diff = np.sum(np.abs(prev-img))
		if not diff:
			break
		prev = img
	return img

def thinningZSIteration(img, iter):
	marker = np.zeros(img.shape,np.uint8);
	for i in range(1,img.shape[0]-1):
		for j in range(1,img.shape[1]-1):
			p2 = img[(i-1),j]
			p3 = img[(i-1),j+1]
			p4 = img[(i),j+1]
			p5 = img[(i+1),j+1]
			p6 = img[(i+1),j]
			p7 = img[(i+1),j-1]
			p8 = img[(i),j-1]
			p9 = img[(i-1),j-1]
			A  = (p2 == 0 and p3) + (p3 == 0 and p4) + (p4 == 0 and p5) + (p5 == 0 and p6) + (p6 == 0 and p7) + (p7 == 0 and p8) + (p8 == 0 and p9) + (p9 == 0 and p2)
			B  = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
			m1 = (p2 * p4 * p6) if (iter == 0 ) else (p2 * p4 * p8)
			m2 = (p4 * p6 * p8) if (iter == 0 ) else (p2 * p6 * p8)
			if (A == 1 and (B >= 2 and B <= 6) and m1 == 0 and m2 == 0):
				marker[i,j] = 1;
	return np.bitwise_and(img,np.bitwise_not(marker))

og_image = cv2.imread(name(), 0)
og_image = (og_image[:,:]>128).astype(np.uint8)
start = time.time()
image = thinningZS(og_image)*255
exec_time = time.time()-start
og_image = og_image*255
final_image = og_image-image
print ("Execution Time For the Image : ", exec_time)

cv2.imshow("cool", final_image)
cv2.waitKey(2000)
cv2.imwrite("Output/"+name()[7:-4]+"_zs.png", final_image)

tr = ThinningRate(image)
op, sp, ts = ThinningSpeed(og_image, image, exec_time)
print ("Name : ", name())
print ("Algo : ZS")
print ("Thinning Rate : ", tr)
print ("Object Points : ", op)
print ("Skeleton Points : ", sp)
print ("Thinning Speed : ", ts)





