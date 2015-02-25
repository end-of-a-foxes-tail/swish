from numpy import *
import operator

import math

# number of elements co-prime with p^k is .... p^k-p^{k-1}
# e.g. for 25, get 20

#hece for 5^10, number of elements co-prime is 5^10-5^9


#problem, want the last 10 digits of 28433 x 2^7830457

b=7830457-5**10+5**9
print 'left over is',b

start=1
for i in range(b):
	start=divmod(2*start,10**10)[1]

print 'now we have', start
start=divmod(28433*start, 10**10)[1]
print 'now we have', start



print 'another guy'


a=zeros(25,int)

print 'we want a banana', divmod(2**20,25)

start=2
counter=1


while divmod(start,25)[1]!=1:
	start=divmod(start*2,25)[1]
	counter+=counter+1
	


print counter, start, 'an elephant'




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