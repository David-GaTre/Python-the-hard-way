i = 0 
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	#writing the list numbers prints all the list with the [] 
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num

#Study Drills	
def use_while(n,skip):
	numbers1 = []
	i = 0
	while i < n:
		print "At the top i is %d" % i
		numbers1.append(i)

		i = i + skip
		#writing the list numbers prints all the list with the [] 
		print "Numbers now: ", numbers1
		print "At the bottom i is %d" % i
	
print "Today i woke up feeling like usint the use_while function! with... 4"
use_while(4,1)
print "\nNow with... 3!"
use_while(3,1)
print "\nNow skipping 2 by 2"
use_while(3,2)

#5 if you don't get rid of the + 1 it will add one extra
	

	