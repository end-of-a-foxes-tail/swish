from numpy import *
import operator

import math

def binom(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print binom(8,3)

a=2**28

for i in range(28)[2:]:
	if i%2==0: a=a-binom(28,i)*(2**(28-i))
	else: a=a+binom(28,i)*(2**(28-i))

print a
	


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