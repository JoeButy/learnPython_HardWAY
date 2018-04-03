
def triangle_room(entered_blue_room):
	
	if entered_blue_room:
		print "You enter a triangilar room, where the grey paint was, there is a door."
	
	else:
		print "You enter a triangular room."
		print "The left wall has some gray paint on it."
	
	print "The door behind you is still adjar."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	openDoor = entered_blue_room and "open" in choice 
	goback = "exit" in choice or "leave" in choice
	
	if openDoor:
	
		dead("You have escaped the Maze of Death.",True)
	
	elif goback:
		start(entered_blue_room)
	
	else:
		dead("Nothing happens.")

def circle_room(entered_blue_room):
	print "You enter a circular room."
	print "The door that you came in thru is adjar."
	print "There is a large red splat on the ground and similarly on the ceiling."
	print "There is a glowing white botton in the middle of the room on the floor."
	print "There is a circlar tunnel, chest high, in the wall."
	again = ""
	
	attemps = 0
	
	while True:
		choice = raw_input(again + "> ")
		pressButton = "press the button" in choice
		intoTunnel = "tunnel" in choice
		backOut = "leave" in choice
		attemps += 1
		if pressButton:
			circle_room_buttoned()
			
		elif intoTunnel:
			tunnel_closed(entered_blue_room)
		
		elif backOut:
			start(entered_blue_room)
			
		elif attemps >=3:
			dead("You starve and die.")
			
		else:
			print "Nothing happens."
			again = "Now What?"

def tunnel_closed(entered_blue_room):
	print "The tunnel is a dead end."
	print "Do you back out?"

	choice = raw_input("> ")
	
	if "back out" in choice:
		circle_room(entered_blue_room):
	else:
		dead("You starve.")

def circle_room_buttoned():
	ceilingMove = "You hear a loud bang and the ceiling moves down a bit."
	print ceilingMove
	print "Then you hear the door behind you clang loudly."
	print "You have a sinking feeling you better do something fast."
	
	attemps = 0
	
	while attemps < 4:
		choice = raw_input("> ")
		
		if "go thru tunnel" in choice:
			blue_room()
		
		if attemps == 0:
			print ceilingMove
			print "The ceiling is just above your head."
			
		elif attemps == 1:
			print ceilingMove
			print "You are now crowching the ceiling is so low."
		
		elif attemps == 2:
			print ceilingMove
			print "You are now bent over neiling."
		
		else:
			dead("The ceiling crushed you into a red splat.")
		
		attemps+=1

def blue_room():
	print "You crawl out of the tunnel into a blue room."
	print "There is nothing in the room, except the tunnel you came in thru."
	
	choice = raw_input("> ")
	entered_blue_room = True
	
	if "go thru tunnel" in choice:
		circle_room(entered_blue_room)
	else:
		dead("Nothing happens, you starve.")

def rectangle_room(entered_blue_room):
	print "You enter a rectangular room."
	print "The door you came in thru is still adjar."
	print "There is a rectangular whole in the middle of the room."

	choice = raw_input("> ")
	
	if "leave thru the door" in choice:
		start(entered_blue_room)
		
	elif "whole" in choice:
		dead("The whole does not have a bottom, you are in free fall. You starve and die.")
	
	else:
		dead("The door you came in thru shuts. You starve and die.")

def dead(str):
	print str, " Good Job!"
	exit(0)


def start(entered_blue_room=False,first_start=False):

	if first_start:
		print "You wake up in at the vertex of a pizza slice shaped room."
		print "Your stomach rumbles. You are so hungry you could die."
	
	else:
		print "You are back where you started."
		
	print "There are three doors. left, right and center."
	print "Which door do you go thru?"
	
	choice = raw_input("> ")
	
	if "left" in choice:
		triangle_room(entered_blue_room)
	elif "center" in choice:
		circle_room(entered_blue_room)
	elif "right" in choice:
		rectangle_room(entered_blue_room)
	else:
		dead("You choose to starve.")

start(False, True)