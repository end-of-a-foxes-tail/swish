from numpy import *
import operator

m=13533
n=13530
i=2

candidates=ones(m,int)

remember=list(zeros(m, int))
for i in range(m):
	remember[i]=[]

candidates[0]=0
candidates[1]=0
numbers = []

for k in range(m):
	if candidates[k]!=0:
		numbers.append(k)
		remember[k].append(k)
		times=divmod(m-1,k)[0]
		for time in range(2,times+1):
#			print k, time
#			if k*time>len(candidates): break
			candidates[k*time]=0
			remember[k*time].append(k)

#for i in range(len(remember)):
#	print i, remember[i]

#print numbers[len(numbers)-1]

#print remember[14],remember[15], remember[16], remember[17],remember[18]

"""
make a numbers vector which lists the primes in order : [2,3,5,7,11, ...]
"""

def howmany(w,p):
	for i in range(9999):
		if w%(p**(i+1))!=0: return i
	return 99



#print howmany(2,2), howmany(4,2), howmany(5,2), howmany(14,7)

""" trinum is number of tri numbers considered
	prinum is number of primes you divide into them... 
"""

# here we will try doing both numbers at once in the thing :).

trinum=n
primes=n #controls how long the list of primes we check against is... 

maxval=-1
maxindex=-1
a=0

for i in range(trinum):
	#hacktors[i]=[]
	current=1
	if a==0:
		for p in numbers:
			if p in remember[i+1] or p in remember[i+2]: 
				if p>(i+2)**2 and p!=i+1 and p!=i+2: 
					break
				newguy=howmany((i+1)*(i+2)/2,p)
				if newguy>0: current=current*(newguy+1)
#			else: print 'i was',i, 'p was', p, 'remembers were', remember[i+1], remember[i+2]
				#hacktors[i].
#		print 'triangle number', (i+1)*(i+2)/2, 'has', current, 'factors'
		if current>maxval: 
			maxindex=i+1
			maxval=current
			if current>499: print 'we won', i+1
			#a=1
			#break

print 'we found out', maxindex, 'triangle number', maxindex*(maxindex+1)/2, 'has this many factors:', maxval

""" old version

"""

"""
trinum=n
primes=n #controls how long the list of primes we check against is... 

tractors=[]

for i in range(trinum):
	tractors.append([])

for i in range(trinum):
	for j in range(primes):
		tractors[i].append(howmany(i+1,numbers[j]))

#print tractors[16]

#triangles=[]

triangles=zeros(trinum-1,int)
triangles=list(triangles)

for i in range(trinum-1):
	triangles[i] =(map(operator.add, tractors[i], tractors[i+1]))
#	triangles.append(map(operator.add, tractors[i], tractors[i+1]))
	triangles[i][0]-=1 #because we had to divide out by 2.

def transform(vec):
	newguy=[]
	for i in vec:
		if i>0:
			newguy.append(i)
	return newguy



for i in range(trinum-1):
	triangles[i]=transform(triangles[i])


	#triangles[i]=triangles[i]+tractors[i+1]+1
	#if i==0: triangles[i]=triangles[i]-1

print 'second tractor is', tractors[1]
print 'first guy is', triangles[0]
print '2 guy is', triangles[1]
print '3 guy is', triangles[2]
print '4 guy is', triangles[3]
print '10 guy is', triangles[9]

a=0
b=0
c=0
d=0	


for i in range(trinum-1):
	prod=1
	for j in triangles[i]:
		prod=prod*(j+1)
	#factors.append(prod)
	if prod>50 and a==0: 
		print 'we made it above 50', i+1
		a=a+1
	if prod>100 and b==0: 
		print 'we made it above 100', i+1
		b=b+1
	if prod>150 and c==0: 
		print 'we made it above 150',i+1
		c=c+1
	if prod>200 and d==0: 
		print 'we made it above 150',i+1
		d=d+1
		break




"""


