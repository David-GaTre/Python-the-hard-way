x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#These two lines print the string that are in x and y variables
print x
print y 
#these two take as reference the variables of x and y using the format characters
print "I said: %r." % x
print "I also said: '%s'." % y
#creates 2 new variables, a boolean one and a string one
hilarous = False
joke_evaluation = "Isn't that joke so funny?! %r"
#prints the joke string and uses false as reerence
print joke_evaluation % hilarous
#creates two strings
w = "This is the left side of..."
e = "a string with a right side."
#w and e strings are concatenated
print w + e 
#there are actually 5 places