
last=0
hot=1
counter=0
total=0


for i in range(32):
	hottemp=hot
	hot=hot+last
	last=hottemp
	counter=counter+1
	if counter%3==2: total=total+hot


	print counter, hot, total
