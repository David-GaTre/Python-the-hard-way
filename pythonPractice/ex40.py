#self makes reference to the same class, used to access the variables beloning
#to the class, if you didn't use any variable, is not necessary
class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	# self.lyrics is the number of line strings in the list
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"With the pocket full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#How classes work in Python
# to create objects, see line 11
# the __init__() function is used to initiate the class, it takes the properties
# just like a constructor in c++, in this case, self and lyrics are the args
# so, it will have a parameter that will be called lyrics, which is a list of
# strings. You could write also print bulls_on_parade.lyrics and it will print
# the list with the []