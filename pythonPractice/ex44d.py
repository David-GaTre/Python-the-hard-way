class Parent (object):

	def override(self):	
		print "PARENT override()"
	
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child (Parent):
	
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

#actual common use of super():
#class Child(Parent):
#	def __init__(self, stuff):
#		self.stuff = stuff
#		super(Child, self).__init__()
#here you inherit the parent properties		