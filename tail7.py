from numpy import *

n=10

i = 2
numbers = []

def isprime(k, numbers):
	counter=0
	for i in range(len(numbers)):
		factor=numbers[i]
		if k%factor==0:
			return False
	return True

print 'we are trying', isprime(7,[2,3,5])
print 'we are trying', isprime(6,[2,3,5])
print 'we are trying', isprime(10,[2,3,5])



while len(numbers) < 11000:
    if isprime(i,numbers): 
    	    numbers.append(i)
    i = i + 1

print 'the 1001-th prime is', numbers[1000]
print 'the 10001-th prime is', numbers[10000]

