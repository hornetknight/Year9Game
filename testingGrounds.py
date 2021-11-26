import time
import random
from typing import cast
import termcolor
import playsound
inventory = []
objectsr1 = [ "puppy", "unicorn", "ice cream sundae", "friendly dragon" ]
keeploop2 = 11

def line():
    print("--------------------")

def longline():
    print("---------------------------------------------------------------------------------------------------------")

def interactchoice():
    print("what would you like to interact with?")
    print (objectsr1)
    actinteract = input()
    if "upp" in actinteract:
        print ("You interact with the puppy. Seeing it makes you happier")
    elif "nico" in actinteract:
        print ("You see the unicorn")
    else:
        print ("That is not a valid thing to interact with")
    
    return


def interact1(room1):
    if room1 == "interact":
        interactchoice()




print ("Type 'interact' ")

while keeploop2 == 11:
    room1inpt = input()
    interact1(room1inpt)





