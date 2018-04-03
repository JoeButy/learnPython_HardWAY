#ask questoins:
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

#results
print "So, you're %s old, %s tall and %s heavy." % (age,height,weight)


#########################333
# python -m pydoc raw_input
#Help on built-in function raw_input in the module __builtin__:

#raw_input(...) 
#	raw_input([promt]) -> string
#	
#	Read a string from standard input. The trialing newline is stripped.
#	If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
#	onUnix, GNU readline is used if enabled. The prompt string, if given,
#	is printed without a trailing newline before reading.
##################


##########################
# open(...)
	# open(name[, mode[,buffering]]) -> file object
	
	# Opend a file ising the file() type, return a file object. This is the	preffered way to open a file. see file.__doc__ for further information.
#######################