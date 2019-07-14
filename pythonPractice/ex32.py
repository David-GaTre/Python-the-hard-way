the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# if you wish to do matrices, like in c++, you can
# list = [[1, 2], [3, 4]] 

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in items
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts, range grabs an argument and goes 
# through it one by one, in this case, it would be the same to say range(6)
# goes from 0 to 5, does not count the last one
for i in range(0,6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)	
	# append() function adds an element at the end of the list
	
# now we can print them out too
for i in elements: 
	print "Element was: %d" % i