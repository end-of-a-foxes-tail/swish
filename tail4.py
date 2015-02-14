from numpy import *
max=0


def checkme(num):
	g=str(num)
	length=len(g)
	half=divmod(length,2)[0]
	counter=0
	for i in range(half):
		if g[i]==g[length-i-1]: counter=counter+0
		else: counter=counter+1
	if counter==0: 
		return True
	else: return False


for i in range(1000)[800:]:
	for j in range(1000)[i:]:
		now=i*j
		if checkme(now): 
			if now>max: max=now

print max

