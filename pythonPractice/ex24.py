#basic escapes \n for newline, \t for tab, \d for a ', and \\ for backslash
print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

#the """ is for indefinite text
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requieres an explanation
\n\t\twhere there is none.
"""

print "---------------"
print poem
print "---------------"

#basic maths
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#function that adds 3 variables
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
#calls the function with a start of 10,000 and assigns them to the 3 variables	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#uses references
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#modifies the value of start_point
start_point = start_point / 10

#calls the function in the reference area
print "We can also do that this way:"
print "We'd have %d, %d jars, and %d crates" % secret_formula(start_point)