mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple']

def apple():
	print "I AM APPLES!"

class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print "I MA CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine


class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

print '-' * 10
happy_bday = Song(["Happy birthday to you", \
					"I don't want to get sued", \
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print '-' * 10

hand_del_pus_corus = ["I told her to come thru", "The I just could out", "And give it to you"]

hand_del_pus = Song(hand_del_pus_corus)

hand_del_pus.sing_me_a_song()


