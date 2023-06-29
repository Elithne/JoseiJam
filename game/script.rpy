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
image al amused:
    "sprites/alex/al_amused.png"
    zoom 0.75
    
image al angry:
    "sprites/alex/al_angry.png"
    zoom 0.75
    
image al annoyed:
    "sprites/alex/al_annoyed.png"
    zoom 0.75
    
image al embarrassed:
    "sprites/alex/al_embarrassed.png"
    zoom 0.75

image al happy:
    "sprites/alex/al_happy.png"
    zoom 0.75
    
image al laughing:
    "sprites/alex/al_laughing.png"
    zoom 0.75
    
image al nervous:
    "sprites/alex/al_nervous.png"
    zoom 0.75
    
image al neutral:
    "sprites/alex/al_neutral.png"
    zoom 0.75

image al proud:
    "sprites/alex/al_proud.png"
    zoom 0.75

image al sad:
    "sprites/alex/al_sad.png"
    zoom 0.75

image al shocked:
    "sprites/alex/al_shocked.png"
    zoom 0.75

image al silhouette:
    "sprites/alex/al_silhouette.png"
    zoom 0.75

#Bernard
image be amused:
    "sprites/bernard/be_amused.png"
    zoom 0.75
    
image be angry:
    "sprites/bernard/be_angry.png"
    zoom 0.75
    
image be annoyed:
    "sprites/bernard/be_annoyed.png"
    zoom 0.75
    
image be embarrassed:
    "sprites/bernard/be_embarrassed.png"
    zoom 0.75

image be happy:
    "sprites/bernard/be_happy.png"
    zoom 0.75
image be idealized:
    "sprites/bernard/be_idealized.png"
    zoom 0.75
    
image be laughing:
    "sprites/bernard/be_laughing.png"
    zoom 0.75
    
image be nervous:
    "sprites/bernard/be_nervous.png"
    zoom 0.75
    
image be neutral:
    "sprites/bernard/be_neutral.png"
    zoom 0.75

image be proud:
    "sprites/bernard/be_proud.png"
    zoom 0.75

image be sad:
    "sprites/bernard/be_sad.png"
    zoom 0.75

image be shocked:
    "sprites/bernard/be_shocked.png"
    zoom 0.75

# image be silhouette:
#     "sprites/bernard/be_silhouette.png"
#     zoom 0.75

#Marcos
image ma amused:
    "sprites/marcos/ma_amused.png"
    zoom 0.75
    
image ma angry:
    "sprites/marcos/ma_angry.png"
    zoom 0.75
    
image ma annoyed:
    "sprites/marcos/ma_annoyed.png"
    zoom 0.75
    
image ma embarrassed:
    "sprites/marcos/ma_embarrassed.png"
    zoom 0.75

image ma happy:
    "sprites/marcos/ma_happy.png"
    zoom 0.75
    
image ma idealized:
    "sprites/marcos/ma_idealized.png"
    zoom 0.75

image ma inconvenianced:
    "sprites/marcos/ma_inconvenianced.png"
    zoom 0.75
    
image ma laughing:
    "sprites/marcos/ma_laughing.png"
    zoom 0.75
    
image ma nervous:
    "sprites/marcos/ma_nervous.png"
    zoom 0.75
    
image ma neutral:
    "sprites/marcos/ma_neutral.png"
    zoom 0.75

image ma obnoxious:
    "sprites/marcos/ma_obnoxious.png"
    zoom 0.75

image ma proud:
    "sprites/marcos/ma_proud.png"
    zoom 0.75

image ma sad:
    "sprites/marcos/ma_sad.png"
    zoom 0.75

image ma shocked:
    "sprites/marcos/ma_shocked.png"
    zoom 0.75

image ma shocked:
    "sprites/marcos/ma_smug.png"
    zoom 0.75

# image ma silhouette:
#     "sprites/marcos/ma_silhouette.png"
#     zoom 0.75

#Sam
#sam
image sa_home amused:
    "sprites/sam/sa_home_amused.png"
    zoom 0.75
    
