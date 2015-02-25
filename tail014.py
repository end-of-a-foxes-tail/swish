from numpy import *
import operator

import math

k=5000001

a=zeros(k,int)

for i in range(k):
	a[i]=-1

a[0]=-1
a[1]=1

for j in range(2):
	for i in range(k)[1:]:
		if a[i]!=-1:
			if 2*i<k: a[2*i]=a[i]+1
			if (i-1)%3==0 and (i-1)%6!=0: 
				if (i-1)/3!=1:
					a[(i-1)/3]=a[i]+1

max=-1
maxval=-1

print 'before the loop, the zero guy was', a[0]

for guy in range(1000000)[1:]:
	if a[guy]==-1:
		counter=0
		zig=[]
		while (guy>k or a[guy]==-1) and counter<1000 :
			zig.append(guy)
			counter+=1
			if counter>999: print 'we failed in a counter way with guy', guy
			if guy%2==0: newguy=guy/2
			else: newguy=3*guy+1
			guy=newguy
			if guy==0: print 'guy was here here', guy, newguy, zig
		#	if guy<k:
		#		if a[guy]!=-1 : print 'we won won won won at step', i, 'with guy', guy

#print 'zig got me ', zig, 'counter is', counter, 'a[80] is', a[80]

		for i in range(len(zig)):
			if zig[i]<k:
				a[zig[i]]=a[guy]+len(zig)-i

		#print 'so then we got', guy, a[guy], zig
		if a[i]>maxval: 
			max=i
			maxval=a[i]

print 'max i is', max, 'with maxval', maxval			
print a[:50]

jmax=-1
jmaxval=-1

for i in range(1000000)[1:]:
	if a[i]>jmaxval:
		jmax=i
		jmaxval=a[i]

print 'jamxss', jmax, jmaxval

"""



def binom(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print binom(8,3)

a=2**28

for i in range(28)[2:]:
	if i%2==0: a=a-binom(28,i)*(2**(28-i))
	else: a=a+binom(28,i)*(2**(28-i))

print a
	

"""
"""idea : if prime factorisation  p1^a1 p2^a2 ... p^k a^k

then sum of divisors is prod_{j=1}^k (\sum_i=0^k p^i)

eg p^2q has sum 1+p+p^2+q+pq+p^2q = (1+p+p^2)(1+q)
"""



"""
make a numbers vector which lists the primes in order : [2,3,5,7,11, ...]
"""
"""

def howmany(w,p):
	for i in range(9999):
		if w%(p**(i+1))!=0: return i
	return 99


def binn(r):
	return bin(r)[2:]

print binn(8), binn(9)

def xxr(a,b):
	#assumes the a string is bigger. 
	l=max(len(a),len(b))
	w=min(len(a),len(b))
	newguy=''
	if l!=w:
		for i in range(l)[w:]:
			newguy=newguy+a[i]
			print i, a[i]
	for i in range(w):
		#print 'we made it to looking through range w', a[0]
		if a[i]=='0':
			#print 'was in the zero a bit'
			if b[i]=='0': newguy=newguy+'0'
			if b[i]=='1': newguy=newguy+'1'
		if a[i]=='1':
			#print 'was in the one a bit'
			if b[i]=='1': newguy=newguy+'0'
			if b[i]=='0': newguy=newguy+'1'
	return newguy

print xxr('1', '1')


for j in range(1000)

#print xxr('111011', '0000')









def transform(vec):
	newguy=[]
	for i in vec:
		if i>0:
			newguy.append(i)
	return newguy


"""