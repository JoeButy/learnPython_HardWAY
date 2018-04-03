# IMPORTANT FILE COMMANDS!
# close -- Closes the file. like file -> save in the text editor. (? does it close it thou?)
# read -- reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file. 
# truncate -- Empties the file. Watch out if you care about the file. (XD)
# write('stuff') -- Writes "stuff" to the file. 

### Make a simple little text editor.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..." # opening a file to in 'write' mode
target = open(filename, 'w') # open file that was specified in the terminal by argv 1
# open file in 'w' mode will truncate the file automatically.


print "Truncating the file. Goodbye!"
target.truncate() # delete file contents (again!)

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# use the plus sign to concate in python, unlike with print where you can use a comma. but i think that is just
# to add things to the same line. where as the plus sign works as a concatination.
print_str = line1 + "\n" + line2 + "\n" + line3 + "\n"
# print print_str
 
target.write(print_str)

print "And finally, we close it."
target.close() # always always close a file when you are done.
