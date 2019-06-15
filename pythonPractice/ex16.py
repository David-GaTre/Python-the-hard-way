#file commands to remember
#close: like File -> Save
#read: reads the contents of the file, you can assign it to a variable.
#readline: like getline from c++
#truncate: empties the file
#write: to write stuff on the file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
#print "First, we'll read what you have..."
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#it waits for the user to press enter
raw_input("?")

#The 'w' stands for permission to write in the file, puts it in write mode
#just using the w will truncate the file
print "Opening the file..."
target = open(filename, 'w')


print "Truncating the file. Goodbye!"
#due to 'w' we can comment the truncate function
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
