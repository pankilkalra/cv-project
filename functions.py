import cv2

def CalculateWeight(i, j, image):
	n, m = len(image), len(image[0])
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

def InvertImage(name, image):
	image[image<128] = 0
	image[image>=128] = 1
	for i in range(len(image)):
		for j in range(len(image[0])):
			if image[i][j]==0:
				image[i][j] = 255
			else:
				image[i][j] = 0
	cv2.imwrite(name, image)

def Mark4(i, j, image):
	count = 0
	n, m = len(image), len(image[0])
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