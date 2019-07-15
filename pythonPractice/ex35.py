from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")

	try:
		how_much = int(next)
		if how_much < 50:
			print "Nce, you're not greedy, you win!"
			exit(0)
		else:
			dead("You greedy bastard!")
	except ValueError:	
		dead("Man, learn to type a number.")
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	#infinite loop
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()

#the exit(0) ends the program, simliar to the return 0 in c++

# Study Drills
#4 is better to check when transforming to int, if you get ValueError, then, it is not
# Details at the bottom
#5 int() returns a number 

# original code in line 6 was like this :
#	next = raw_input("> ")
#if "0" in next or "1" in next:
#	how_much = int(next)
#else:
#	dead("Man, learn to type a nu
#if how_much < 50:
#	print "Nice, you're not greed
#	exit(0)
#else:
#	dead("You greedy bastard!")

# the try function block lets you test a block of code for errors
# the except executes the code in case of error, there are various errors
# in this case, as the value is not valid if you input a string of letters
# you get a ValueError, thus, it executes the exception block