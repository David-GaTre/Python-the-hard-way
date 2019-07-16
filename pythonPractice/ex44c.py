class Parent (object):
	
	def altered (self):
		print "PARENT altered()"
		
class Child (Parent):
	
	def altered (self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() #here we call parent.altered, as with super we get something from the parent class
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()