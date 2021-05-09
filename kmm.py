import cv2
import numpy as np
import time
from functions import CalculateWeight, InvertImage, Mark4
from performance_measures import ThinningRate, ThinningSpeed

name = "big_dog.png"
# InvertImage(name, cv2.imread(name, 0))
# exit()

# BACKGROUND = 0, FOREGROUND = 1
image = cv2.imread(name, 0)
n, m = len(image), len(image[0])
image[image<=128] = 0
image[image>128] = 255
image[image==255] = 1

# INITIALISATION
deletion_array = {3, 5, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 48, 52, 53, 54, 55, 56, 60, 61, 62, 63, 65, 67, 69, 71, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 97, 99, 101, 103, 109, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 131, 133, 135, 141, 143, 149, 151, 157, 159, 181, 183, 189, 191, 192, 193, 195, 197, 199, 205, 207, 208, 209, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 223, 224, 225, 227, 229, 231, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255}
change = True
iterations = 0
start = time.time()

while change:
	change = False
	
	# MARKING 2's
	for i in range(n):
		for j in range(m):
			if image[i][j]!=0:
				if i>0 and image[i-1][j]==0:
					image[i][j] = 2
				elif j>0 and image[i][j-1]==0:
					image[i][j] = 2
				elif i<n-1 and image[i+1][j]==0:
					image[i][j] = 2
				elif j<m-1 and image[i][j+1]==0:
					image[i][j] = 2

	# MARKING 3's
	for i in range(n):
		for j in range(m):
			if image[i][j]==1:
				if i>0 and j>0 and image[i-1][j-1]==0:
					image[i][j] = 3
				elif i<n-1 and j>0 and image[i+1][j-1]==0:
					image[i][j] = 3
				elif i<n-1 and j<m-1 and image[i+1][j+1]==0:
					image[i][j] = 3
				elif i>0 and j<m-1 and image[i-1][j+1]==0:
					image[i][j] = 3

	# MARKING 4's
	for i in range(n):
		for j in range(m):
			if image[i][j]!=0:
				count = Mark4(i, j, image)
				if count==2 or count==3 or count==4:
					image[i][j] = 4

	# DELETING UNNECESSARY 4's
	for i in range(n):
		for j in range(m):
			if image[i][j]==4:
				if CalculateWeight(i, j, image) in deletion_array:
					image[i][j] = 0
				else:
					image[i][j] = 1

	# DELETING UNNECESSARY 2's
	for i in range(n):
		for j in range(m):
			if image[i][j]==2:
				if CalculateWeight(i, j, image) in deletion_array:
					image[i][j] = 0
					change = True
				else:
					image[i][j] = 1

	# DELETING UNNECESSARY 3's
	for i in range(n):
		for j in range(m):
			if image[i][j]==3:
				if CalculateWeight(i, j, image) in deletion_array:
					image[i][j] = 0
					change = True
				else:
					image[i][j] = 1

	# image = image*255
	# cv2.imshow("image", image)
	# cv2.waitKey(100)
	# image = image//255

exec_time = time.time()-start
print ("Execution Time For the Image : ", exec_time)

og_image = cv2.imread(name, 0)
og_image[og_image<=128] = 0
og_image[og_image>128] = 255
image = image*255
final_image = og_image-image
cv2.imshow("image", final_image)
cv2.imwrite(name[:-4]+"_kmm.png", final_image)
cv2.waitKey(1000)

tr = ThinningRate(image)
op, sp, ts = ThinningSpeed(og_image, image, exec_time)
print ("Name : ", name)
print ("Algo : KMM")
print ("Thinning Rate : ", tr)
print ("Object Points : ", op)
print ("Skeleton Points : ", sp)
print ("Thinning Speed : ", ts)



