intro_text = """
--------INTRO-------
Aliens have invaded a spave ship and out hero has to go through a maze of
rooms defeating them so he can escape into an escape pod to the planet
below. The game will be more like a Zork or Adventure type game with text
outputs and funny ways to die. Each room will print its own description
when the player inters it and then tell the engine what room to run next
out of the map. 
--------------------
"""


def death():
	player = dead

def central_cooridor():
	room_description = ""
	print room_description
	
def armory():
	guns = []
	
def brige():
	bridge_description
	print bridge_description

def excape_pod():
	escape_pod_description
	print escape_pod_description

nouns = """
Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape Pod
Planet
Map
Engine
Death
Central Corridor
Laser Weapon
The Bridge
"""

class_heirarchy = """
*Map
*Engine
*Scene
	*Death
	*Central Cooridor
	*Laser Weapon Armory
	*The Bridge
	*Escape Pod
"""

actions = """
*Map
	-next_scene
	-opening_scene
*Engine
	-play
*Scene
	-enter
	*Death
	*Centeral Corridor
	*Laser Weapon Armory
	*The Bridge
	*Escape Pod
"""

from sys import exit
from random import randint


class Scene(object):
	
	def enter(self):
		print "This scene is not yest configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene("finished")

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		current_scene.enter()

class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud.... if she were smarter.",
		"Such a lewser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(1,len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		
		gothons = randint(1,4)
		central_corridor_fight = Fight(gothons)
		
		print """
		The Gothons of planet Percel #25 have invaded your ship and destroyed
		your entire crew. You are the last surviving member and your last
		mission is to get the neutron destruct bomb from the Weapons Armory,
		put it in the bridge, and blow the ship up ater getting into an
		escape pod.
		"""
		print "You're running down the central cooridor to the Weapons Armory when"
		print "%d Gothon(s) jumps out" % gothons
# 		print "with red scaly skin, dark grimy teeth and evil clown costume"
# 		print "flowing around his hate filled body. He's blocking the door to the"
# 		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
# 			print """ 
# 			Quick on the draw you yank out your blaster and fire at the Gothon.
# 			His clown costume is flowing and moving around his body, which throws
# 			off your aim. Your laser hits his costume but misses him entirely. This
# 			completely ruins his brand new costume his mother bought him, which
# 			makes him fly into an insane rage and blast you repeatedly in the face until
# 			you are dead. Then he eats you.
# 			"""

			fight_won = central_corridor_fight.commence()
			
			if fight_won:
				print "The battle was won! You continues on to the Weapon Armory."
				output = 'laser_weapon_armory'
			
			else:
				output = 'death'
		
		
		elif action == "dodge!":
			print """
			Like a world class boxer you dodge, weave, slip and slide right
			as the Gothon's blaser cranks a laser past your head.
			In the middle of your artful dodge your foot slips and you
			bang your head on the metal wall and pass out.
			You wake up shortly after only to die as the Gothon stomps on
			your head and eats you.
			"""
			output = 'death'
			
		elif action == "tell a joke":
			print """
			Lucky for you they made you learn Gothon insults in the academy.
			You tell the on Gothon joke you know:
			Lbhe Zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
			The Gothon stops, tries ot to laugh, the busts out laughing and can't move.
			While he's laughing you run up and shoot him square in the head
			putting him down, then jump thru the Weapon Armory door.
			"""
			output = "laser_weapon_armory"	
		
		else:
			print "DOES NOT COMPUTE!"
			output = "central_corridor"
		
		return output


class LaserWeaponArmory(Scene):
	
	def enter(self):
		low_digit = 1
		high_digit = 1
		print """
		You do a dive roll into the Weapon Armory, crouch and scan the room
		for mor Gothons that might be hiding. It's dead quiet, to quiet.
		You stand up and run to the far side of the room and find the 
		neutron bomb in its container. There's a keypad lock on the box
		and you need the code to get the bomb out. If you get the code
		wrong 10 times then the lock closes forever and you can't 
		get the bomb. The code is 3 digits.
		"""
		print "The key pad takes digits %d thru %d" % (low_digit, high_digit)

		code = "%d%d%d" % (randint(low_digit,high_digit),
			randint(low_digit,high_digit), randint(low_digit,high_digit))
		guess = raw_input("> ")
		guesses = 1
		
		while guess != code and gesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("> ")
		
		if guess == code:
			print """
			The container clicks open and the seal breaks, letting gas out.
			You grab the neutron bomb and run as fast as you can to the
			bridge where you must place it int the right spot.
			"""
			return "the_bridge"
		else:
			print """
			The lock buzzes on last time and then you hear sickening
			meling sound as the mechanism us fused together.
			You decide to sit there, and finally the Gothons blow up the 
			ship from their ship and you die.
			"""
			return "death"
			

