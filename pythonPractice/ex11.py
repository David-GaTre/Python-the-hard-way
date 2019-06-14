#the comma at the end is for it to does not start in a new line
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %s tall and %r heavy." % (
	age, height, weight)

#now cool coded questions
favorite_animal = raw_input("What's your favorite animal? ")
favorite_band = raw_input("What's your favorite band? ")

print "So, your favorite animal is %s and your favorite band is %s... COOL!" % (
	favorite_animal, favorite_band)
#for getting numbers we can try something like x = int(raw_input()) 