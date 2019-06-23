#Returns works just as in C++, with the difference that you don't specify the data
#type at the beggining. By the moment...
def add(a, b):
	print "ADDING %d and %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(50, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzzle for the extra credit
#The normal formula would be age + ( height - ( weight * iq / 2) )
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

#trying to do (age * (weight / 3))- height
ans = substract( height, multiply( age, divide(weight, 3)))
print "The puzzle 2 answer is: ", ans, "Izzi pizzi, right?"