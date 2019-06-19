#in resume, this function prints the cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers) :
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
#here the int() parse the values into integers, probably we will see a better
#way to do it onward	
def sum (x, y) :
	return int(x) + int(y)
	
#calls the function with just two numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#calls the function, but now with variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calls the functionagain, but does the math, note the commas
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

#here it makes the combination of math and variables, not the commas
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "From here onward, they are just function tests, just ignore, tks :)"

print "Okay, we will try with user inputted data."
first = raw_input("Write a number: ")
second = raw_input("Write another number: ")

#Yay, we can also reference the sum function
print "Your result is: %d" % sum(first,second)

print "Okay, we've learned enough for today"