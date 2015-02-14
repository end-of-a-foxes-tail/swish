from numpy import *

""" want a^2 +b^2 =c^2 and a+b+c=1000"""


f = open('readtail8.txt', 'r')
s=f.read()
print s[0],s[1],s[2],s[3]
print 'length is', len(s)

k=13
a=[]
for j in range(k):
	a.append(int(s[j]))

max=1




for l in range(k):
	max=max*a[l]

print max

newproduct=max



for i in range(1000-k):
	oldproduct=newproduct
	old=int(s[i])
	new=int(s[i+k])
	if old!=0 : 
		newproduct=oldproduct*new
		newproduct=newproduct/old
	if old==0 : 
		newproduct=1
		for j in range(k):
			newproduct=newproduct*int(s[i+j+1])
	print newproduct
	if newproduct>max: max=newproduct

print max

