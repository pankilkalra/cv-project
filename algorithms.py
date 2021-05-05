import numpy as np

def thinningZS(img):
	prev = np.zeros(img.shape,np.uint8)
	while True:
		img = thinningZSIteration(img,0)
		img = thinningZSIteration(img,1)
		diff = np.sum(np.abs(prev-img))
		print(diff)
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

def thinningGH(img):
	prev = np.zeros(img.shape, np.uint8)

	while(True):
		img = thinningGHIteration(img, 0)
		img = thinningGHIteration(img, 1)
		diff = np.sum(np.abs(prev-img))
		print(diff)
		if not diff:
			break
		prev = img 
	return img