from numpy import *
import operator

m=2000000
i=2

candidates=ones(m,int)

candidates[0]=0
candidates[1]=0
#numbers = []

tally=0

for k in range(m):
	if candidates[k]!=0:
		tally+=k
#		numbers.append(k)
#		remember[k].append(k)
		times=divmod(m-1,k)[0]
		for time in range(2,times+1):
#			print k, time
#			if k*time>len(candidates): break
			candidates[k*time]=0
#			remember[k*time].append(k)

print tally
#print candidates