
import time
import random
from typing import Set, cast
import termcolor
import playsound

keeploop2 = 11
room2progression = 0
inventory = []
objectsr1 = [ "puppy", "unicorn", "ice cream sundae", "friendly dragon" ]
objectsr2 = ["ice", "snow", "pinecones", "half a carrot", "full can of beans"]
objectsr3 = ["fancy bow", "scissors", "sparkles", "baloon"]
setchapter = 1
room3empty = 4
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
    line()
    global setchapter
    if setchapter == 1:
        print ("Try interacting with everything in the room!")
    elif setchapter == 5:
        print ("Try the inventory command! Youll find you can do things with your items")
    elif setchapter >= 10:
        print ("Almost everything in your inventory and around you has a purpose, just use everything you have!")
    return

def happinessbar():
    smiles = [":|", ":]", ":}", ":)", ":D"]
    print (smiles)
    return

def happiness(happyCheck):
    if happyCheck == "happiness":
        happinessbar()

def debugmode():
    print ("setchapter is - ", setchapter)
    print ("room2progression is - ", room2progression)
    print ("room3empty is - ", room3empty)

def interactchoice():
    global setchapter
    line()
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
    line()
    print("Sorry! That is  not (or no longer is) a valid input!")
    print("Please print something else!")
    print("If you're stuck, try the hint command!")

    return


def incorrectnarrationprogression2():
    line()
    print ("That could work, mabye if you just come back to it later")
    if room2progression == 0:
        print ("Everythings still covered in ice. Mabye fire could melt it")
    if room2progression == 1:
        print ("Now theres a lot of water everywhere. Something magical could clear it!")
    if room2progression == 2:
        print ("Just relax for a bit")
    if room2progression == 3:
        print ("You only have 1 thing left in your inventory")
    if room2progression > 4:
        print ("Nothing in your inventory is useful right now")

        
    return

def incorrectnarrationvariation():
    line()
    print ("That is a suprise tool that will be useful later!")
    print ("You'll know when its time to use this!")


def helpcommands():
    line()
    print ("'look around' - use it when you first enter a room to know what you can interact with")
    print ("'help' - prints this message")
    print ("'hint' - gives you a hint about what to do next in your current room")
    print ("'interact' - interact with something and put it in your inventory")
    print ("'inventory - opens your inventory'")
    print ("'happiness' - opens your happiness bar")
    return


def inventoryuser2():
    line()
    global room2progression
    global setchapter
    if setchapter >= 3 and setchapter <= 8:
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
                print ("After a burst of fire, the room is covered in water, but no longer frozen")
                room2progression += 1
                inventory.remove("friendly dragon")
            else:
                incorrectnarrationprogression2()
        elif "ream" in inventoryinteract:
            if room2progression == 3:
                print ("You eat the ice cream. It allows you to see everything in the room more clearly")
                narratortalk("You may interact with items in the room now")
                room2progression += 1
                inventory.remove("ice cream")
                setchapter += 1
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
    elif setchapter >= 9:
        print ("What would you like to interact with?")
        print (inventory)
        inventoryinteract = input()
        if "bean" in inventoryinteract:
            print ("You take out the can of beans")
            inventory.remove("can of beans?")
            print ("You eat the beans")
            print ("Nothing really happens, but you feel less hungry")
        elif "ice" in inventoryinteract:
            print ("The ice is quite cold, but you take it out")
            inventory.remove("ice")
            setchapter += 2
            print ("as the ice melts into the water, you notice a horse dish it starts to fill up")
        elif "pinecone" in inventoryinteract:
            print ("Thats a really nice pinecone")
            print ("If only we could find a use for it")
        elif "carrot" in inventoryinteract:
            if setchapter >= 11:
                print ("A horse comes out and eats the carrot out of your hand")
                inventory.remove("half a carrot")
                setchapter += 1
                print ("the horse opens the way for a door")
                narratortalk ("did he just ram through the wall?")
                print ("the room contains some glue, which you grab")
                inventory.append("glue")
            else:
                incorrectnarrationvariation()
        elif "glue" in inventoryinteract:
            if setchapter >= 12:
                print ("You use the glue")
                print ("you connect the pinecone to the baloon nearby")
                print ("its a strange gift?")
                inventory.remove("glue")
                inventory.remove("pinecone")
                inventory.append("gift?")
                setchapter += 1
            else:
                incorrectnarrationvariation()
        elif "gift" in inventoryinteract:
            print ("work on it some more before you present it!")
        elif "bow" in inventoryinteract:
            if setchapter == 13:
                print ("you add the funky bow to the gift")
                inventory.remove("bow")
                setchapter += 1
            else:
                incorrectnarrationvariation()
        elif "sparkle" in inventoryinteract:
            if setchapter == 14:
                print ("you add sparkles to the gift")
                inventory.remove("sparkles")
                setchapter += 1
            else:
                incorrectnarration()
        elif "scissor" in inventoryinteract:
            if setchapter == 15:
                print ("you trim the edges of the gift, polishing it up")
                inventory.remove("scissors")
                setchapter += 1
            else:
                incorrectnarrationvariation()



    else: 
        print ("Not right now. Try to interact?")