class TheBridge(Scene):
	
	def enter(self):
		print """ 
		Your burst onto the Bridge with the netron destuct bomb
		under your arm and surprise 5 Gothons who are trying to 
		take control of the ship. Each of them has an even uglier
		clown costume than the last. They haven't pulled their
		weapons out yet as they see the active bomb under your
		arm and don't want to set it off.
		"""
			
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print """
			In a panic you throw the bomb at the group of Gothons
			and make a leap for the door. Right as your drop it a 
			Gothon shoots you right in the back killing you.
			As you die you see another Gothon frantically try to disarm
			the bomb. You die knowing they will probably blow up when 
			it goes off.
			"""
			output =  "death"
		
		elif action == "slowly place the bomb":
			print """
			You point your blaster at the bomb under your arm
			and the Gothons put their hands up and start to sweat.
			You inch backwards to the door, opwn it, and then carfully
			place the bomb on the floor pointing your blaster at it.
			You then jump back through the door, punch the close button
			and blast the lock so the Gothons can't get out.
			Now that the bomb is placed you run to the escape pod to
			get off this tin can.
			"""
			output =  'escape_pod'
		
		else:
			print "DOES NOT COMPUTE!"
			output = "the_bridge"
		
		return output

class EscapePod(Scene):
	
	def enter(self):
		number_of_pods = 2
		print """
		You rush throught the ship desperatly trying to make it to 
		the escape pod before the whole ship explodes. It seems like 
		hardly any Gothons are on the ship, so your run is clear of
		interference. You get to the chamber with the excape pods, and 
		now need to pick on to take. Some of them could be damaged
		but you don't have time to look.
		"""
		print "There are %d pods, which one do you take?" % number_of_pods	
		
		good_pod = randint(1,number_of_pods)
		guess = raw_input("[pod #]> ")
		
		print "You jump into pod %s and hit the eject button." % guess
		
		if int(guess) != good_pod:
			print """
			The pod escapes out into the void of space, then"
			implodes as the hull ruptures, crushing your body
			into a jam jelly.
			"""
			return 'death'
		else:
			print """
			The pod easily slide out into space heading to 
			the planed below. As it flies to the planet, you look
			back and see your ship implode the explode like a 
			bright star, taking out the Gothon ship at the same
			time. You won!
			"""
			return 'finished'
			
class Finished(Scene):
	
	def enter(self):
		print "You won! Good job."
		return 'finished'

class Fight(object):

	def __init__(self, gothons, difficulty = 1):
		self.difficulty = difficulty
		self.hero_hp = 100
		self.gothons = gothons
		self.gothon_arr = []
		for i in range(0,gothons):
			self.gothon_arr.append(50 + randint(-5,20) * difficulty)
		 
	def commence(self):
		win = False
		
		if self.hero_hp < 95: 
			self.hero_hp += 25
			
		elif self.hero_hp >= 95:
			self.hero_hp = 100

		while self.hero_hp > 0:
			gothon_attack = randint(-25 * self.difficulty,0)
			hero_attack = randint(0,50 * self.difficulty)
			self.hero_hp += gothon_attack
			
			if self.hero_hp <= 0:
				win = False
				break
				
			print "You were hit for %d your hp is now %d" % (abs(gothon_attack), self.hero_hp)
			for i in range(0, self.gothons):
				gothon = self.gothon_arr[i]
				if gothon > 0:
					self.gothon_arr[i] -= hero_attack
					print "Gothon #%d was hit for %d" % (i, hero_attack)
					print "The gothon now has %d hp" % self.gothon_arr[i]
					break
				
				elif gothon <= 0 and i == self.gothons - 1:
					win = True
					break
					
				else:
					pass
			if win:
				break
						
		return win
	
class Map(object):
	
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)


print intro_text
a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()




