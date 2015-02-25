from numpy import *
import operator


"""idea : if prime factorisation  p1^a1 p2^a2 ... p^k a^k

then sum of divisors is prod_{j=1}^k (\sum_i=0^k p^i)

eg p^2q has sum 1+p+p^2+q+pq+p^2q = (1+p+p^2)(1+q)
"""

m=10010
n=10001
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

nums=n
primes=n #controls how long the list of primes we check against is... 

maxval=-1
maxindex=-1
a=0

divisorsums=zeros(n,int)


for i in range(nums)[1:]:
	#hacktors[i]=[]
	current=1
	if a==0:
		for p in numbers:
			if p in remember[i]:
				#print 'i is', i, 'and we remember', remember[i]
				if p>i**2 and p!=i: 
					break
				newguy=howmany(i,p)
				#print 'we just set new guy to howmany of', i,p
				if newguy>0:
					sumguy=1 
					for j in range(newguy):
						sumguy=sumguy+p**(j+1)
					current=current*(sumguy)
					#print 'i is', i, 'p is', p, 'newguy is', newguy, 'sumguy is', sumguy

#			else: print 'i was',i, 'p was', p, 'remembers were', remember[i+1], remember[i+2]
				#hacktors[i].
#		print 'triangle number', (i+1)*(i+2)/2, 'has', current, 'factors'
		current=current-i #this is because we don't wanna sum the num itself in the divisors
		if current>maxval: 
			maxindex=i
			maxval=current
			#a=1
			#break
	divisorsums[i]=current
	#print 'i is', i, 'p is', p, 'current is', current

#print 'we found out', maxindex, 'has divisor sum', maxval
#print 'candidates is', candidates
#print divisorsums

up=0
down=0
sum=0


for i in range(n):
	if i<divisorsums[i]: #we wanna check is it has a thingo
		if divisorsums[i]<n:
			pair=divisorsums[divisorsums[i]]
			if pair==i: 
				print 'we gotta match', i, divisorsums[i]
				sum+=i+divisorsums[i]

print sum
print 'number of guys where divisor sum bigger than guy', up, 'and vice-versa', down

#print 'remember is', remember
""" old version

"""

"""


def transform(vec):
	newguy=[]
	for i in vec:
		if i>0:
			newguy.append(i)
	return newguy


"""