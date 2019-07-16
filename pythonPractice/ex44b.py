class Parent (object):

	def override(self):
		print "PARENT override()"
		
class Child (Parent):
	
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override() 

#Notes:
#like in c++ the function, although called the same, will be executed depending on the
#object type if a virtual is applied, here the definition is by object (like polymorphism)