image sa_home angry:
    "sprites/sam/sa_home_angry.png"
    zoom 0.75
    
image sa_home annoyed:
    "sprites/sam/sa_home_annoyed.png"
    zoom 0.75
    
image sa_home embarrassed:
    "sprites/sam/sa_home_embarrassed.png"
    zoom 0.75

image sa_home happy:
    "sprites/sam/sa_home_happy.png"
    zoom 0.75
image sa_home idealized:
    "sprites/sam/sa_home_idealized.png"
    zoom 0.75
    
image sa_home laughing:
    "sprites/sam/sa_home_laughing.png"
    zoom 0.75
    
image sa_home nervous:
    "sprites/sam/sa_home_nervous.png"
    zoom 0.75
    
image sa_home neutral:
    "sprites/sam/sa_home_neutral.png"
    zoom 0.75

image sa_home proud:
    "sprites/sam/sa_home_proud.png"
    zoom 0.75

image sa_home sad:
    "sprites/sam/sa_home_sad.png"
    zoom 0.75

image sa_home shocked:
    "sprites/sam/sa_home_shocked.png"
    zoom 0.75

image sa_street amused:
    "sprites/sam/sa_street_amused.png"
    zoom 0.75
    
image sa_street angry:
    "sprites/sam/sa_street_angry.png"
    zoom 0.75
    
image sa_street annoyed:
    "sprites/sam/sa_street_annoyed.png"
    zoom 0.75
    
image sa_street embarrassed:
    "sprites/sam/sa_street_embarrassed.png"
    zoom 0.75

image sa_street happy:
    "sprites/sam/sa_street_happy.png"
    zoom 0.75
image sa_street idealized:
    "sprites/sam/sa_street_idealized.png"
    zoom 0.75
    
image sa_street laughing:
    "sprites/sam/sa_street_laughing.png"
    zoom 0.75
    
image sa_street nervous:
    "sprites/sam/sa_street_nervous.png"
    zoom 0.75
    
image sa_street neutral:
    "sprites/sam/sa_street_neutral.png"
    zoom 0.75

image sa_street proud:
    "sprites/sam/sa_street_proud.png"
    zoom 0.75

image sa_street sad:
    "sprites/sam/sa_street_sad.png"
    zoom 0.75

image sa_street shocked:
    "sprites/sam/sa_street_shocked.png"
    zoom 0.75

image sa resigned:
    "sprites/sam/sa_resigned.png"
    zoom 0.75

# image sam silhouette:
#     "sprites/sam/sa_silhouette.png"
#     zoom 0.75


#Sonal
image son amused:
    "sprites/sonal/son_amused.png"
    zoom 0.75
    
image son angry:
    "sprites/sonal/son_angry.png"
    zoom 0.75
    
image son annoyed:
    "sprites/sonal/son_annoyed.png"
    zoom 0.75
    
image son embarrassed:
    "sprites/sonal/son_embarrassed.png"
    zoom 0.75

image son exasperated:
    "sprites/sonal/son_exasperated.png"
    zoom 0.75


image son happy:
    "sprites/sonal/son_happy.png"
    zoom 0.75

image son idealized:
    "sprites/sonal/son_idealized.png"
    zoom 0.75
    
image son laughing:
    "sprites/sonal/son_laughing.png"
    zoom 0.75
    
image son nervous:
    "sprites/sonal/son_nervous.png"
    zoom 0.75
    
image son neutral:
    "sprites/sonal/son_neutral.png"
    zoom 0.75

image son proud:
    "sprites/sonal/son_proud.png"
    zoom 0.75

image son shocked:
    "sprites/sonal/son_shocked.png"
    zoom 0.75

# image son silhouette:
#     "sprites/sonal/son_silhouette.png"
#     zoom 0.75

#Others
image ex:
    "sprites/ex/ex.png"
    zoom 0.75
image garlic:
    "sprites/cats/GarlicJohansson.png"
    zoom 0.75
image ginger:
    "sprites/cats/GingerSnap.png"
    zoom 0.75
image rap:
    "sprites/cats/Rapscallion.png"
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

    #sfx - bathroom

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

