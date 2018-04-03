
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none() 

# function check list:
# did you initialize your function with the "def" syntax?
# does your function name have only characters and '_' (underscore) characters?
# did you put an open parentesis '(' right after the function name?
# did you put your arguments after the parenthesis '(' separated by commas?
# did you make each argument unique (no duplicated names)?
# did you put a close parenthesis AND a colon '):' after the arguments?
# Did you indent ALL lies of code you want in the function? [four spaces, exactly]
# did you end your function by going back to the unindented text column?

# to run call of use a function all mean the same thing. 





