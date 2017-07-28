from random import *

# line number 1 (5 syllable)
five = ["Staring at the sun", "It's now or never ", "Where do you belong" , "Come back right away", "I will go with you", "Right across the street", "It is all my fault"]
#This is the second stanza ( 7 syllables)
seven = ["Is this price acceptable?", "It happened by accident", "I'd like to apologize", "The townspeople applauded", "I'm late for an appointment"]
#THis is the third sranza (5 syllable)
third =["Let's try and stay calm.", "Get the camera.", "He lives off campus.", "Stop me if you can!", "I have to cancel.", "Please light a candle."]

#random number picker for the 3 lines
fiveR= randint(0, len(five)-1)
sevenR= randint(0, len(seven)-1)
thirdR= randint(0, len(third)-1)
# prints the haiku
print(five[fiveR] )
print(seven[sevenR] )
print (third[thirdR])
