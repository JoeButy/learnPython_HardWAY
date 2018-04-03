from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

#we could do there two on one line how?
# in_file = open(from_file)
# indata = in_file.read()
# indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

# print "Does the putput file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# open(to_file, 'w').write(open(from_file).read())
# the above does not gaurentee that the file will be closed. 

# to garentee that the file will be closed, it is suggested to use a with function.
with open(from_file) as in_file, open(to_file, 'w') as out_file:
	out_file.write(in_file.read())


# print "Alright, all done."

# in_file.close()
# out_file.close()