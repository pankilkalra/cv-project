import time
import numpy as np

def ThinningRate(skeleton):
	tm1, tm2 = 0, 0
	n, m = len(skeleton), len(skeleton[0])
	for i in range(1, n):
		for j in range(m):
			if j>0:
				tc = (skeleton[i-1][j-1]*skeleton[i][j-1]) + (skeleton[i-1][j]*skeleton[i-1][j-1])
				if j<m-1:
					tc += (skeleton[i-1][j]*skeleton[i-1][j+1]) + (skeleton[i-1][j+1]*skeleton[i][j+1])
			else:
				tc = (skeleton[i-1][j]*skeleton[i][j+1]) + (skeleton[i-1][j+1]*skeleton[i][j+1])
			tm1 += tc
	tm2 = 4 * ((max(m, n)-1)**2)
	return 1-tm1/tm2


def ThinningSpeed(image, skeleton, time):
	op = (image==255).sum()
	sp = (skeleton==255).sum()
	return op, sp, (op-sp)/time
	
