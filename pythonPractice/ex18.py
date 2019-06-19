#this one is like your scripts with argv
def print_two(*args) :
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
#the '*' tells python to take all the arguments of the function and put it
#into a list, not used that much
	
#ok, that *args is actualy pointless, we can just do this
def print_two_again(arg1, arg2) :
	print "arg1: %r, arg2, %r" % (arg1, arg2)
	
#this just takes one argument
def print_one(arg1) :
	print "arg1: %r" % arg1
	
#this one takes no arguments
def print_none() :
	print "I got nothin'."
	
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#Steps for defining functions:
#1. use def for "define"
#2. write the function name, should be short and meaningful
#3. we tell the arguments.
#4. write ':' for we to start to write the script
#5. write the script, WITH INDENTION (aka, the TAB)