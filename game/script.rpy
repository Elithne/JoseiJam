# The script of the game goes in this file.
# Characters 
define al = Character("Alex", color="#ffffff")
define be = Character("Bernard", color="#ffffff")
define ex = Character(". . .", color="#ffffff")
define ma = Character("Marcos", color="#ffffff")
define sa = Character("Sam", color="#ffffff")
define son = Character("Sonal", color="#ffffff")
define jo = Character("Josephine", color="#c3acce")

#Choices
default goodChoiceBernard = 0
default goodChoiceMarcos = 0
default goodChoiceSam = 0
default goodChoiceSonal = 0
default goodChoiceJosephine = 0 #General Ending that will have an impact with how she deals with her breakup.


#--Images--

#Alex
image al sad:
    "sprites/alex/al_sad.png"
    zoom 0.75
image al silhouette:
    "sprites/alex/al_silhouette.png"
    zoom 0.75


#Bernard
#Marcos
#Sam
#Sonal

#Others
image ex:
    "sprites/ex/ex.png"
    zoom 0.75

# The game starts here.

label start:
    scene login
    #Prologue 

    #[intro]
    #real phone screen

    #create new account
    #input name, saving it into Jo's character
    #put player name
    $ playerName = renpy.input(_("My name is..."), default = "Josephine", length=12)
    $ playerName = playerName.strip()

    if playerName == "" or playerName == " ":
        $ playerName = "Josephine"

    $ jo = Character("[playerName]", color="#c3acce")

    show screen login          
    "Login Successful!"
    hide screen login
    jump intro
    

label intro:
    #go to ex's profile
    play music "audio/SAD - A Cool Electric Rainy Night by Mike Durek.mp3" fadein 2
    scene black with fade
    "Love is a wonderful thing."

    "You meet someone, you laugh at their jokes, you fall in love with them."
    show expost1_beach with dissolve
    "And when they're the one, you're just waiting to spend the rest of your life with them."

    #photo of ex
    
    show ex at top with dissolve
    ex "Hey, I don't think this is working out.{w} Us, I mean."

    #transition into bg_workbathroom

    jo "..."
    scene black with fade
    hide all
    stop music fadeout 3.0

    centered "A month later"

    #sfx - toilet flush
    #sfx - sink noises
    #sfx - paper towel noises

    scene bg_workbathroom with fade

    al "...Hello?"

    al "[playerName!q]?"

    #alex in silhouette form

    show al silhouette at top with dissolve

    al "...[playerName!q]! Everything okay?"

    #alex comes into focus?
    show al sad at top with dissolve

    jo "O-oh! Yes! Thank you, everything is fine."

    "How long was Alex speaking to me?? I didn't even realise anyone was here."

    #music begins

    al "Want me to wait for you?"

    jo "No, I'm alright, thanks."

    al "You sure? I don't mind waiting. We can head over together."

    "Together? Where?"

    jo "Sorry, head over to…?"

    al "To the meeting…? It starts in a few minutes."

    "Oof, get it together, [playerName!q]."

    jo "Right! Yes, of course, the meeting."

    "Alex gives me an inquisitive look that borders on concern."

    al "Yes…? So…we'll walk over together? Or…?"

    jo "Yeah, sorry, if you don't mind."

    al "I'll just wait outside then."

    jo "No! I mean– Sorry, we can just head over right now, actually. Thanks."

    al "..."

    al "...You sure you're okay?"

    menu:
        "Insist I'm doing well":
            jump alexIntro
        "Confess all my problems":
            jump alexIntro

    label alexIntro:
        jo "I'm fine, thanks"
        "Or at least, I will be.{w} Probably."
        jo "Shall we?"

        "Alex hesitates to accept my answer at face value. I chant \"I'm fine\" on a loop in my mind and put on a smile to be extra convincing."

        al "..."

        #sped up text here:

        al "...So don't know if you've heard but the word from George in accounting is that Ivy from HR is in a relationship with someone in our department, which, mysteries aside has to be a nightmare for–"

        "Nice. Smooth. Don't think she suspected anything was amiss."

        "Besides…"

    return

