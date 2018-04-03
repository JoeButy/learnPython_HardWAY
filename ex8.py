# create a string to be filled with elements
formatter = "%r %r %r %r"

#fill string with integers
print formatter % (1, 2, 3, 4)

#fill string with spelled out integers
print formatter % ("one", "two", "three", "four")

#fill string with trues and falses
print formatter % (True, False, False, True)

#fill string with formatter string, not sure why this isnt recursive
print formatter % (formatter, formatter, formatter, formatter)

#fill string with things to say.
print formatter % ("I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")
	#since there is a single quote it prints the fulldouble quote.