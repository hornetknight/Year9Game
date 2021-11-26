import time
import random
from typing import cast
import termcolor
import playsound

keeploop2 = 11
room2progression = 0
inventory = []
objectsr1 = [ "puppy", "unicorn", "ice cream sundae", "friendly dragon" ]
objectsr2 = ["ice", "snow", "pinecones", "half a carrot", "full can of beans"]
setchapter = 1
def line():
    print("--------------------")

def nextchapter():
    global keeploop2
    print ("Looks like you've found all the items in this room!")
    print ("Lets move onto the next room")
    keeploop2 += 9000

    return

def narratortalk(narratortext):
    printnartext = termcolor.colored(narratortext, 'green', 'on_white')
    print (printnartext)

def ominoustalk(ominoustext):
    printomitext = termcolor.colored(ominoustext, 'red', 'on_grey')
    print (printomitext)

def givehint():
    global setchapter
    if setchapter == 1:
        print ("Try interacting with everything in the room!")
    elif setchapter == 5:
        print ("Try the inventory command! Youll find you can do things with your items")
    return

def happinessbar():
    smiles = [":|", ":]", ":}", ":)", ":D"]
    print (smiles)
    return

def happiness(happyCheck):
    if happyCheck == "happiness":
        happinessbar()

def interactchoice():
    global setchapter
    print("what would you like to interact with?")
    print (objectsr1)
    actinteract = input()
    if "upp" in actinteract:
        print ("You interact with the puppy. Seeing it makes you happier")
        objectsr1.remove("puppy")
        inventory.append("puppy")
        setchapter += 1 
    elif "nico" in actinteract:
        print ("You see the unicorn. It looks nice")
        objectsr1.remove("unicorn")
        inventory.append("unicorn")
        setchapter += 1 
    elif "ream" in actinteract:
        print ("You eat the ice cream. It makes you happier")
        objectsr1.remove("ice cream sundae")
        inventory.append("ice cream")
        setchapter += 1 
    elif "ragon" in actinteract:
        print ("You ride on the dragons back for it bit. It makes you happier")
        objectsr1.remove("friendly dragon")
        inventory.append("friendly dragon")
        setchapter += 1
    else:
        print ("That is not a valid thing to interact with")
    
    return


def incorrectnarration():
    print("Sorry! That is  not (or no longer is) a valid input!")
    print("Please print something else!")
    print("If you're stuck, try the hint command!")

    return


def incorrectnarrationprogression2():
    print ("That could work, mabye if you just come back to it later")
    if room2progression == 0:
        print ("Everythings still covered in ice. Mabye fire could melt it")
    if room2progression == 1:
        print ("Now theres a lot of water everywhere. Something magical could clear it!")
    if room2progression == 2:
        print ("Just relax for a bit")
    if room2progression == 3:
        print ("You only have 1 thing left in your inventory")
    else:
        ominoustalk ("You broke the game")

    return

def helpcommands():
    print ("This is a placeholder for until I get this part done")

    return


def inventoryuser2():
    global room2progression
    print ("What would you like to interact with?")
    print (inventory)
    inventoryinteract = input()
    if "upp" in inventoryinteract:
        if room2progression == 2:
            print ("You interact with the puppy")
            print ("The puppy makes you more relaxed")
            room2progression += 1
            inventory.remove("puppy")
        else:
            incorrectnarrationprogression2()
    elif "ragon" in inventoryinteract:
        if room2progression == 0:
            print ("You ask the dragon to melt the room for you")
            room2progression += 1
            inventory.remove("friendly dragon")
        else:
            incorrectnarrationprogression2()
    elif "ream" in inventoryinteract:
        if room2progression == 3:
            print ("You eat the ice cream. It allows you to see everything in the room more clearly")
            narratortalk("You may interact with items in the room now")
            room2progression += 1
            inventory.remove("ice cream sundae")
        else:
            incorrectnarrationprogression2()
    elif "nicor" in inventoryinteract:
        if room2progression == 1:
            print ("the unicorn looks at the melted room, and clear up all the water")
            room2progression += 1
            inventory.remove("unicorn")
        else:
            incorrectnarrationprogression2()
    else:
        incorrectnarration()



def inventoryopen():
    print (inventory)
    narratortalk("Would you like to interact with something?")
    yaynay = input("Yes/No ----------->  ")
    if "es" in yaynay:
        inventoryuser2()
    else:
        print ("ok")

    return





def room1options(room1):
    if room1 == "interact" and setchapter == 5:
        nextchapter()
    elif room1 == "interact":
        interactchoice()
    elif room1 == "hint":
        givehint()
    else:
        incorrectnarration()



def room2setting():
    ominoustalk("It is very cold")
    ominoustalk("Its snowy and wet all around")
    ominoustalk("You see many things around you")
    print ("You see", objectsr2)

    return




def room2options(room2):
    if room2 == "look around":
        room2setting()
    elif room2 == "hint":
        givehint()
    elif room2 == "inventory":
        inventoryopen()
#    elif room2 == "interact":

    elif room2 == "help":
        helpcommands()
    elif room2 == "happiness":
        happinessbar()
    else:
        incorrectnarration()
        






keeploop = 10
sarca1 = 0
keeploop3 = 21






