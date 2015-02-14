
n=600851475143 
max=1


print n**0.5

for i in range(775147):
	if n%(i+1)==0: 
		print i+1
		n=divmod(n,i+1)[0]



