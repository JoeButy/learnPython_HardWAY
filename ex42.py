## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Create a class named Dog that is-a Animal
class Dog(Animal):
	
	def __init__(self,name):
		## Dog has-a name that is set to name
		print "%s, \"Woof\"" % name
		self.name = name

	def eats(self):
		print "%s the dog eats poop. Seems happy with it." % self.name

## Create a class named Cat that is-a Animal
class Cat(Animal):

	def __init__(self,name):
		## Cat has-a name that is set to name
		self.name = name
		print "%s nocks something over." % name

	def eats(self):
		print "%s the cat, eats friskies and dies." % self.name
		
		
## Class named Person is-a object
class Person(object):
	
	def __init__(self,name):
		## Person has-a name that is set to name

		self.name = name
		print "%s says, \"Hello World!\"" % name		
		## Person has-a pet of some kind
		self.pet = None
		
	def pet_pet(self):
		print 'pet pet', self.pet.name
		if not self.pet.name is None:
			print "%s pets %s" % (self.name, self.pet.name)
		else:
			print "%s has no pet to pet." % self.name
			
## Create a class Employee that is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee,self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		print "%s says, \"Chaching!! $%d\"" % (name,salary)

	def works(self):
		print "%s does some important task" % slef.name
		
		
## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## frank is-an Employee and has-a salary of 120,000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

print frank.pet.name
frank.pet_pet()
frank.pet.eats()

frank.pet = satan
frank.pet.eats()

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()
