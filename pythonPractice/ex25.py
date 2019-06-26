#the split() divides whatever you have, between the () you put the separater
#by default is a ' ', we write it anyways
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
#sorts the sentence, but it always put capital letters at the beggining
#to avoid this you can change the key like 
#sorted(var, key=lambda v: v.upper())
#obtained from https://stackoverflow.com/questions/13954841/sort-list-of-strings-ignoring-upper-lower-case
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
#pop() takes the value indicated and puts it into the stack, is erased from the
#original, let's call it "list", in this case 0 indicates the first value
def print_first_word(words):
	"""Prints the first words after popping it off."""
	word = words.pop(0)
	print word

#same as the above with the difference of the -1, that takes the last value of the
#"list"
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and return the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
#this exercise is for working out in the console, it is by running python directly
#then write "import ex25", while in the same folder, to create a module for the 
#functions, as we can see, this are only functions. Then, we can create variables
#within the console to work with, as MySentence = "Well, hello there.". There, we
#can execute every function that we want directly like this:
#ex25.sort_sentence(MySentence)
#and we can display what is on each variable by just writing the name of the variable
#
#VERY USEFUL: you can write help(nameOfYourModule) (or name of the function
#in the console (WYSS) for 
#getting help of your own module, that's the usefulness of the sentences after the
#functions, they are useful as documentation. It is displayed like this:
#FILE
#ex25
#FUNCTIONS
#print_last_word
#Prints the last word after popping it off.
#
#That is an example, that's why it is important to document after each function.
#
#VERY USEFUL 2: to avoid writing "ex25." before each function we can also, from
#the import part write it like this "from /nameOfModule/ import *" and then all
#the functions will be there. Be careful when importing various as function names
#could not be overloaded correctly