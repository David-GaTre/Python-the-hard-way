from sys import argv

#added a new argument(parameter), friend_name
script, user_name, friend_name  = argv
#changed prompt
prompt = 'ANSWER: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "How about %r?" % friend_name
f_like = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
And your friend %r. I really don't care about him.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, f_like, lives, computer)