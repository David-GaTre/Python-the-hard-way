#with import you can get access to code from libraries
from sys import argv
#we get the exists() function
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#in_file = open(from_file)
#indata = from_file.read()
#one liner: indata = open(from_file).read()

#len() measures the length (duh)
#commented due to friendliness
#print "The input file is %d bytes long" % len(indata)

#exists() determines if a file exists or not, a boolean function
#commented due to friendliness
#print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)
#one liner: open(to_file, 'w').write(indata)

open(to_file,'w').write(open(from_file).read())

print "Alright, all done."

#needed to close due that the output file should be saved first (remember that close
#emulates save)
#out_file.close()
#in_file.close()
#at last version you don't need to close because opening and reading/writing
#the file without putting the readed file in a variable first
#in other words, with THESE one liners you don't need to close, as we are not 
#not storing a reference to the open file (in this case, in_file and out_file)
#Python closes it automatically (context manager and interpreters, by default CPython)

#ShadowRanger's note about this obtained from StackOverflow:
#"Note: In the CPython reference interpreter, opening and immediately 
#reading/write-ing to the returned file object (without storing a reference
#to the open file object) happens to be predictable and safe, but that is not the
#case on most other interpreters, and it's not a contractual guarantee of the 
#language (just a side-effect of CPython reference counting). Using with is more
#scalable, portable, and predictable, so always use it, even if it seems like it
#works fine without it. "
#so... wait until learn "with" haha
#also written by Zed in the Common Student Questions section