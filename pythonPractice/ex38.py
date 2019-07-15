ten_things = "Apples Oranges Crows Telephone Ligh Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff) 
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #prints element in position 1
print stuff[-1] #prints element in las position
print stuff.pop() #prints the last item in the list and pops it out
print ' '.join(stuff) #prints with spaces in between, 'join' joins items in a tuple into a string, using the ' '  as separator
print '#'.join(stuff[3:5]) # same as the past, but from range objects 3 to 5