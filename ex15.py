
# this is where the system code package is brought in,
# only the argument value module is accessed.
from sys import argv

# the script variable by default is set to the file that was first referenced 
# in the program call "python ex15.py ex15_sample.txt"
script, filename = argv

# the txt variable is set to the file name file objecct.
txt = open(filename)

#the filename is printed
print "Here's your file %r:" % filename

# the txt file objet is read, and printed
print txt.read()

txt.close()

# end of exercise notes
# python 
# f = open("/Users/joebuty/documents/ex15_sample.txt")

############
# raw_input method
# this method is not as good because you can not quickly run the program again
# by using the up arrow short ut in the terminal to rerun
# the last command that was run. but instead must type the file name again.
############
# # the file name is asked for in the terminal while the code is running
# print "Type the fileName again:"
# # the file name promted with a greater than sign. 
# # the file_again variable is set to the user input.
# file_again = raw_input('> ')
# 
# # the txt_again variable is set to the file_again file object.
# txt_again = open(file_again)
# 
# # the txt_again file object is read and printed to the terminal. 
# print txt_again.read()
# txt_again.close()