#So mr narrator man starts sad. Goal is to get him happy by the end of the game
print ("Our story starts here")
print ("God I hate it when storys start like that")
print ("Let's just get this first part")
print ("So whats your name?")
name = input("Enter your name --------->")
print (name, "? Thats rather strange")
time.sleep(1)
print ("Anyhow," , name, ",lets continue on")
time.sleep(2)
#Yeah so CHP 1 starts. Just collect thingys for now
print ("_______________________________________________________________________________________________")
print ("(  ____ \|\     /|(  ___  )(  ____ )\__   __/(  ____ \(  ____ )     (  ___  )( (    /|(  ____ |")
print ("| (    \/| )   ( || (   ) || (    )|   ) (   | (    \/| (    )|     | (   ) ||  \  ( || (    \/")
print ("| |      | (___) || (___) || (____)|   | |   | (__    | (____)|     | |   | ||   \ | || (__ ")
print ("| |      |  ___  ||  ___  ||  _____)   | |   |  __)   |     __)     | |   | || (\ \) ||  __)")
print ("| |      | (   ) || (   ) || (         | |   | (      | (\ (        | |   | || | \   || ( ")
print ("| (____/\| )   ( || )   ( || )         | |   | (____/\| ) \ \__     | (___) || )  \  || (____/")
print ("(_______/|/     \||/     \||/          )_(   (_______/|/   \__/     (_______)|/    )_)(_______/")
print ("-----------------------------------------------------------------------------------------------")

time.sleep(2)
print ("So here we are!")
print ("Welcome to the game! Might as well understand how this whole thing works shall we?")
print ("You have a happiness bar! You can check it at any time by typing 'happiness'")
print ("Try it now")
playerInp1 = input()
happystartcorrect = False
while not happystartcorrect:
    if 'happiness' in playerInp1.lower():
        happystartcorrect = True
    else:
        ominoustalk("TYPE IN THE WORD 'HAPPINESS'")
        time.sleep(2)
        quit()

happinessbar()
print ("Feel free to check at anytime! (An input is allowed)")
time.sleep(2)
print ("Lets get to this room")
print ("The room you are currently in has big grey walls.")
print ("Oh, and you should probably know the goal of this game")
print ("The goal is to be the happiest you can be by the end of it")
print ("You remember that happiness bar from earlier? Yeah, get that to the max, or I suppose keep it in your case")
print ("SO, In front of you is a large door. Let us enter shall we?")


ominoustalk("You enter the huge castle in front of you")

while keeploop == 10:
    room1start = input()
    if "ook aroun" in room1start:
        print ("You observe your surroundings. You find a puppy, unicorn, dragon, and an ice cream sundae nearby.")
        keeploop += 9
    else:
        print ("...") 
        narratortalk("You can choose to look at your surroundings when you first enter a room with 'look around'")
        narratortalk("Go ahead and try")
        


while sarca1 < 4:
    room1act = input()
    if "ook aroun" in room1act:
        print ("You observe your surroundings. You find a puppy, unicorn, dragon, and an ice cream sundae nearby.")
        sarca1 += 10
    else:
        print ("...")
        sarca1 += 1

if sarca1 < 6:
    narratortalk("You know, Ill just make the game move on, this is getting sad")
    print ("Type 'interact' then the object you want to interact with to interact with an item")
else:
    narratortalk("After this, the most basic function is 'interact'. Print it followed by the item you want to interact with in the next input")

print ("An example is like 'interact'. Then it will ask about what you are interacting with. You would type 'puppy' the following sentence")

while keeploop2 == 11:
    room1input = input()
    room1options(room1input)

time.sleep(3)    
print ("   ________  _____    ____  ________________     _______       ______ ")
print ("  / ____/ / / /   |  / __ \/_  __/ ____/ __ \   /_  __/ |     / / __ ]")
print (" / /   / /_/ / /| | / /_/ / / / / __/ / /_/ /    / /  | | /| / / / / /")
print ("/ /___/ __  / ___ |/ ____/ / / / /___/ _, _/    / /   | |/ |/ / /_/ / ")
print ("\____/_/ /_/_/  |_/_/     /_/ /_____/_/ |_|    /_/    |__/|__/\____/ ")
#LOTS OF BAD STUFF HAPPEN
#just deimate happniess here
ominoustalk("So a wonderful journey you had!")
print ("New commands unlocked!")
print ("Inventory - see what you are currently holding")
print ("Help, shows you a general list of all actions ")
narratortalk("Yeah, you've sorta been scooping up everything you interact with here")

while keeploop3 == 21:
    room2input = input()
    room2options(room2input)


print ("▄█▄     ▄  █ ██   █ ▄▄     ▄▄▄▄▀ ▄███▄   █▄▄▄▄        ▄▄▄▄▀ ▄  █ █▄▄▄▄ ▄███▄   ▄███▄  ")
print ("█▀ ▀▄  █   █ █ █  █   █ ▀▀▀ █    █▀   ▀  █  ▄▀     ▀▀▀ █   █   █ █  ▄▀ █▀   ▀  █▀   ▀ ")
print ("█   ▀  ██▀▀█ █▄▄█ █▀▀▀      █    ██▄▄    █▀▀▌          █   ██▀▀█ █▀▀▌  ██▄▄    ██▄▄  ")
print ("█▄  ▄▀ █   █ █  █ █        █     █▄   ▄▀ █  █         █    █   █ █  █  █▄   ▄▀ █▄   ▄▀ ")
print ("▀███▀     █     █  █      ▀      ▀███▀     █         ▀        █    █   ▀███▀   ▀███▀   ")
print ("         ▀     █    ▀                     ▀                  ▀    ▀                    ")
#Gain some back, not too much though

print ("   __  _ __  _   ___  _____ ___  ___    ____  _   _ __ ___ ")
print (" ,'_/ /// /.' \ / o |/_  _// _/ / o |  / __/,' \ /// // o |")
print ("/ /_ / ` // o // _,'  / / / _/ /  ,'  / _/ / o |/ U //  ,'")
print ("|__//_n_//_n_//_/    /_/ /___//_/`_\ /_/   |_,' \_,'/_/`_|")
#Conclude the game, all those things, dont affect the score at all