import cv2
import numpy as np
import time
from functions import CalculateWeight, InvertImage
from performance_measures import ThinningRate, ThinningSpeed

name = "big_dog.png"
# InvertImage(name, cv2.imread(name, 0))
# exit()

# INITIALISATION
border_lookup = {3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60, 62, 63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223, 224, 225, 227, 231, 239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254}
phase1_lookup = {7, 14, 28, 56, 112, 131, 193, 224}
phase2_lookup = {7, 14, 15, 28, 30, 56, 60, 112, 120, 131, 135, 193, 195, 224, 225, 240}
phase3_lookup = {7, 14, 15, 28, 30, 31, 56, 60, 62, 112, 120, 124, 131, 135, 143, 193, 195, 199, 224, 225, 227, 240, 241, 248}
phase4_lookup = {7, 14, 15, 28, 30, 31, 56, 60, 62, 63, 112, 120, 124, 126, 131, 135, 143, 159, 193, 195, 199, 207, 224, 225, 227, 231, 240, 241, 243, 248, 249, 252}
phase5_lookup = {3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60, 62, 63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223,224, 225, 227, 231, 239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254}
one_pixel_lookup = {3, 6, 7, 12, 14, 15, 24, 28, 30, 31, 48, 56, 60, 62, 63, 96, 112, 120, 124, 126, 127, 129, 131, 135, 143, 159, 191, 192, 193, 195, 199, 207, 223,224, 225, 227, 231, 239, 240, 241, 243, 247, 248, 249, 251, 252, 253, 254}
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
while change:
	change = False

	# IDENTIFYING BORDER PIXELS
	borders = set()
	for i in range(n):
		for j in range(m):
			if image[i][j] and CalculateWeight(i, j, image) in border_lookup:
				borders.add((i, j))

	# REMOVING PIXELS IN PHASES
	ind = 0
	while ind<len(lookup_arrays):
		curr_lookup = lookup_arrays[ind]
		to_be_removed = set()
		for pixel in borders:
			if CalculateWeight(pixel[0], pixel[1], image) in curr_lookup:
				image[pixel[0]][pixel[1]] = 0
				change = True
				to_be_removed.add(pixel)
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
cv2.imwrite(name[:-4]+"_k3m.png", final_image)
cv2.waitKey(1000)

tr = ThinningRate(image)
op, sp, ts = ThinningSpeed(og_image, image, exec_time)
print ("Name : ", name)
print ("Algo : K3M")
print ("Thinning Rate : ", tr)
print ("Object Points : ", op)
print ("Skeleton Points : ", sp)
print ("Thinning Speed : ", ts)








