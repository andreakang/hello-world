# let the user know what's going on
print ("Welcome to Bel-Air!")
print ("Answer the questions below to play.")
print ("-----------------------------------")


direction1 = raw_input ("Name a direction. Left, right, upside-down...")
time = raw_input ("Choose a window of time: ")
verb = raw_input ("Choose a verb: ")
royalty = raw_input ("Name a royal title: ")
place = raw_input ("Name a place that kids play: ")
shoot = raw_input("Name something you shoot: ")
hooligans = raw_input ("Name an adjective for hooligans: ")
blank = raw_input("Fill in the blank 'Started making ____: ")
town = raw_input("What is the name of the town or city you grew up in?: ")
emotion = raw_input("Name a negative emotion: ")


# this is the story. it is made up of strings and variables.
story = "Now this is a story all about how / " + "My life got flipped-turned " +  direction1 + ". " \
+ "And I'd like to take a " + time + " / Just " + verb + " right there. / " \
"I'll tell you how I became the " + royalty + " of a town called Bel-Air. / " \
"In " + town + " born and raised. / " \
"On the " + place + " was where I spent most of my days. / " \
"Chillin' out maxin' relaxin' all cool. / " \
"And all shooting some " + shoot + " outside of the school. / " \
"When a couple of " + hooligans + " who were up to no good. / " \
"Started making " +  blank + " in my neighborhood. / " \
"I got in one little fight and my mom got " + emotion + ". / " \
"She said, 'You're movin' with your auntie and uncle in Bel-Air.'"



print (story)