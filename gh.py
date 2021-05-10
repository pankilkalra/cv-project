import cv2
import numpy as np
import time
from performance_measures import ThinningRate, ThinningSpeed
from name import name

# name = "big_dog.png"
def thinningGHIteration(img, iter):
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
			c = (p2==0 and (p3 or p4)) + (p4==0 and (p5 or p6)) + (p6==0 and (p7 or p8)) + (p8==0 and (p9 or p2))
			n1 = (p9 or p2) + (p3 or p4) + (p5 or p6) + (p7 or p8)
			n2 = (p2 or p3) + (p4 or p5) + (p6 or p7) + (p8 or p9)
			if(n1 < n2):
				n = n1
			else:
				n = n2
			if(iter == 0):
				m = ((p6 or p7 or p9==0) and p8)
			else:
				m = ((p2 or p3 or p5==0) and p4)
			if(c == 1 and (n>=2 and n<=3) and m==0):
				marker[i][j] = 1
	return np.bitwise_and(img, np.bitwise_not(marker))

def thinningGH(im):
	img = np.copy(im)
	prev = np.zeros(img.shape, np.uint8)
	while(True):
		img = thinningGHIteration(img, 0)
		img = thinningGHIteration(img, 1)
		diff = np.sum(np.abs(prev-img))
		if not diff:
			break
		prev = img 
	return img

og_image = cv2.imread(name(), 0)
og_image = (og_image[:,:]>128).astype(np.uint8)
start = time.time()
image = thinningGH(og_image)*255
exec_time = time.time()-start
og_image = og_image*255
final_image = og_image-image
print ("Execution Time For the Image : ", exec_time)

cv2.imshow("cool", final_image)
cv2.waitKey(2000)
cv2.imwrite("Output/"+name()[7:-4]+"_gh.png", final_image)

tr = ThinningRate(image)
op, sp, ts = ThinningSpeed(og_image, image, exec_time)
print ("Name : ", name())
print ("Algo : GH")
print ("Thinning Rate : ", tr)
print ("Object Points : ", op)
print ("Skeleton Points : ", sp)
print ("Thinning Speed : ", ts)




