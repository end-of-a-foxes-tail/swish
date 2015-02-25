from numpy import *
import operator

from fractions import gcd
import math



import time

"""

Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), 
B(0, b), 
C(-c, 0), 

D(0, -d), 
where 1 leq a, b, c, d leq m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points.


How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?

Picks theorem
2A equals 2i plus b minus 2.

i is interior points... and b is boundary points. 

Step 1. work out how many boundary points on the 0,a,b triangle.

if a and b have only one prime factor, p, in common, then have p+1 points on the line ab including endpoints.

if 3 and 21,       then 1,7; 2,14, 3,21 all make triangles :).

i=1/2 ((a-1)(b-1)+1 - gcd(a,b))
so then add teh 4i's together, 
and add (a-1)+(b-1)+(c-1)+(d-1) +1
for edge points and origin point respectively.


"""

def ire(a,b):
	return ((a-1)*(b-1)+1-gcd(a,b))/2



n=101 #i.e. is equal to m+1

start=time.time()

#matty=zeros((n-1,n-1),int)

matty=[]
for i in range(n-1):
	matty.append([])
	for j in range(n-1):
		matty[i].append(ire(i+1,j+1))
mid=time.time()


squares =0
for a in range(n-1):
	for b in range(n-1):
		totab=matty[a][b]+a+b+1
		for c in range(n-1):
			totbc=matty[b][c]+c
			for d in range(n-1)[c:]:
				result=(totab+totbc+matty[c][d]+matty[a][d]+d)**0.5
				#print 'abcd gave me', a,b,c,d,result
				if result==int(result): 
					squares+=1
					if c!=d: squares+=1


print 'tell j that',n-1, 'is',squares

def binn(a,b):
	return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

end=time.time()

print end-start, 'amount of time'
print mid-start, 'to make the matrix'



