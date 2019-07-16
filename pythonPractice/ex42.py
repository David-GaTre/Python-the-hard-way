# Animal is-a object 
class Animal(object):
	pass
	
# With these you are saying that dog is an animal, this is inheritance
class Dog(Animal):
	
	def __init__(self, name):
		# here we add a property of dogs
		self.name = name
		
	def talk(self):
		print "Woof!"
			
#here we create another child class, that is also an animal
class Cat(Animal):
	
	def __init__(self, name):	
		# here we add a property of dags, curiously, is the same as dogs'
		self.name = name
	
	def talk(self):
		print "Meow"
				
# Person is-a object
class Person (object):
	
	def __init__(self, name):
		#A person has a name, is a propery
		self.name = name
		
		#Person has-a pet of some kind, by default, they don't have
		self.pet = None
		
#Employee class, is a person
class Employee (Person):
	
	def __init__(self, name, salary):
		#Some compostion magic, the super() gives access to the superclass' methods
		#super() by itself returns a temporary object of the superclass
		#it is useful to extend the functionality of a class
		#a good example at the bottom
		super(Employee, self).__init__(name)
		#A new property, salary
		self.salary = salary
		
#new class, Fishes BOOM
class Fish (object):
	pass
	
#a kind of fish, a child class named salmon
class Salmon (Fish):
	pass
	
#another kind of Fish
class Halibut (Fish):
	pass
	
	
#rover is-a Dog
rover = Dog("Rover")

#satan is-a Cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

#mary has-a pet named satan
mary.pet = satan

#frank is an employee and has a name and a salary
frank = Employee("Frank", 120000)

#frank's pet is rover
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()

satan.talk()
frank.pet.talk()

#6 if you add after the class name (like "Employee) another object, it will have
#multiple inheritance
#Notes:
#You can add class variabl if you put after the class the variable
#just the line before the __init__, it will share this atribute between instances
#for example if add kind = 'canine' in Dog, and you create two Dog objects (call'em
#a and b and you put a.kind and b.kind, both will return 'canine', and if modified
#in one, all will be modified

#How to use super(), extracted from https://realpython.com/python-super/, not sure if only works in Python 3
#class Rectangle:
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width
#
#    def area(self):
#        return self.length * self.width
#
#    def perimeter(self):
#        return 2 * self.length + 2 * self.width
#
#class Square(Rectangle):
#    def __init__(self, length):
#        super().__init__(length, length) #this makes that the lenght is the same on both sides, what happens is that it really is a rectangle with sides of the same lenght (just as the real world!)
#
#class Cube(Square):
#    def surface_area(self):
#        face_area = super().area()
#        return face_area * 6
#
#    def volume(self):
#        face_area = super().area()
#        return face_area * self.length
#
#Note that there is no __init__() in the Cube, as it is only a collection of squares (previously made objects)
#thus, we can define a cube object by just cubito = Cube(3) (and it will have lenght
#3) and you can do cubito.surface_area() (it's 54 btw) 