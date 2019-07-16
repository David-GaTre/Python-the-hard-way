class Parent(object):

	def implicit(self):
		print "PARENT implicit()"
	
class Child(Parent):
	pass #this means it's an empty block
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()