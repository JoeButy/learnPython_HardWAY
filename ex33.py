i = 0 
numbers = []

def while_Counting_function(count,increment = 1):
	j = 0
	runTime = True
	while runTime:
		print "At the top i is %d." % j
		numbers.append(j)
	
		j += increment
		print "Numbers now: ", numbers
		print "At the bottome i is %d." % j
		if j >= count:
			runTime = False 
	print "The numbers:"



	for num in numbers:
		print num

def for_Counting_function(count,increment = 1):
# 	j = 0
# 	runTime = True
	for j in range(0, count, increment):
		print "At the top i is %d." % j
		numbers.append(j)
	
		j += increment
		print "Numbers now: ", numbers
		print "At the bottome i is %d." % j
		if j >= count:
			runTime = False 
	print "The numbers:"



	for num in numbers:
		print num

for_Counting_function(100,5)