def interactchoice2():
    line()
    global setchapter
    if setchapter <= 5:
        print ("Mabye try later? Your inventory is a good place to look for now")
    else:
        print ("What would you like to interact with?")
        print (objectsr2)
        actinteract2 = input()
        if "ice" in actinteract2:

            objectsr2.remove("ice")
            print ("the ice glows faintly.")
            print ("you collect it")
            inventory.append("ice")
            narratortalk ("It's great to see you so happy!")
            setchapter += 1

        elif "pinecone" in actinteract2:
            objectsr2.remove("pinecones")
            print ("This might be useful for making a gift later")
            inventory.append("pinecone")
            setchapter += 1
        elif "now" in actinteract2:
            objectsr2.remove("snow")
            objectsr2.append("narrator")
            print ("The snow melts in your hand.")
        elif "carrot" in actinteract2:
            objectsr2.remove("half a carrot")
            inventory.append("half a carrot")
            setchapter += 1
            print ("Looks useful for taming a horse")
        elif "beans" in actinteract2:
            print ("you scoop up the can of beans")
            print ("you know, Heizn beans arent that bad")
            print ("you know another time as a child I ate beans and I was sad after I ate them")
            inventory.append("can of beans?")
            objectsr2.remove("full can of beans")
            setchapter += 1
        elif "arrator" in actinteract2:       
            if setchapter >= 6:
                print ("You ask the narrator how he is doing")
                narratortalk("Its ok, but I'm not feeling well, I could use someone to make me feel better")
                narratortalk ("Thanks for asking. I feel much better now")
                objectsr2.remove("narrator")
            else:
                print ("Mabye try talking to him later")


def inventoryopen():
    line()
    print (inventory)
    narratortalk("Would you like to interact with something?")
    yaynay = input("Yes/No ----------->  ")
    if "es" in yaynay:
        inventoryuser2()
    else:
        print ("Sorry, that is not a good answer")

    return





def room1options(room1):
    line()
    if room1 == "interact" and setchapter == 5:
        nextchapter()
    elif room1 == "interact":
        interactchoice()
    elif room1 == "hint":
        givehint()
    else:
        incorrectnarration()



def room2setting():
    line()
    ominoustalk("It is very cold")
    ominoustalk("Its snowy and wet all around")
    ominoustalk("You see many things around you")
    print ("You see", objectsr2)

    return




def interactchoice3():
    line()
    global setchapter
    global room3empty
    if room3empty == 0:
        print ("its probably a good time to mess with your inventory")
    else:
        print ("what would you like to interact with?")
        print (objectsr3)
        actinteract3 = input()
        if "bow" in actinteract3:
            print ("you grab the bow from the table")
            objectsr3.remove("fancy bow")
            inventory.append("bow")
            room3empty -= 1
        elif "cisso" in actinteract3:
            print ("you grab the scissors")
            print ("SAFELY")
            objectsr3.remove("scissors")
            inventory.append("scissors")
            room3empty -= 1
        elif "parkle" in actinteract3:
            print ("you grab the bottle of sparkles")
            objectsr3.remove("sparkles")
            inventory.append("sparkles")
            room3empty -= 1
        elif "aloon" in actinteract3:
            print ("mabye try to make use of that later?")
            room3empty -= 1
            objectsr3.remove("baloon")
        else:
            incorrectnarration()


