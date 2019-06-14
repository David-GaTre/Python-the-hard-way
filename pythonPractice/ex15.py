from sys import argv

script, filename = argv

#i really like variables in python, just type the name
#open function is like in c++ function
txt = open(filename)

print "Here's your file %r:" % filename
#read function is like ifstream in c++, functions are used with a dot, like c++
#with the variable behind
print txt.read()

#as in c++, close files regularly although python does not mark error
#syntax fileObject.close()
txt.close()

#Here we recieve the name of the txt file
print "Type the filename again:"
file_again = raw_input("> ")

#this shows that can also be done with raw_input, it inputs the file into a variable
#in other words, creates a file object 
txt_again = open(file_again)

#this reads the txt file
print txt_again.read()

txt_again.close()

