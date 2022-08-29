# We gonna learn how we can concatnate two strings together
# what is madlib ? Pick a story from any category and fill in a word for each prompt. example - Do you know about ____ ?

#How can you do this ? for this there are three methods where you can fill the blank with your own choice of word and print it out.
 
# Let's write what are the 3 ways

# First lets create one variable and leave it as blank for now

'''adjective = "GOD"  
'''

#First method to write this or concatanate

'''print("Do you know about " + adjective )
'''
# Second way to print this is 
# what this format fucntion do ? whatever you will pass in the format function will come under the curly braces{}
'''print("Do you know about {}".format(adjective))
'''
# Third way to do this is 
#f in the start means the f-string which means just by prepending f in the fron of string you will be able to add the variable directly in curly braces.

'''print(f"Do you know about {adjective}")
'''
# what will happen if I run this , it will give me 3 output do you know about ___ because adjective is having no value right now.
# if you will assign value to adjective you will see 3 output do you know about  (Adjective value(whater you assigned)) F-string is the cleanest way to express string concatanation


#Let's ask user to enter the value and print the vwhole sentance



# we have used f-string method to write the madlib and we have asked user to fill the blanks we have put under the curly bracess.
#In the end we are printing the madlib

adj = input("Adjective Value: ")
verb1 = input("Verb1: ")
verb2 = input("verb2: ")
Hero = input("Your hero :")
madlib = f"{adj} is so easy to understand. It will help you to understand {verb1} and you will definetely feel {verb2}.\
 Just like my famous hero {Hero}"
print(madlib)

# This / is used to go into the next line
