#this means we work with command line arguments, from where we execute our 
#code, in my case, in PowerShell
#this are called modules, as libraries in c++ (referring to sys)
from sys import argv

#difference between argv and raw_input(), argv is inputted in the command line (reads as string)
#while raw_input() is while the script is running
#we need to run it using 3 parameters apart from the name of the script
#as "python ex13.py one two yeehaw, don't write more or less, it won't run
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third