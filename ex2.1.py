# calculate the number of digits you need to make 
# a password in base 10, that would take 3 years to brute force
# assume a trial rate of 10^12 per second.
	#update! the iphone screen cracker runs at 1 attempt every 40 seconds.

# calculate the number of trials that would be possible in three years

# let x be the numer of attempts possible
# one minute is 60 seconds
x = 60 * 1/40 #10**12

# one hours is 60 minutes

x = x * 60

# one day is 24 hours

x = x * 24

# one year is about 365.25 days

x = float(x * 365.25)

# for three years

x = 3 * x
print "The number of possible attempts.", x 
# Let y be the number of possible code permutaions
# Let z be ther number of digits

# so: y = 10^z

# we know the number of possible code that can be calculated, x
# so let y = x and solve for z
import math

print math.ceil(math.log10(x))
