import random
from urllib import urlopen
import sys


# word source URL.
WORD_URL = "http://learncodethehardway.org/words.txt"
#blank word list. 
WORDS = []

# create a dictionary for the with snippets as keys and phrases as values. 
PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	 "class %%% has-a ___init___ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	 "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	 "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	 "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	 "From *** get the *** attribute and set it to '***'."
}

# do they want to dripp phrases first?
if len(sys.argv) == 2 and sys.argv[1] == 'english':
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website.
for word in urlopen(WORD_URL).readlines():
	# build the words list in the program so it only needs to be referenced once. 
	WORDS.append(word.strip())

def convert(snippet, phrase):
	# fill in tripple char sets with words from bank.
	class_names = [w.capitalize() for w in
			random.sample(WORDS, snippet.count("%%%"))] # capitalize ALL class names.
	other_names = random.sample(WORDS, snippet.count("***")) # fill in other names.
	
	# set results to blank list. 
	results = []
	
	# set params list to empty
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		# set a number of params to include.
		param_count = random.randint(1,3)
		# pull the words from the bank for that many params.
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		# set results list to the code snipped and phrase strings
		result = sentence[:]
		
		# replace each trip char set to word from name list's
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
		
		#fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word,1)
		
		# compile the results
		results.append(result)
	# return from conver function.
	return results

#keep going until they hit CTRL-D
try:
	while True:
		# set phrase dic keys to 'code' snippets
		snippets = PHRASES.keys()
		# shuffle snippets list.
		random.shuffle(snippets)
		
		for snippet in snippets:
			# grab a the phrase that is the current code snippet. 
			phrase = PHRASES[snippet]
			#convert BOTH answer and question.
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				# when 'english' is given as argv, ie phrase is given code is answer.
				question, answer = answer, question
				
			print question
			
			# get response but do no comparison?!? ok....
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"