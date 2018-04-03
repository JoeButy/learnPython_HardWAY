print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3+2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it gtreater?", 5 > -2
print "Is it greater of equal?", 5 >= - 2
print "Is it less or equal?", 5 <= - 2

# extra
print 3%4
print 10000%2

# calculate the number of digits you need to make 
# a password in base 10, that would take 3 years to brute force
# assume a trial rate of 10^12 per second.
	#update! the iphone screen cracker runs at 1 attempt every 40 seconds.

# calculate the number of trials that would be possible in three years

# let x be the numer of attempts possible
# one minute is 60 seconds
x = 60 * float(1)/float(40) #10**12
print "Attempts per minute:", x
# one hours is 60 minutes

x = x * 60
print "Attempts per hours:", x 
# one day is 24 hours

x = x * 24
print "Attempts per day:", x 
# one year is about 365.25 days

x = float(x) * float(365.25)
print "Attempts per year:", x 
# for three years

x = 3 * x
print "The attempts in three years:", x 
# Let y be the number of possible code permutaions
# Let z be ther number of digits

# so: y = 10^z

# we know the number of possible code that can be calculated, x
# so let y = x and solve for z
import math

print "Recommended iPhone screen lock length:", math.ceil(math.log10(x))
print "Number of possibily passwords", 10**7, "<- Ten Million"