name = 'Zed A. Shaw'
age = 19 #actual age 
height = 74 #inches
weight = 110 #pounds
eyes = 'Black' #looks like a black hole
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
height *= 2.54
print "He's %d centimeters tall." % height
print "He's %d pounds heavy" % weight
weight *= 0.453
print "He's %d kilograms heavy" % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)