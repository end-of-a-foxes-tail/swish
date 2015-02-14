from numpy import *

""" want a^2 +b^2 =c^2 and a+b+c=1000"""

a=zeros((20,20),int)

f = open('readtail011.txt', 'r')

for row in range(20):
	s=f.readline()[:-1]
	t=s.split(' ')
	for col in range(len(t)):
		a[row,col]= int(t[col])



print a

""""

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
"""

