
# ask age
print "How old are you?",
# obtain response
age = raw_input()

#ask height
print "How tall are you?",
# obtain reponse
height = raw_input()

#as weight?!
print "How much fo you weight?",
# obtain response
weight = raw_input()

# results
print "So, you're %s old, %s tall, and %s heavy." % (age, height, weight)
# height needs to be formatted to allot feet'inch" format.
# change %r to %s


#my own "form"

print "Do you like cats?",
like_cats = raw_input("[Y/N] ").lower() == 'y' 

#alternatly substitute == 'y' with 
# in ('y','yes','true','on','1')

if like_cats:
	like_cats = "do"
else:
	like_cats = "don't"


print "\nSo you %s like cats.\n" % like_cats
