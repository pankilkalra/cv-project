import cv2
import numpy as np
import time

def CalculateWeight(i, j):
	N = [128, 1, 2, 64, 0, 4, 32, 16, 8]
	ans = 0
	if i>0 and j>0 and image[i-1][j-1]!=0:
		ans += N[0]
	if i>0 and image[i-1][j]!=0:
		ans += N[1]
	if i>0 and j<m-1 and image[i-1][j+1]!=0:
		ans += N[2]
	if j>0 and image[i][j-1]!=0:
		ans += N[3]
	if j<m-1 and image[i][j+1]!=0:
		ans += N[5]
	if i<n-1 and j>0 and image[i+1][j-1]!=0:
		ans += N[6]
	if i<n-1 and image[i+1][j]!=0:
		ans += N[7]
	if i<n-1 and j<m-1 and image[i+1][j+1]!=0:
		ans += N[8]
	return ans

def Mark4(i, j):
	count = 0
	if i>0 and j>0 and image[i-1][j-1]==0:
		count += 1
	if i>0 and image[i-1][j]==0:
		count += 1
	if i>0 and j<m-1 and image[i-1][j+1]==0:
		count += 1
	if j>0 and image[i][j-1]==0:
		count += 1
	if j<m-1 and image[i][j+1]==0:
		count += 1
	if i<n-1 and j>0 and image[i+1][j-1]==0:
		count += 1
	if i<n-1 and image[i+1][j]==0:
		count += 1
	if i<n-1 and j<m-1 and image[i+1][j+1]==0:
		count += 1
	return 8-count


# BLACK TO WHITE WHITE TO BLACK
image = cv2.imread("big_dog.png", 0)
n, m = len(image), len(image[0])
image[image<128] = 0
image[image>128] = 255
for i in range(n):
	for j in range(m):
		if image[i][j]==0:
			image[i][j] = 0
		else:
			image[i][j] = 1

# INITIALISATION
deletion_array = {3, 5, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 48, 52, 53, 54, 55, 56, 60, 61, 62, 63, 65, 67, 69, 71, 77, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 97, 99, 101, 103, 109, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 131, 133, 135, 141, 143, 149, 151, 157, 159, 181, 183, 189, 191, 192, 193, 195, 197, 199, 205, 207, 208, 209, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 223, 224, 225, 227, 229, 231, 237, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255}
change = True
iterations = 0
start = time.time()

while change and iterations<1000:
	change = False
	iterations += 1
	print ("Iteration : ", iterations)
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
				count = Mark4(i, j)
				if count==2 or count==3 or count==4:
					image[i][j] = 4

	# DELETING UNNECESSARY 4's
	for i in range(n):
		for j in range(m):
			if image[i][j]==4:
				if CalculateWeight(i, j) in deletion_array:
					image[i][j] = 0
				else:
					image[i][j] = 1

	# DELETING UNNECESSARY 2's
	for i in range(n):
		for j in range(m):
			if image[i][j]==2:
				if CalculateWeight(i, j) in deletion_array:
					image[i][j] = 0
					change = True
				else:
					image[i][j] = 1

	# DELETING UNNECESSARY 3's
	for i in range(n):
		for j in range(m):
			if image[i][j]==3:
				if CalculateWeight(i, j) in deletion_array:
					image[i][j] = 0
					change = True
				else:
					image[i][j] = 1

	print ("Time Taken :", time.time()-start)
	start = time.time()


image = image*255
cv2.imshow("image", image)
cv2.imwrite("image.png", image)
cv2.waitKey(2000)
