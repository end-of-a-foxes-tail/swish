from numpy import *
import operator

import math


print 'hellow world'

def binn(a,b):
	return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

"""
if we have x red tiles it replaces 2x black tiles, so we now have n-x tiles, and we color x of them red.

if we have y green tiles it replaces 3y black tiles, so we now have n-2y tiles, and we color y of them red.

"""

def redtiles(n):
	max=divmod(n,2)[0]
	total=0
	for i in range(max+1)[1:]:
		total+=binn(n-i,i)
	return total

def greentiles(n):
	max=divmod(n,3)[0]
	total=0
	for i in range(max+1)[1:]:
		total+=binn(n-2*i,i)
	return total

def bluetiles(n):
	max=divmod(n,4)[0]
	total=0
	for i in range(max+1)[1:]:
		total+=binn(n-3*i,i)
	return total



print 'for 5, we get red', redtiles(5), 'green', greentiles(5), 'blue', bluetiles(5)

answer=bluetiles(50)+greentiles(50)+redtiles(50)
print 'the answer is ', answer

print binn(6,4)
print binn(3,3)