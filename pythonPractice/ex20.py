from sys import argv

script, input_file = argv

#function that reads all of the f file object
def print_all(f):
	print f.read()

#the seek method sets the file's current position, 0 sets it to the start
#1 to the relative to the current position, 2 to the file's end	
def rewind(f):
	f.seek(0)

#function that reads only the next line until an \n is foundt, of the f file object
def print_a_line(line_count, f):
	print line_count, f.readline()
	
#creates a variable with the file to be read
current_file = open(input_file)

print "First let's print the whole file: \n"

#prints all the lines of the file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#returns read position of the file to 0
rewind(current_file)

print "Let's print three lines:"

#calls to the print_a_line function with only prints a single line, 3 times
current_line = 1
print_a_line(current_line, current_file)

#here, current_line is 2, also could be written as current_line += 1
current_line = current_line + 1
print_a_line(current_line, current_file)

#here, current_line is 3
current_line = current_line + 1
print_a_line(current_line, current_file)