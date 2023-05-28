# The script of the game goes in this file.
# Characters 
define al = Character("Alex", color="#ffffff")
define be = Character("Bernard", color="#ffffff")
define ex = Character("Joseph", color="#ffffff")
define ma = Character("Marcos", color="#ffffff")
define sa = Character("Sam", color="#ffffff")
define son = Character("Sonal", color="#ffffff")
define jo = Character("Josephine", color="#c3acce")

#Choices
default goodChoiceBernard = 0
default goodChoiceMarcos = 0
default goodChoiceSam = 0
default goodChoiceSonal = 0
default goodChoiceJosephine = 0 #General Good Ending. 


# The game starts here.

label start:
    scene login

    #input name, saving it into Jo's character
    $ playerName = renpy.input(_("My name is..."), default = "Josephine", length=12)
    $ playerName = playerName.strip()

    if playerName == "" or playerName == " ":
        $ playerName = "Josephine"

    $ jo = Character("[playerName]", color="#c3acce")

    show screen login          
    "Login Successful!"
    hide screen login

    scene white
    jo "I have a name now"

    # This ends the game.

    return

