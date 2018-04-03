from sys import argv # import the argv module

script, input_file = argv # set variables with the argv from the terminal

def print_all(f): # define a fuction
	print f.read() # print file contents 

def rewind(f): # define a function
	print f.seek(0) # return the file to the 0 postion

def print_a_line(line_count, f): # define a fucntion with two inputs
	print line_count, f.readline() # print the first variable and run readline operator (f FSO will keep track of the byte position, also readline will print a '\n' at the end of the return string.

current_file = open(input_file) # set FSO to file given in terminal

print "First let's print the whole file:\n"

print_all(current_file) # call print all function

print "Now let's rewind, kind of like a tape." 

rewind(current_file) # call the rewind function

print "Let's print three lines." 

current_line = 1
print_a_line(current_line, current_file)

# rewind(current_file)
current_line+=1
print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line, current_file)