def room2options(room2):
    line()
    global setchapter
    global keeploop3
    if setchapter == 10:
        print ("Looks like you're ready to move on!")
        print ("you go into the next room")
        keeploop3 += 6789
    elif room2 == "look around":
        room2setting()
    elif room2 == "hint":
        givehint()
    elif room2 == "inventory":
        inventoryopen()
    elif room2 == "interact":
        interactchoice2()
    elif room2 == "help":
        helpcommands()
    elif room2 == "happiness":
        happinessbar()
    elif room2 == "debughornet":
        debugmode()
    else:
        incorrectnarration()
        

def room3options(room3):
    line()
    global keeploop4
    global setchapter
    if setchapter == 16:
        keeploop4 += 11345444
    elif room3 == "look around":
        print ("the room is decorated well")
        print ("You see a variety of things around you, such as ...")
        print (objectsr3)
    elif room3 == "help":
        helpcommands()
    elif room3 == "inventory":
        inventoryopen()
    elif room3 == "happiness":
        happinessbar()
    elif room3 == "hint":
        givehint()
    elif room3 == "interact":
        interactchoice3()
    elif room3 == "debughornet":
        debugmode()
    else:
        incorrectnarration()






keeploop = 10
sarca1 = 0
keeploop3 = 21
keeploop4 = 31






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
narratortalk ("I'm glad that you're doing so well")
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
print ("You look around")
print ("It looks like your house in the winter")
print ("There is a lot of ice everywhere, things seem to be frozen off")


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
print ("This is probably the last room!")


while keeploop4 == 31:
    room3input = input()
    room3options(room3input)


print ("you present your gift box to the narrator")
print ("he seems very happy")
time.sleep(1)
narratortalk("Oh")
narratortalk("So you've made it to the end of the game")
time.sleep(1)
narratortalk("Congrats!")
narratortalk("I hope you had fun on your journey")
narratortalk("Thank you again for all the help you've given me!")
time.sleep(2)
narratortalk("Ill be going now")
narratortalk("I do have one last thing for you though!")
time.sleep(1)
print ("Inventory item obtained! - Gift box")
print ("The narrator leaves the room")
time.sleep(2)
inventory.append("gift box")
print ("you might want to open your inventory one last time")

endgame = False
while endgame == False:
    playerlastaction = input()
    if "inventory" in playerlastaction:
        print ("you check your inventory")
        print ("just the gift the narrator has given you")
        print ("you open it")
        time.sleep(2)
        print ("a rabbit hops out of the box")
        time.sleep(2)
        print ("You suppose you've always wanted one!")
        print ("/__   \ |__   __ _ _ __ | | _____   / _| ___  _ __   _ __ | | __ _ _   _(_)_ __   __ _  / |")
        print ("  / /\/ '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__| | '_ \| |/ _` | | | | | '_ \ / _` |/  /")
        print (" / /  | | | | (_| | | | |   <\__ \ |  _| (_) | |    | |_) | | (_| | |_| | | | | | (_| /\_/ ")
        print (" \/   |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|    | .__/|_|\__,_|\__, |_|_| |_|\__, \/")
        print ("                                                    |_|            |___/         |___/     ")
        time.sleep(5)
        narratortalk("The end!")
        endgame = True
    
    else:
        print ("go on!")
        print ("open the box!")



#print ("   __  _ __  _   ___  _____ ___  ___    ____  _   _ __ ___ ")
#print (" ,'_/ /// /.' \ / o |/_  _// _/ / o |  / __/,' \ /// // o |")
#print ("/ /_ / ` // o // _,'  / / / _/ /  ,'  / _/ / o |/ U //  ,'")
#print ("|__//_n_//_n_//_/    /_/ /___//_/`_\ /_/   |_,' \_,'/_/`_|")
#Conclude the game, all those things, dont affect the score at all
#DLC will come at later date
#TBA