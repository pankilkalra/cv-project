import numpy as np

def thinningZS(im):
	prev = np.zeros(im.shape,np.uint8);
	while True:
		im = thinningZSIteration(im,0);
		im = thinningZSIteration(im,1)
		diff = np.sum(np.abs(prev-im));
		if not diff:
			break
		prev = im
	return im

def thinningZSIteration(im, iter):
	marker = np.zeros(im.shape,np.uint8);
	for i in range(1,im.shape[0]-1):
		for j in range(1,im.shape[1]-1):
			p2 = im[(i-1),j]
			p3 = im[(i-1),j+1]
			p4 = im[(i),j+1]
			p5 = im[(i+1),j+1]
			p6 = im[(i+1),j]
			p7 = im[(i+1),j-1]
			p8 = im[(i),j-1]
			p9 = im[(i-1),j-1]
			A  = (p2 == 0 and p3) + (p3 == 0 and p4) + (p4 == 0 and p5) + (p5 == 0 and p6) + (p6 == 0 and p7) + (p7 == 0 and p8) + (p8 == 0 and p9) + (p9 == 0 and p2)
			B  = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
			m1 = (p2 * p4 * p6) if (iter == 0 ) else (p2 * p4 * p8)
			m2 = (p4 * p6 * p8) if (iter == 0 ) else (p2 * p6 * p8)
			if (A == 1 and (B >= 2 and B <= 6) and m1 == 0 and m2 == 0):
				marker[i,j] = 1;
	return np.bitwise_and(im,np.bitwise_not(marker))