people = 20
cats = 30
dogs = 15

#if an if statement is truth, it executes every line of the idention (branch)
#after it, remember to ident with tab or with 4 spaces.

if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	

if people == dogs:
	print "People are dogs."
	
#add boolean expresions is easy	

if people == dogs and people < cats:
	print "I think there are more cats than dogs."