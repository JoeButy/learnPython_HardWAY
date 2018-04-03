

class Parent(object):

	def __init__(self):
		self.val = 1
	def implicit(self):
		print "PARENT implicit()"

	def override(self):
		print "PARENT overrise()"
		
	def altered(self):
		self.val *= 2
		print "PARENT altered() %d" % self.val

		
class Child(Parent):

	def __init__(self):
		self.val = 100
	
	def override(self): # explicitly define child override
		print "CHILD override()"	
	
	def altered(self):
# 		self.val = 0
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # calls the parent function. inheriting it.
		print "CHILD, AFTER PATEN altered()"


dashes = "- " * 10	
print "\n\tCreate Instances"
dad = Parent()
son = Child()
print dashes
dad.implicit()
son.implicit()
print dashes
dad.override()
son.override()
print dashes
dad.altered()
print dashes, "altered child"
son.altered()
print dashes