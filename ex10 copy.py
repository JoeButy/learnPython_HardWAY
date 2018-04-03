#set cat variables
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



# ESCAPE	WHAT IT DOES.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

print "a\a"
print "b\b"
print "f\f"
print "n\nn"
print "N\N{name}" # as shown
print "r\rr"
print "t\tt"
print "u \u1111 u" # as shown
print "U \U00001111 U" # as showm
print "v\vv"
print "ooo \111 oooo"
print "xhh\x11 xhh" # weitd arrow thing

# create an array of elements have i variable cycle thru them
# one the array is complete the loop restarts?!?! HOW DO I MAKE IT STOP LOL!!!!
# for each element in the array print the element.
for i in ["/", "-", "|", "\\", "|"]:
	print "%s" % i,

print ":" * 15

print "%r" % "''" #quotes appear
print "%s" % "''" #quotes dont appear


# i hate when programs are on infiinite loops. omg i hate it.
# while True:
	# for i in ["/", "-", "|", "\\", "|"]:
		# print "%s\r" % i,
		
		
		
		