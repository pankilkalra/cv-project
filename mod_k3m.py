import cv2
import numpy as np
import time
from functions import CalculateWeight, InvertImage
from performance_measures import ThinningRate, ThinningSpeed

def c1(i, j, image):
	wt = CalculateWeight(i, j, image)
	if (wt==95 and image[i-2][j]==0) or (wt==125 and image[i][j-2]==0) or (wt==215 and image[i][j+2]==0) or (wt==245 and image[i+2][j]==0):
		return True
	return False

def c2(i, j, image, borders):
	wt = CalculateWeight(i, j, image)
	if wt==241 and image[i][j+1] in borders and image[i][j+2]==0 and image[i+1][j+2]==0:
		return True
	return False


def c3(i, j, image, borders):
	wt = CalculateWeight(i, j, image)
	if (wt==195 or wt==227) and image[i+1][j-1] in borders:
		return True
	return False




name = "big_dog.png"
# InvertImage(name, cv2.imread(name, 0))
# exit()

# INITIALISATION
border_lookup = {3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60, 62,63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223, 224, 225,227, 231, 239, 240, 241, 243, 247, 248, 249, 251,252, 253, 254,}
phase1_lookup = {7, 14, 28, 56, 112, 131, 193, 224}
phase2_lookup = {7, 14, 15, 24, 28, 30, 48, 56, 60, 112, 120, 131,135, 192, 193, 195, 224, 225, 240}
phase3_lookup = {7, 14, 15, 28, 30, 31, 56, 60, 62, 112, 120, 124, 131, 135, 143, 193, 195, 199, 224, 225, 227, 240, 241, 248}
phase4_lookup = {7, 14, 15, 28, 30, 31, 56, 60, 62, 63, 112, 120, 124, 126, 131, 135, 143, 159, 193, 195, 199, 207, 224, 225, 227, 231, 240, 241, 243, 248, 249, 252}
phase5_lookup = {3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60, 62, 63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223,224, 225, 227, 231, 239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254}
one_pixel_lookup = {2, 5, 13, 20, 21, 22, 32, 48, 52, 54, 65, 67,69, 80, 81, 84, 88, 97, 99, 128, 133, 141, 208, 216}
lookup_arrays = [phase1_lookup, phase2_lookup, phase3_lookup, phase4_lookup, phase5_lookup]
change = True

# BACKGROUND = 0, FOREGROUND = 1
image = cv2.imread(name, 0)
n, m = len(image), len(image[0])
image[image<=128] = 0
image[image>128] = 255
image[image==255] = 1

start = time.time()
iteration = 1
while change and iteration<100:
	change = False

	# IDENTIFYING BORDER PIXELS (Phase 0)
	borders = set()
	for i in range(n):
		for j in range(m):
			wt = CalculateWeight(i, j, image)
			if image[i][j] and CalculateWeight(i, j, image) in border_lookup:
				if wt==193 and image[i-1][j-1]==1:
					borders.add((i-1, j-1))
				borders.add((i, j))
			else:
				if c1(i, j, image):
					borders.add((i, j))

	# Phase 0A
	for i in range(n):
		for j in range(m):
			if (i, j) in borders:
				wt = CalculateWeight(i, j, image)
				if wt==31 or wt==124:
					borders.add((i, j))


	# REMOVING PIXELS IN PHASES
	ind = 0
	while ind<len(lookup_arrays):
		curr_lookup = lookup_arrays[ind]
		to_be_removed = set()
		for pixel in borders:
			wt = CalculateWeight(pixel[0], pixel[1], image)
			if wt in curr_lookup:
				if c2(i, j, image, borders):
					if CalculateWeight(pixel[0], pixel[1]+1, image) in curr_lookup:
						image[pixel[0]][pixel[1]+1] = 0
						to_be_removed.add((pixel[0], pixel[1]+1))
				elif c3(i, j, image, borders):
					if CalculateWeight(pixel[0]+1, pixel[1]-1, image) in curr_lookup:
						image[pixel[0]+1][pixel[1]-1] = 0
						to_be_removed.add((pixel[0]+1, pixel[1]-1))
				change = True
				image[pixel[0]][pixel[1]] = 0
				to_be_removed.add((pixel[0], pixel[1]))


		for pixel in to_be_removed:
			borders.remove(pixel)
		ind += 1

	# VISUALISATION
	# image = image*255
	# cv2.imshow("image", image)
	# cv2.waitKey(100)
	# image = image//255


# ONE PIXEL THINNING
for i in range(n):
	for j in range(m):
		if image[i][j] and CalculateWeight(i, j, image) in one_pixel_lookup:
			image[i][j] = 0

exec_time = time.time()-start
print ("Execution Time For the Image : ", exec_time)

og_image = cv2.imread(name, 0)
og_image[og_image<=128] = 0
og_image[og_image>128] = 255
image = image*255
final_image = og_image-image
cv2.imshow("image", final_image)
cv2.imwrite(name[:-4]+"_modk3m.png", final_image)
cv2.waitKey(1000)

tr = ThinningRate(image)
op, sp, ts = ThinningSpeed(og_image, image, exec_time)
print ("Name : ", name)
print ("Algo : Modified K3M")
print ("Thinning Rate : ", tr)
print ("Object Points : ", op)
print ("Skeleton Points : ", sp)
print ("Thinning Speed : ", ts)








