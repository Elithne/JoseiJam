# The script of the game goes in this file.

# Characters
define narrator = Character(None, what_italic=True, callback = name_callback, cb_name = None)
define al = Character("Alex", color="#ffffff", callback = name_callback, cb_name = "alex")
define be = Character("Bernard", color="#ffffff", callback = name_callback, cb_name = "bernard")
define ex = Character(". . .", color="#ffffff")
define gar = Character("Garlic Johansonn", color="#ffffff", callback = name_callback, cb_name = "garlic")
define gin = Character("Ginger Snap", color="#ffffff", callback = name_callback, cb_name = "ginger")
define ma = Character("Marcos", color="#ffffff", callback = name_callback, cb_name = "marcos")
define rap = Character("Rapscallion", color="#c3acce", callback = name_callback, cb_name = "rapscallion")
define sa = Character("Sam", color="#ffffff", callback = name_callback, cb_name = "sam")
define son = Character("Sonal", color="#ffffff", callback = name_callback, cb_name = "sonal")
define stu = Character("Student", color="#ffffff", callback = name_callback, cb_name = None)
define jo = Character("Josephine", color="#c3acce", callback = name_callback, cb_name = None)

#Choices
default goodChoiceBernard = 0
default goodChoiceAlex = 0
default goodChoiceMarcos = 0
default goodChoiceSam = 0
default goodChoiceSonal = 0
default goodChoiceJosephine = 0 #General Ending that will have an impact with how she deals with her breakup.

#ExtraChoices
default changedPassword = False
default checkedSamPhone = False
default acceptBernardDrink = False
default weekOneGoOut = False
        
# The game starts here.
init:
    call define_sprites
    $ flash = Fade(0.5, 0, 0.5, color="#FFFFFF") 


label start:
    #Prologue 
    scene black
    show loginpage with dissolve
    pause(1.5)
    show emptysignuppage with dissolve
    $ playerName = renpy.input(_("My name is..."), default = "Josephine", length=12)
    $ playerName = playerName.strip()

    if playerName == "" or playerName == " ":
        $ playerName = "Josephine"
    $ jo = Character("[playerName]", color="#c3acce")

    play sound "audio/sfx/28-sfx_poetrytyping.ogg" volume 0.3
    show filledsignuppage
    show screen login with dissolve         
    pause(3)
    jump intro
    
label intro:
    hide screen login with dissolve 
    scene black with fade
    show mcprofile with dissolve 
    "Successful!"
    play music "audio/SAD - A Cool Electric Rainy Night by Mike Durek.mp3" fadein 0.5
    scene black with fade

    show ex_profile with dissolve
    "Love is a wonderful thing."
    show prebreakup_post with dissolve
    "You meet someone, you laugh at their jokes, you fall in love with them."
    "And when they're the one, you're just waiting to spend the rest of your life with them."

    scene bg_breakup with dissolve
    show ex at top with dissolve
    ex "Hey, I don't think this is working out.{w} Us, I mean."

    jo "..."
    scene black with fade
    hide all
    stop music fadeout 3.0

    centered "A month later"

    play sound "audio/sfx/01-sfx_bathroom.ogg" volume 0.3
    pause(1)
    scene bg_workbathroom with fade

    al "...Hello?"
    al "[playerName!q]?"

    show al silhouette at top with dissolve

    al "...[playerName!q]! Everything okay?"

    show al sad at top with dissolve

    jo "O-oh! Yes! Thank you, everything is fine."
    "How long was Alex speaking to me?? I didn't even realise anyone was here."

    play music "audio/GENERAL 1 - Decent Person by HoliznaCC0.mp3" fadein 3 volume 0.6

    show al  at top
    al "Want me to wait for you?"
    jo "No, I'm alright, thanks."
    al "You sure? I don't mind waiting. We can head over together."
    "Together? Where?"
    jo "Sorry, head over to…?"
    al "To the meeting…? {w}It starts in a few minutes."
    "Oof, get it together, [playerName!q]."
    jo "Right! Yes, of course, the meeting."
    "Alex gives me an inquisitive look that borders on concern."
    al "Yes…? So…we'll walk over together? Or…?"
    jo "Yeah, sorry, if you don't mind."
    al "I'll just wait outside then."
    jo "No!"

    show al shocked at top
    jo "I mean. {w}Sorry, we can just head over right now, actually. Thanks."

    show al sad at top
    al "..."

    al "...You sure you're okay?"

    menu:
        "Insist I'm doing well":
            jump alexIntro
        "Confess all my problems":
            jump alexIntro

label alexIntro:
    jo "I'm fine, thanks."
    "Or at least, I will be. {w}Probably."
    jo "Shall we?"
    "Alex hesitates to accept my answer at face value. I chant \"I'm fine\" on a loop in my mind and put on a smile to be extra convincing."
    al "..."


    show al happy at top

    al "...{w}So don't know if you've heard but the word from George in accounting is that Ivy from HR is in a relationship with someone in our department, which, mysteries aside has to be a nightmare for–"
    "Nice. Smooth. {w} Don't think she suspected anything was amiss."
    "Besides…"

    hide all
    scene bg_office_hallway1 with fade

    "Alex is friendly enough but I'd rather have her gossip about somebody else's problems. {w}I never know if what I tell her is going to end up as next week's office buzz."
    "As we walk to the conference room on the other side of the building, I find my mind drifting in and out of the conversation." 

    show al happy at top with dissolve
    al "--so then they said there's this other rumour–"
    "Alex's voice is pretty soothing…like one of those rain noises videos for sleep…" 

    hide all
    scene bg_office_hallway2 with dissolve
    show al shocked at top with dissolve

    al "--can't believe this was happening under all of our noses–"
    "...Who is she even talking about now? I've already lost the thread of this convo."
    al "--to think that they didn't think anyone would notice–"
    "Though, honestly, now that she's on a roll, I don't really need to engage beyond the occasional nod anyway so…."

    hide all
    scene bg_office_hallway3 with dissolve
    show al laughing at top with dissolve
    al "--not my cup of tea, if I'm honest, but then again–"

    "Oops, how long has it been since I made a noise to show I'm still listening?"
    jo "Hmm."
    "Did that sound interested enough?"

    show al embarrassed at top
    al "--so then I said– Oh, there's still some open seats."

    jo "Huh. Really."
    "I almost walk right into Alex, not realising that we've arrived at our destination. {w}Luckily, she hasn't noticed, intent on peering through the conference room door instead." 
    al "They're at the front, but we can sneak in. We're right on time– {w}ah, I mean only a little late. No one will even notice, probably."
    "I follow Alex inside, trying to refocus my thoughts as I enter."

    
    hide all
    play sound "audio/sfx/02-sfx_conferenceroom.ogg" volume 0.3
    scene bg_office_conferenceroom with fade
    
    show son at top with dissolve 
    son "...Let's see. {w}One, two, three, four, five and now, Alex and… [playerName!q]."
    play music "audio/SONAL 1 - Medicine by TimTaj.mp3" fadein 3
    show son annoyed at top
    son "Thank you for being on time."

    "So much for sneaking in."

    "I wilt a little under Sonal's intense gaze and quietly move to sit down. I don't want to give her more reasons to judge me."

    show son at top with dissolve
    "Alex has settled into the middle of three open seats, which means the only available spots to me are either at the head of the table, closest to Sonal, or on Alex's other side next to some person I've never seen before."

    "I weigh both options equally in the split second I have to make a decision."

    menu:
        "Sit in the first spot, in front of Sonal.":
            jump marcosIntro
        "Sit in the third spot, on the other side of Alex.":
            jump marcosIntro
    
label marcosIntro:

    "My hesitation doesn't go unnoticed and the knowledge of this fact amps up my social anxiety." 
    "Any considerations I was making go out the window and I just sit in the chair closest to me, which is not the one by Sonal."
    "...she's going to take it personally, isn't she."

    show son questionmark at top
    son "Are we missing someone? There's still an open chair here at the front…"
    "Sonal's eyes sweep around the room again as she does another mental headcount."

    stop music fadeout 0.5
    show son annoyed at top
    son "Oh."

    #music stops.
    hide son questionmark
    show son happy at top
    son "Let's go ahead and start, shall we? {w}First, I'd like to–"

    hide son happy with dissolve
    play sound "audio/sfx/03-sfx_marcosentrance_heels.ogg" volume 0.3

    "The click of heeled shoes walking at a brisk pace down the hallway somehow permeates the glass walls."

    play music "audio/SFX - Marcos Entrance Fanfare.mp3" fadein 3
    "The door swings open, the force of which sends papers flying."

    "As people scramble to grab their loose papers and pens, Marcos, the last attendee of this meeting, strides in with the full confidence of someone who's dad is a major stakeholder in the company."

    show ma smug maxcharm at top with fade 
    ma "Sorry, sorry, everyone!{w} You know what they say, can't rush perfection!"

    hide ma smug with dissolve
    show son laughing angermark at topleft with dissolve 
    son "...Marcos."
    show ma obnoxious at topright with dissolve
    ma "Sonal."
    stop music fadeout 3
    #music begins again

    "Marcos sits down in the empty chair next to Alex and immediately raises the height of the seat."

    play sound "audio/sfx/05-sfx_chairraise.ogg" volume 0.3

    "I know he's got long legs, but the unintentional (or intentional?) effect is that he's managed to be close to Sonal not only in seating arrangement, but also height."
    "Sonal seems to be pointedly ignoring this, like she always attempts to do whenever Marcos is involved."

    son "Thank you for joining us. Now, as I was–"
    ma "Of course, of course. I know how disappointed you would be if I didn't make an appearance."

    son "..."
    hide all with dissolve
    scene bg_office_conferenceroom
    hide ma obnoxious with dissolve   
    show son at top with dissolve
    son "As I was saying."

    "Sonal pulls up the first slide in her presentation."
    
    son "First, I'd like to clarify that the project we are discussing was originally–"
    "... Originally Marcos' responsibility, right?"
    "Sure enough, Marcos' name is listed on the title slide, albeit underneath Sonal's name."
    "Didn't he make a big deal out of being assigned this case? Not that it's surprising that Sonal had to pick up the slack."

    hide son with dissolve
    show son at topright with dissolve
    show ma smug at topleft with dissolve
    ma "Question– how long is this meeting going to be?"

    "Sonal pauses as if she wasn't just interrupted."
    show son annoyed at topright with dissolve
    son "Good question, Marcos."

    son "I sent an email out in advance with the agenda. Maybe you didn't receive it. I'm sure it's my fault."
    show ma obnoxious at topleft with dissolve
    ma "Oh, right, I did see a notification in my inbox."

    "There's a silence as we all take in the implication that he obviously didn't read said email."
    show son angry at topright with dissolve
    son "...Great. Glad to hear it."

    ma "Still, is there an estimate?"

    son "Well, luckily I had the foresight to print copies of the agenda which you'll see before you. It's also here on this next slide which I was about to get to."
    ma "Only asking because I have to make a meeting with some investors so…"
    son "You're very welcome to leave early if you need to."
    ma "No, no, I don't want to steal your thunder."
    ma "Besides, it would be so boring without me."
    ma "Gotta give the people something to live for."
    ma "But if you want to wrap this up early, by all means…"
    son "...I'll do my best."
    son "If there are no further questions–"
    "Sonal gives everyone a look warning us not to add unnecessarily to the meeting length."
    
    show son at topright with dissolve
    son "--onto the first order of business, shall we?"
    "I can hear the smile in Marcos' voice as he pipes up almost immediately."
    show ma laughing at topleft with dissolve
    ma "Question–"

    scene bg_office_conferenceroom with fade

    show son at top with dissolve
    son "I'll send the rest of the briefing in an email, since we're running short on time. Feel free to email me any questions or concerns otherwise."

    play sound "audio/sfx/06-sfx_endofmeeting.ogg" volume 0.3

    hide son with dissolve

    "I stretch my arms out before collecting my papers. It felt like a much longer meeting than it actually was."

    show ma  at top with dissolve
    ma "Just gonna make a call, don't mind me."

    "Marcos stands, looming over all of us. I always forget how tall he is on top of all the space he takes up naturally by being a nuisance."
    hide ma  with dissolve
    show ma  at topright with dissolve
    show son  at top with dissolve
    son "Alex, do you mind popping by my desk before you head to lunch for a quick chat about the Turner case?"

    show al  at topleft with dissolve
    al "Oh, of course–"

    show ma laughing at topright with dissolve
    ma "Heya James, might be a few minutes late to tennis–"
    ma "No I didn't want to be rude, you know how it is."

    show son angry at top with dissolve
    son "..."

    "Alex, eager to diffuse the tension, moves around Marcos to join Sonal at the head of the table."
    show al sad at topleft with dissolve
    al "...th-the Turner case. Sorry, you were saying?"

    show ma smug at topright with dissolve
    ma "Yeah, I'll grab something for their assistant too. We can just write it off."

    show son exasperated sigh at top with dissolve 
    "Sonal takes a deep breath."
    
    son "...Yes, sorry, Alex. {w} I was just asking if you had–"

    "Maybe it's time to leave."
    
    scene bg_office_conferenceroom with dissolve
    "Just as I'm getting up, Marcos grabs his coat off the back of his chair. As he heads towards the door, we make sudden intense eye contact, causing Marcos to stop in his tracks."

    show ma shocked at top with dissolve
    ma "My god, [playerName!q], you scared me!"

    jo "Sorry–"

    ma "No, just a coworker."
    show ma annoyed at top with dissolve

    "Marcos pauses, never breaking eye contact."
    "Why is he staring so intently? I-is there something on my face?"     
    ma "Ah, not mascara."

    show ma  at top with dissolve
    ma "...get some rest, love."
    "As he moves past me, he continues his conversation on the phone."

    show ma smug at top with dissolve
    ma "No, she just looks haggard– like a panda with those eye bags–"
        
    menu:
        "Laugh it off":
            jump prologuePhone
        "Curse him out":
            jump prologuePhone

label prologuePhone:        
    jo "..."
    hide ma smug with dissolve
    "Marcos leaves the room, but I swear I can hear the echoes of what he said bouncing around the near empty conference room."
    jo "So, I'll just be at my desk then."

    show son embarrassed at topright with dissolve
    show al at topleft with dissolve

    "Sonal acts like she didn't hear me while Alex gives me a supportive smile that just makes her look pained."

    scene bg_office_desks with fade

    "Unfortunately, I can't just leave work out of shame as much as I would like to curl up in a pit and never be seen again."
    "I mean he probably wasn't wrong. I do look a mess."
    "At least, I feel like a mess."
    "..."
    "And whose fault is that?"

    #flash to image of couples photo on black (lmk if we need just the photo alone)

    scene black with flash
    show expost1_beach with dissolve
    "..."

    "Ugh, I don't even want to think about Them."
    "Whatever, it makes me human to be going through it, right?"
    "That's normal. And appropriate."
    "Not rebounding so fast that you start to wonder if He ever even–"
    "..."
    "Bet she'd never be caught looking so… haggard."
    "..."
    "Just a peek."

    #real phone screen
    #edited couples photo longer
    scene bg_office_desks with flash
    "Nope. Nope. Why? Why did I do that?"

    show al at top with dissolve
    al "Ready for lunch? I'm famished."

    "I drop my phone in shock."

    play sound "audio/sfx/07-sfx_phonedropclatter.ogg"  volume 0.3

    jo "Hello! Yes!"
    "I'm so glad my phone fell on the desk face down."
    jo "H-how was the talk with Sonal?"
    al "Pretty normal."
    jo "Right. Lunch. Let me just–"
    "Let me just make a big show of double checking my work related tabs."
    "I slowly close an empty excel sheet."
    
    play sound "audio/sfx/08-sfx_closingclick.ogg" volume 0.3 

    jo "...Good to go."
    al "You know, I think it's okay for a bit of pre-lunch phone time."
    jo "...haha, what do you mean?"
    al "Were you playing a game? I've been looking for a more challenging one to pass the time. You looked pretty frustrated so I just wanted to ask if you had a recommendation."

    menu:
        "Be honest with Alex.":
            jump prologueLunch
        "Lie through my teeth.":
            jump prologueLunch

label prologueLunch:
    jo "J-just saw something um… distressing on the uh… news."
    al "Oh, right, the news is always so depressing, yeah?"
    jo "Yeah, like I wish I had a game to recommend to you instead, honestly."

    show al laughing at top 
    al "If I find something good, I'll let you know!"

    show al at top 
    al "Although speaking of games and depressing news–"
    "Alex starts up a new source of office gossip, something about a senior executive…someone being bullied…mind games…"
    "I relax again, tuning in and out as we begin to walk."
    
    scene bg_office_lunchspot with fade

    show al at top with dissolve
    al "What about you?"

    "I realise Alex is looking at me expectantly."
    jo "Uh… I–"
    "I am completely lost as to what Alex is asking me."

    show al exclamation at top 
    "Luckily, Alex spots something of interest and completely pivots her attention away."

    #sfx music? Sonal 1?
    hide al exlamation
    show al happy at top
    al "Oh, Sonal!"

    "Sonal looks up from her phone, mid bite of food."

    "Alex walks over faster than I expected her to."
    show al happy at topleft with dissolve
    al "You're not eating at your desk today?"

    show son at topright with dissolve
    son "...No. I thought I would take a proper break."
    al "You certainly deserve it."
    "I feel like we're intruding on Sonal's truly rare break time. In fact, I have half a mind to walk away now and leave her be."
    "Alex is faster than me though, and twice as invested in socialising."
    al "Mind if we join you then?"

    show son annoyed at topright
    son "..."

    hide son annoyed
    show son at topright
    son "No, not at all."

    scene bg_office_lunchspot with dissolve
    "Sonal gestures at the empty seats at the table."
    "Alex begins to unpack her homemade lunch."

    show al laughing tinyflowers at topleft with dissolve
    show son at topright with dissolve
    al "I see you have a lovely little salad! Certainly feels like a salad day, doesn't it [playerName!q]?"

    "Neither Alex nor I are having salad for lunch. I nod anyway as I procure a sad, soggy sandwich."
    hide al
    show al exclamation at topleft
    al "Oh sorry Sonal, you're vegan right? I suppose you didn't have too many choices around here."
    hide al
    show al at topleft
    
    son "Vegetarian. Only for the last few years though.{w} Though, there were a few other options–I just thought a salad was faster."
    jo "I actually had no idea."
    jo "That you were vegetarian. {w}Not about the speed of grabbing a salad. {w}Though I understand of course. {w}You certainly don't have to heat it up and all."
    "Sonal nods, not quite sure how to follow up that blurb of information."
    al "Well, you're technically newer to the company than Sonal, right [playerName!q]? {w}You haven't had a chance to get to know each other for very long."
    son "We hired in at the same time, I think."
    al "Oh forgive me, you just seem like a more seasoned worker, Sonal."

    show son laughing at topright
    son "Thanks. I'm trying my best to keep up."
    "I mean, I do try too. Not all of us can be a Sonal."
    jo "...So you just personally decided to be vegetarian one day?"

    show son annoyed at topright
    son "Er…yes. That's how it works for a lot of people, I thought."
    "Why do I feel like I've offended her somehow?"
    al "Mm, did you know Marcos is a vegan too?"

    show son annoyed disgust at topright
    son "I'm not– "
    "Sonal pauses and then seems to let whatever she wanted to say go."
    son "No, I wasn't aware. I don't usually have the chance to ask him about his diet."
    jo "With how often you're put on projects with him, I would've thought that the topic had arisen by now."

    hide son annoyed disgust at topright
    show son angry at topright
    son "Unfortunately, Marcos rarely stays around long enough to have a meal with me."

    "What, has Sonal tried to ask Marcos to dinner?"
    "I mean, Marcos is fanciable if we're talking visuals alone. {w}And he comes from money. He has connections. And his hair is always so soft-looking– I could see where she's coming from."
    "And like Alex said, Sonal is so good at her job. Plus her hair is just as nice as his and she always looks so pretty. They'd make a perfect couple. "
    "God, I must seem even more of a mess next to her."
    al "H-have you asked him to?"

    show son shocked at topright
    show al shocked at topleft
    son "What."

    show son exasperated at topright
    son "I mean, sorry, no, I– it never occurred to me."
    son "I get things done faster without him there anyway, you see."
    show son at topright
    hide al

    show al at topleft
    son "I'm sure he wouldn't enjoy my power… dinners."
    "Oh wow. Is this how Alex feels when she sniffs out a new workplace romance?"
    "I glance at Alex but I can't read her expression for once."

    menu:
        "Try to subtly find out if Sonal likes Marcos.": 
            jump prologueLunchContinue
        "Ask Sonal outright if she likes Marcos.":
            jump prologueLunchContinue

label prologueLunchContinue:
    jo "I'm sure you want him to."

    show son annoyed questionmark at topright
    show al angry flyingsweat at topleft
    jo "I mean, I'm sure he'd love you."
    jo "Dinner with you."
    jo "I think you would um, have a good time together."
    "Oh god, why did I open my mouth?"
    "For that matter, why does talking to Sonal intimidate me so much?"
    
    show al laughing sweat at topleft
    al "Yes, I'm sure any of us would love to have dinner with you, that's what you meant, right [playerName!q]?"
    "Yes. No. I don't know."
    "I nod anyway."

    show son fork at topright
    son "...I would rather not have to stay behind to tie up loose ends at all."

    show al shocked at topleft
    "Sonal punctuates her point by stabbing the last bit of her salad with her fork."

    son "But thank you."
    son "I think I'll head back early."

    play sound "audio/sfx/08-sfx_closingclick.ogg"  volume 0.3

    "She stands, efficiently grabbing all her trash and belongings, before pushing her chair in with her leg."

    hide al
    show al happy at topleft
    al "Okay, see ya!"

    son "Enjoy the rest of your lunch."

    hide son with dissolve
    hide son with dissolve

    "Once Sonal leaves the space entirely, I turn to Alex."
    hide al with dissolve
    show al at top with dissolve

    jo "...Alex, hear me out okay?"
    al "Of course, love."
    jo "Do you ever get the sense that Sonal hates me?"
    al "Oh you mean from just now? I think that was just a slip of the tongue, I'm sure she understands–"
    jo "I guess I just get the sense that she's not happy to be around me. Is it just me?"
    al "I haven't experienced that, if I'm being honest."
    jo "It's probably just me then."

    show al happy tinyflowers at top
    al "Don't get in your head too much! Take it from someone who's been here a bit longer than you–we have a good set of coworkers here."
    al "Trust me when I say it could have been much worse."
    jo "Right."
    al "It'll only get better with time!"
    "While I'm not convinced yet by Alex's placating statements, I don't see why Sonal would have reason to hate me."
    "It's not like I'm a terrible person." 
    "After all, I don't make trouble for Sonal on a regular basis like some people."
    "At least… I don't think I do?"

    scene bg_office_desks with fade
    #sfx of typing
    #cue marcos music

    ma "Still hard at work, sweetheart?"
    show ma at top with dissolve
    "I look up to see Marcos standing at my side."

    "...He's really quite tall. Like model level proportions."

    jo "Just finishing up here."

    ma "I see. Any plans for the evening?"

    jo "..."

    "Why am I flustered by such a normal question?"

    jo "...For the evening?"

    "Don't panic, [playerName!q], he's likely just finding people for an after work pub visit… Although I didn't realise we had interacted enough for him to want to hang out like that."

    jo "N-nothing special, I think. {w} Go down to the local, probably, but–"

    ma "Great, great, see, I have a bit of work left to do–"

    jo "Oh no!"

    show ma sad at top
    ma "Yes, it's a shame because I'm busy this evening. {w}The remainder probably won't take too long but I would hate to cut into my plans."

    "I almost feel a sense of relief that he's not asking me out, platonically or romantically. Instinctively, I know that Marcos is trouble."

    jo "That is a shame. I wish there was something that could be done."

    "...What would that even look like? A relationship with Marcos? {w}Even in my anger at my ex, I feel like that's a step in the wrong direction… But maybe the right message to send?"

    ma "Isn't it? You're the only one who understands. {w}If it's not too much, you wouldn't mind finishing everything up for me, right? {w}Since you don't have anything special planned."

    jo "Um…"

    "Wait, how did we get to this point? Did I accidentally agree to something? I don't think I did but…"

    show ma happy sparkle at top
    ma "I understand if you're busy after all. {w}Only, you'd be helping me out of a major bind and I won't forget it…"

    "I didn't plan on staying behind either, if I could help it!"

    ma "I don't want to pressure you so, think on it if you need the extra time. {w}I know you're a really nice person and I don't want to take advantage of your niceness."

    "Well… I mean, it's good to help people out right? And… he's basically saying he'll owe me one right?"

    menu: 
        "Tell Marcos I can't do it.":
            jump prologueSonvsMar
        "Agree to take on the work.":
            jump prologueSonvsMar

label prologueSonvsMar:
    jo "Actually…"

    "Sonal walks by and actively turns back around to stop and talk to the both of us."

    hide ma with dissolve
    show ma at topright with dissolve
    show son at topleft with dissolve

    son "Hey, before either of you leave for the evening, make sure to change your passwords. IT sent out an email but I was specifically instructed to remind everyone verbally."

    ma "Sonal! Great timing– just who I wanted to see."

    "Sonal hesitates, though her body is still turned away as if she's poised to leave as soon as possible."

    show son annoyed disgust 
    #son shocked/disgusted face but mild

    son "...Did you already change your password? Great. I applaud your industriousness, Marcos."

    ma "Ah, still on my to-do list, I'm afraid. I have a bit of a conundrum that I was wondering if you could help me with Sonal."

    show son nervous at topleft with dissolve

    "Sonal glances at me."

    "Is she asking for help?"

    son "...Did [playerName!q] turn you down already?"

    "Or is she trying to figure out if I'm a threat to her interest in Marcos?"

    "Maybe she wants to have Marcos in her debt?"

    show ma smug at topright with dissolve

    ma "Oh, glad we're already on the same page!"

    ma "You know, [playerName!q] is such a sweetheart."

    ma "But I'm always in need of someone with a sharp and critical eye to look over everything. So I thought, you know who would be perfect for this? Sonal!"

    son "...I'm flattered."

    ma "So you'll do it then?"

    son "I'm afraid I have a few other tasks to complete already."

    ma "Aw, what a shame. Isn't that such a shame [playerName!q]?"

    menu: 
        "Agree with Marcos":
            jump prologueAgreeMarcos
        "Backup Sonal":
            jump prologueAgreeSonal


label prologueAgreeMarcos:
    jo "Yes, that's too bad." 
    ma "Well, what can we do? It can't be helped if Sonal is lacking."
    ma "We wouldn't want to push her past her limits." 

    show son annoyed at topleft with dissolve

    son "..."
    son "Apologies." 
    son "If you don't need anything else from me, I have to go work on my other, very taxing tasks now."
    ma "Remember to take breaks, Sonal!"

    hide all with dissolve

    show ma at top with fade

    ma "Well, sweetheart, I wanted to spare you but you're my only hope."
    jo "O-oh, right."
    ma "Oh good, I didn't want to have to get on my knees and beg."

    jump bernardIntro

label prologueAgreeSonal:

    jo "I think Sonal deserves a day off."

    show ma shocked at topright with dissolve

    pause 2.0

    show ma obnoxious at topright with dissolve

    ma "You're probably right. Sonal's looking a little tired."
    ma "We don't want to push her past her limits. Make sure to take breaks, Sonal!"

    show son annoyed at topleft with dissolve

    son "..."
    son "I'll be sure to head home as soon as possible to get more rest. Thank you for your concern."

    hide son with dissolve
    hide ma with dissolve

    show ma at top with fade

    ma "Always classy, that one."
    ma "So good to see an office friendship blossoming too."
    jo "Between…?"
    ma "You and Sonal! Look at you, taking on extra work for her."

    jump bernardIntro

label bernardIntro:

    "What–?"

    ma "It's really not too much. You're a great worker, you'll have it done in no time."
    ma "I'll send over the files in a second, alright?"
    ma "Thanks, love."

    jo "W-wait–!" 

    hide ma with dissolve

    "Aaaaaand he's gone."

    "...This won't take too long, will it?"

    "Flashbacks of other days spent working overtime cross my vision."

    jo "..."
    jo "I'll just get it done as soon as possible."
    jo "He said it's really not that much!"
    "Right? Right???"

    scene black with fade

    centered "One hour later…" 

    jo "I need to get a drink."

    scene bg_transition_subwaysign with fade
    scene bg_transition_subwaytrain with fade
    #sfx subway noise

    scene bg_bar with fade
    #sfx bar crowd

    be "Hey. Good to see you. The usual?"

    jo "Actually, something stronger today, if you could, Bernard."

    be "Long day?"

    jo "That's everyday, isn't it?"

    be "Longer day than usual?"

    jo "For now. Bet it won't be long before \"usual\" is just a distant memory and this becomes the standard."

    be "Mhmm."

    "Bernard grabs a bottle off the shelf and pours a glass of amber liquid for me."

    #sfx pour drink

    jo "Had to finish up someone else's work today."

    be "That Marcos guy?"

    jo "Wow, was it that obvious?"

    be "Seems to be a recurring antagonist."

    jo "Yeah well, I don't know why I fall for it every time."

    "I think about Sonal's reaction to his request."


    "She was so good at getting out of it. I'm such a pushover."
    show be at top with dissolve

    "I take a sip of my drink, letting the burn in my throat mingle with the bitterness of my emotions."

    be "How many times has he done this already?"

    jo "...well,  I guess, if I really think about it, this is only the second time."

    jo "Fool me twice and all, I guess. Next time though. I'll say no."

    "I punctuate that thought with a longer sip."

    jo "I mean he's not terrible. He's not like a serial killer for example."

    jo "And his work is well done and easy to pick up and I don't know… maybe he has normal expectations for how long things will take and I'm just slow."

    jo "So I guess… I guess it's not exactly a crime for him to ask me for help but…."

    jo "Although, he was being a right arse during the meeting this morning."

    jo "But I guess that's what they call confidence."

    jo "I suppose I should respect that."

    "Bernard raises his eyebrows but doesn't say anything."

    "*One drink later*"

    jo "And I don't want Sonal to hate me! I think I'm a good person– I'm a good person right, Bernard?"

    "I squint at the blurry bottles on the wall and take a few seconds to realise Bernard isn't even in front of me. He's filling a pint for another person at the bar."

    "I have enough presence of mind to stage whisper at Bernard instead of yelling my head off."

    jo "Bernard. Bernaaaard, listen."

    "Bernard makes his way back at his own pace."

    be "I'm listening."

    jo "...What was I saying?"

    jo "Oh right, Sonal has everything together and it's not like I'm causing her problems, y'know? Even when I try to show that I'm on her side though…she seems to think I'm not? God, I don't want her to hate me."

    be "I'm sure she doesn't…or that there's an explanation if she does."

    jo "Yeah well–"

    jo "Issa vibe. A feeling. You wouldn't get it."

    jo "Nobody gets it."

    jo "Can I get another drink?"

    #transition

    "*Several drinks later.*"

    #bernard looks a little tired

    jo "...And this morning! My ex posted another picture with that– that– the one– the one with the hair–  from the other photo! Like why do I need to see their slow progression into a–"
    
    scene black with fade
    "*One drink later*"
    scene bg_bar with fade
    hide be with dissolve

    jo "It hasn't even been that long! I can't b'lieve they'd do this to me! To me! Did I do something to deserve this?"

    jo "I just don't– I don't understaaaaaand. What do they have that I don't?!"

    be "I couldn't say…"

    jo "Can't say what?"

    be "...I think you've had enough, [playerName!q]."

    jo "Oh gosh, what time is it?"

    "Bernard glances at the register."

    be "Twenty five to eleven."

    jo "......"

    jo "I have work in the morning!"

    be "Yes."

    jo "Thanks Bern'd."

    be "My pleasure. Be safe."

    scene bg_bar with fade
    hide be with dissolve
    show be sad at top with dissolve

    "I'm a big girl. I can make it home."

    "Be safe…" 

    "M-maybe I shouldn't risk it."

    #choice

    #call alex

    "I do have Alex's number…Somewhere in the… Somewhere–"

    #sfx: dial tone

    sa "Hello?"

    jo "Alex!"

    sa "No, did you mean to call Alex?"

    jo "Uh…no."

    jo "Maybe. You're not Alex though."

    sa "No."

    jo "S'course, I knew that. You're Sam."

    sa "Yes."

    scene bg_street_bar with fade
    #sfx door close
    #sfx street

    #end choice 1

    #call sam

    "Sam! Sam."

    #sfx: dial tone

    sa "Hello?"

    jo "Sam!"

    sa "Yes, hi. Is something up?"

    jo "No, why?"

    sa "You sound a bit too excited to speak to me."

    jo "Do I?"

    jo "You're just such a great– a great–"

    sa "Are you drunk?"

    jo "No."

    jo "Okay, maybe. Not plastered just you know… had a cheeky drink or three and now the street is a little worgly. Wuggy. Wiggly."

    #end choice 2

    sa "Right."

    jo "And since I've got you on the phone…"

    sa "*sigh* Mhmm."

    jo "Could you come pick me up, pretty pleaaasseee?"

    sa "Where are you right now?"

    jo "Outside the Better Days Bar… come quickly or I'll abscond with the next nice person I seeeeee." 

    sa "*sigh* I'll be right there."

    jo "Hurry, I'm this close to rebounding with a stranger."

    sa "Go sit inside till I'm there."

    jo "Alright, Mr. Bossy."

    sa "I'm hanging up. Remember, sit inside, please."

    #sfx call ending

    "I mean I could sit inside."

    "Bar won't close for another… soon."

    "I'm too tired to go back in though." 

    "I'll just… sit myself down here on the sidewalk. People can go around me if they're so bothered."

    "..."

    "...Where is Sam anyway?"

    "..."

    "How long has it been since I called him?"

    "Feels like it's been a while."

    "Should I call him again?"

    "What if he's not coming?"

    #sfx dial numbers sound
    #sfx dial tone

    #sfx phone ringtone

    #sfx phone call ended

    sa "What did I say about sitting outside?"

    sa "Bernard would've been better company than the ground."

    jo "Did you just hang up on me without picking up?!"

    jo "Everyone's always hanging up on me. Leaving me behind."

    sa "I was literally a few feet away. I could already see you."

    jo "Well you took your time!"

    sa "I was actually going as fast as I could without triggering feelings of annoyance."

    #shaky text?
    jo "I am annoying, aren't I? You probably want to replace me too."

    jo "If you wait at least a month, you won't– you won't even be the worst–"

    jo "We were together for *hic* so many years and I'm just tossed aside like rubbish at the sight of the next pretty face?!"

    jo "I'm pretty enough right?! Why didn't he and I ever go on trips to the sea? Post cringe photos on Tangram?"

    jo "We should take a selfie right now! Show that jerk what he's missing out on."

    sa "..."

    sa "No, thanks."

    jo "Yeah, thought you'd say that."

    sa "..."

    jo "*sniff*"

    sa "Done throwing a wobbly?"

    jo "You're throwing a wobbly."

    sa "Alright. Up you get."

    sa "You have all your stuff? Phone, wallet, keys? Purse?"

    jo "Yes, mum."

    sa "You're okay to walk?"

    jo "*sniff* Yes."

    sa "You can lean on me if you need to."

    jo "*sniff* 'Kay."

    #bg_carinterior
    #sfx car stuff
    #sfx car doors
    #sfx car starting
    #sfx driving noise

    #basically they're on the way home

    sa "You know, you're lucky I was awake."

    jo "You don't even sleep at night."

    jo "Besides it doesn't take that long to get here."

    sa "Sure. Just so we're clear, I'm always happy to make sure you're safe, but like I did last time, I am gently reminding you that taxis exist."

    jo "*sniff* Isn't it nice to hang out?"

    sa "There are better ways to hang out. This is not one of them."

    #bg starts fading in and out until black.

    #sfx ignition off

    #bg black

    sa "[playerName!q]? [playerName!q], wake up. We're here."

    #sfx car doors + lock

    #bg black
    #sfx key noises

    #sfx walking up stairs

    #fade to bg_aptstairs, #bg fade to black

    #bg_apthall

    sa "Where are your keys?"

    jo "Purse."

    #sfx digging through purse

    sa "Why do you have so many napkins– nevermind, found them."

    jo "Mmm."

    sa "Hey, stay with me, you're almost there."

    jo "Sleepy."

    #sfx door unlocking

    #bg_joflat_entrance

    sa "Shoes."

    "I attempt to kick my shoes off."

    jo "Ah! Cramp, cramp in my leg, ow ow ow ow."

    "Sam sighs loudly."

    sa "Sit down and hold still."

    "Sam firmly removes my shoes for me."

    sa "I'm going to leave your purse on the table. Do you want your phone?"

    jo "Mmm."

    sa "Is that a yes?"

    jo "Yeah."

    sa "How's your leg?"

    jo "Still feels tense but… *yawn* false alarm, I guess."

    sa "You feeling alright otherwise?"

    jo "Sleepyyyy."

    sa "[playerName!q]."

    jo "Yeah, I'm fine just– *yawn*"

    sa "Okay."

    sa "I can stay if– Well, no I don't think I should. But if you need me, call me or knock on my door, okay?"

    jo "'kay."

    #sam leaves

    #sfx door closing in the distance

    #mc enters dark bedroom

    #sfx flopping into bed

    "..."

    "Of course, as soon as I'm in bed, I'm wide awake."

    "I should change out of these clothes."

    "Ah but my bed is so soft and…"

    "...What if I– One little peek…?"

    "No. I shouldn't."

    "I find myself opening the Tangram app anyway."

    jo "Not going to do anything silly."

    jo "..."

    jo "It's my alt account anyway."

    #sfx typing poetry

    #Insta post:
    scene black with fade
    show cringepoetry1 with dissolve

    "You could have been"
    "My everything"

    "I would have been"
    "Your forever"

    "Now you are another"
    "Learning experience"
    jump introWeekOne
        
#Week 1
label introWeekOne:
    scene bg_flat_mc_bed with fade

    jo "Ugh my mouth is so dry…"

    scene black with fade
    centered "One week later..."

    scene bg_flat_mc_bed_morning with fade
    jo "What time is it even?"
    jo "5:30 AM?"
    "Did I wake up from dehydration? I feel like a husk of a being."
    "There's a strange, dull ache in my legs too."
    jo "...What did I do last night?"

    scene black with fade
    centered "Last night..."
    scene bg_flashback_mall with fade

    jo "I deserve to treat myself. {w}I deserve to look amazing."
    jo "This is a definite yes. {w}Oh and this too!"

    play sound "audio/sfx/29-sfx_chaching.ogg"  volume 0.3

    jo "Ah I feel so much better! So much lighter!"

    scene bg_flat_mc_bed_morning with fade
    play music "audio/GENERAL 2 - Day Trips by HoliznaCC0.mp3" fadein 3 volume 0.6

    jo "Oh god."
    jo "My poor bank account."
    jo "How many clothes did I buy?"
    "The light from my window illuminates a few bulky shapes, but I'm afraid to look too closely."
    "As I get out of bed, I trip over at least three bags."
    jo "..."
    jo "Tea first and then we can face my sins."

    scene bg_flat_mc with fade
    play sound "audio/sfx/30-sfx_makingtea.ogg" volume 0.3

    "What was it that even triggered all of this?"
    "Something is bothering me but I can't quite remember what it is, like my brain is trying to protect itself from a source of danger."
    jo "I suppose I can figure it out later. {w}Let's look through these bags first."

    play sound "audio/sfx/31-sfx_rustlebags.ogg" volume 0.3 

    jo "Well, these aren't terrible outfits at least–but oof, that is expensive. As is this. And that." 
    "My poor, poor wallet. I can't even imagine how much worse it would be if I had done some online retail therapy instead."
    jo "I'll see if I can return some things. {w}I should still have all my receipts here. Somewhere."
    "But I can't deny, it would be nice to wear something new today. {w}Maybe if I look better than I feel, I can get through the day just fine."
    "I rifle through the bags until I find something that works for the office."
    jo "These heels are pushing the boundaries of business appropriate but… {w}They're so cute… And just the right shade of green…"
    "I'm sure no one will call me on it."
    "Hmm, but fashion aside, is it a physically bad idea to wear brand new heels to work?"

    stop music fadeout 5
    menu: 
        "Yes, this is a terrible idea.":
            jump firstSonalDecision
        "No, I'm an adult who makes adult decisions.":
            jump firstSonalDecision

label firstSonalDecision:
    "...I'm sure it'll be fine this time."
    "After all, I'd have to break them in anyway. Might as well be today."
    scene bg_transition_subwaytrain with fade
    play sound "audio/sfx/11-sfx_subwaytransition.ogg" volume 0.3

    "Since I woke up so early, I'm able to head to work at a leisurely pace."
    "Which is good, because the heels pinch a bit, but at least they look great!"
    scene bg_transition_subwaysign with fade
    pause(2.0)   

    scene black with fade
    stop music fadeout 2
    play sound "audio/sfx/32-sfx_elevatording.ogg" volume 0.3
    pause(3.0)

    scene bg_office_elevator with fade
    show al at top with dissolve
    play music "audio/GENERAL 1 - Decent Person by HoliznaCC0.mp3" fadein 3 volume 0.6
    al "Morning [playerName!q]!"
    jo "Morning!"
    al "You're here earlier than usual."
    jo "Oh, only by a little."
    show al questionmark at top
    al "You seem different today–is that a new outfit?"
    jo "I might have gone shopping over the weekend."

    hide al
    show al happy at top
    al "Oh what's the occasion? You look very fresh."
    jo "...No occasion, just wanted to try something new."
    al "Oh, yes, I suppose sometimes a change is nice!"
    al "Though, I wouldn't have been surprised if you had a reason to dress up today. {w}It's very different from your usual look!"
    jo "Um, thanks."

    "Why do I feel so annoyed by this conversation?"
    "I glance at Alex who is pointedly not looking at me, like she's waiting for me to fess up about who it is I'm looking to impress."

    play sound "audio/sfx/33-sfx_elevatorarrival.ogg"  volume 0.3

    jo "Well here we are."
    al "See you around!"

    hide al with dissolve
    
    scene bg_office_desks with fade
    jo "Let's see, what's on the old agenda today?"

    show son exclamation at top with dissolve
    play music "audio/SONAL 1 - Medicine by TimTaj.mp3" fadein 3 volume 0.6
    son "Oh [playerName!q], hello."

    hide son exclamation
    show son at top

    "Sonal's stopped at my desk, a look of mild surprise on her face.{w} It's quickly replaced by her standard expression of professional politeness."
    "I guess clothes are on my mind, because I mentally note how Sonal looks like she has her life together even without a brand new outfit. I aspire to reach her level of effortless but striking fashion."
    "We start speaking at the same time."

    son "Did you get around to changing your password?"
    jo "You look nice today, Sonal."

    show son annoyed questionmark at top
    son "....huh?"
        
    hide son annoyed questionmark
    show son annoyed at top
    jo "M-my password?"

    son "Was that– I mean, not sure if you remember from last week, but IT sent an email telling everyone to change their work passwords. {w}Your name is on the list of people who I've been told to specifically speak to in person. {w}Again, I mean."
    
    "That's actually very embarrassing."
    
    jo "Sorry, I'll get to it today."
    son "As soon as possible, please."
    hide son with dissolve
    "Sonal leaves without addressing my orphaned compliment."
    "I'm not sure if I'm relieved or horrified."

    stop music fadeout 1

    menu: 
        "Change password now.":
            $ goodChoiceSonal+= 1
            $ changedPassword = True

            "As for my password… I'm definitely going to forget to change it later."
            "And I don't want to have Sonal coming around again on the very high chance that I'll say something even more embarrassing out loud."      
            jo "Let's get that fixed up right now. Where is the link to the account settings…ah here…"
            
            play sound "audio/sfx/34-sfx_changepassword.ogg" volume 0.3
            
            "Fueled by the social pressure, I get the task done in no time."
            "Not going to lie, I feel slightly closer to the efficiency of Sonal's work ethic just by completing this one little thing."
        "Change password later.":
            $ goodChoiceMarcos+=1
            $ goodChoiceAlex+=1
            $ changedPassword = False
            "About my password… well it's not exactly watertight but it's not getting hacked in one morning if it hasn't failed already."
            "I'll get to it after the rest of my work is done."
            "I put the IT department's emails in the back of my mind, filed away for a better time."

    "The morning work is pretty standard and before long, I reach a good place to take a break."
    jo "Let's get up and stretch our legs…"
    "Time for a cuppa, I think."
    "I head to the office kitchen."

    scene bg_office_kitchen with dissolve
    show son at top with dissolve

    play music "audio/SONAL 3 - Thoughtful by TimTaj.mp3" fadein 3 volume 0.6

    "Surprisingly, or perhaps not surprisingly, Sonal is in the kitchen, already boiling water in the kettle."
    
    son "Oh, [playerName!q], I was just about to come ask if anyone else wanted a cup."
    jo "Well, I saved you a trip!"
    son "I guess, you did. Though, I'll still have to ask the others–"
    jo "Oh, right."
    "Sonal doesn't make a move to leave just yet though."

    if changedPassword:
        jo "...Before I forget, I just wanted to let you know I changed my password."
        show son happy sparkle at top
        son "That's great! Thanks for getting to that so fast."
        jo "One less thing to worry about."
        son "Yes, exactly."
        
        show son embarrassed blush at top
        son "Also, um, I didn't do anything special but– thanks for the compliment. {w}Earlier, I mean."
        son "And you look nice too."
        "I'm genuinely pleased to hear that from Sonal. {w}Perhaps we could get along better if all of our interactions were like this?"
        jo "Thanks."
        son "..."
        jo "..."
        "Maybe that was too much wishful thinking."
        jump firstMarcosDecision

    else:     
        "A hush falls over the kitchen."
        "I realise I have nothing to say to Sonal."
        "I mean does she care to hear about what I did over the weekend? We don't really talk about things like that."
        "In fact, since we both got hired, most of our conversations have been strictly about work."
        "And speaking of work, I can't very well tell her I didn't change my password yet, right?"
        "What would that conversation even look like?"
        "Sonal, I didn't change my password." 
        
        show son annoyed at top
        "Okay."
        "...And then that would be it. Exceptionally inane and Sonal would judge me even more than she already does."
        jump firstMarcosDecision

    stop music fadeout 1
label firstMarcosDecision:
    "Just as it starts getting to extremely awkward levels of silence...."

    play sound "audio/sfx/35-sfx_kettlebeep.ogg"  volume 0.3

    "As if summoned by the sound of the kettle, Marcos sweeps into the kitchen trailed by not one but at least ten, posh-looking uni students."
    
    show son angry at top
    "I exchange looks with Sonal, temporarily stunned into an alliance against the absurdity of the scene before us."

    show son annoyed at topright with dissolve
    show ma at topleft with dissolve
    ma "Oh, perfect timing."
    
    play music "audio/MARCOS 1 - Black Tears by Mr Smith.mp3" fadein 2 volume 0.6
    "We both watch as Marcos makes himself a cup of tea."
    "And then another, and another, until it's clear he's going to use all of the water in the kettle to offer tea to all the students."
    "Sonal opens and closes her mouth, unable to speak."

    stu "Thanks, Mr. Roble!"

    show ma laughing tinyflowers at topleft
    ma "Of course! And even as our interns, you can call me Marcos. After all, I've known most of you since you were in nappies."

    "Ah… nepotism interns."
    "Wait, interns? {w}Shouldn't they be the ones making tea?"
    "Faintly, I can hear Sonal muttering something under her breath." 

    show son angry angermark at topright
    son "How can anyone be so– so—"

    "She partially turned away from Marcos so he can't see her mouth moving and I get the sense that the unfinished statement is directed at him."

    menu:
        "Offer to boil more water.":
            $ goodChoiceSonal+=1

            jo "Lucky that we have more kettles, right?"
            jo "I'll just put another on right now."
            hide son angermark
            show son annoyed at topright
            "Sonal nods somberly."
            jo "Do you want to go and ask if anyone wants a cup now?"
            show son at topright
            son "I just… {w}I'll um… yes. {w}I'll be back later."

        "Rationalise what just happened.":
            $ goodChoiceMarcos+=1

            jo "Well… I suppose we should treat our interns nicely on their first day here, especially if they have ties to important people to the company…"
            hide son angermark
            show son annoyed at topright
            son "You honestly think that?"
            jo "It… it makes sense logically…?"
            jo "We can always boil more water."
            son "I guess."
            son "I'm going to-{w} I'll be back.{w} Later."

    hide son with dissolve
    hide ma laughing tinyflowers with dissolve
    show ma at top with dissolve
    "Sonal leaves the kitchen. The motion makes all the interns turn towards where she was standing. {w}Where I'm still standing."
    "As if they only just noticed me for the first time, the interns give me a very obvious once over."
    "I am distinctly anxious under the scrutiny of the youths and mutter a silent thank you to whatever possessed me to dress up a little more today."

    stu "What do you do here, miss?"
    "Miss. {w}I feel inexplicably ancient."
    "Before I can even speak, Marcos grins."

    ma "[playerName!q], here is an invaluable part of the office."
    "I'm a little shocked at Marcos' positive assessment."

    show ma laughing at top
    ma "Even now, she keeps us all running by selflessly keeping watch over the kettle."
    "The students chuckle amongst themselves. {w}I feel any positive vibes drain out of my body, replaced by a deep upset."
    ma "Let me tell you, on any other day, there would be a distinct line of mugs on the counter and three kettles full of water boiling for the morning rush for tea."

    show ma at top
    ma "Someone's got to keep it all operating smoothly."
    "He makes it sound like this is my entire job."
    "Marcos raises his eyebrows at me, smiling like he's letting me in on the joke."

    show ma laughing laughter at top
    "When I don't smile back at him, he laughs."
    ma "Alright, talk amongst yourself for a second. Take a few selfies if you want."
    "Surprisingly, the students comply, many of them taking photos with the various appliances in the kitchen."
    "Marcos approaches in several large strides and leans over to speak at a volume that the interns can't hear."

    hide ma laughing laughter
    show ma at top
    ma "Thank you for humouring me. We wouldn't have had time to stop for tea otherwise."
    ma "You look very nice today, by the way."
    "In spite of my annoyance, I can't help feeling a little pleased to be told this by Marcos who, as rumour has it, frequently hangs out with super models."
    ma "Thank you for putting in the effort on an important day.{w} We can't have the kids of major investors thinking we're not worth interning with."
    "..."
    "It's not like I knew there were rich students coming to work today! It's not like I dressed up to impress anyone here!"
    "Don't I make enough of an effort every day?"
    "Is it really such a drastic change?"
    show ma obnoxious sparkle at top
    ma "Oh would you look at the time! Time to move onto the next leg of our tour."
    ma "Feel free to leave your mugs on the table. [playerName!q] will get to them, no problem."
    
    stop music fadeout 1

    hide ma with dissolve
    jo "...."
    "The students file out of the kitchen after Marcos, leaving a summoning circle of mugs in their wake."
    "Perhaps, I should have been smart like Sonal and gotten out of here while I still could."
    "I sigh and startput another kettle on, before turning to gather the mugs and put them in the sink."

    scene bg_office_desks with fade

    "Luckily it's a slow day and Alex and I are able to head out a little early for lunch."

    scene bg_lunchspot with fade

    show al at top with dissolve
    play music "audio/GENERAL 2 - Day Trips by HoliznaCC0.mp3" fadein 2 volume 0.6
    al "I called ahead so it shouldn't take too long."
    "Of course, Alex being Alex, we are suddenly responsible for grabbing food for a bunch of people in the office."
    jo "Feels an awful lot like intern work."

    show al happy at top
    al "Doesn't it?"

    show al annoyed at top
    al "Speaking of…"
    "Alex gets uncommonly serious all of a sudden."
    jo "...speaking of? What's wrong?"
    al "Don't take this the wrong way, [playerName!q], only I wanted to be sure… you're not dressed up today to attract someone specifically at the office, right?"
    jo "What?"
    jo "No, of course not. Is that what you think?"

    show al nervous at top
    al "No, sorry, I just…"

    show al nervous flyingsweat at top
    al "I overheard one of the interns in the bathroom say that you um… {w}You seemed very close with Marcos.{w} That it seemed like you were um… fr- friendly."
    jo "And you wanted to check?"
    al "Well no. Yes. {w}I'm concerned about you, you know? {w}Workplace romances can get really ugly."

    hide al nervous flyingsweat
    show al sad at top
    al "And Marcos is… {w}Well… {w}Trust me when I say he's not someone you want to get involved with."
    al "Just… be careful, alright?"
    jo "Thanks."
    al "Oh [playerName!q], you know I'm not saying this to be petty or–"
    jo "Well, I can tell you emphatically that the reason I wore these clothes in the first place was not related to work at all."
    jo "In fact…"
    "In fact…"
    jo "My ex posted a new photo of their new partner over the weekend, so I just wanted to look better than them, okay?"
    stop music fadeout 1
    "..."
    "Oh no, I really didn't mean to say any of that out loud."
    al "[playerName!q]..."
    jo "Let's not talk about this. Please."
    al "Alright."

    show al at top
    "It's awkward heading back together after that but I just focus on picking up the orders. And Alex always has things to share to fill the silence."
    "She's probably babbling a bit out of fear she offended me, but I find that I'm fine letting her keep talking out of guilt."

    scene bg_office_desks with fade

    "We end up eating lunch at our respective desks but not even my queued up cat videos are enough distraction from my increasingly distressed thoughts."
    "Does everyone think I dressed up to impress someone? {w}Why do I have no control over the narrative when I'm at the centre of it?"
    "I find myself closing my cat videos and opening Tangram and pulling up that photo."
    "Even unconsciously, I know the outfit I chose references Her look. {w}The cut, the styling, everything down to the makeup is a little bit of an homage to this image."
    jo "This is crazy ex behaviour."
    "Well… the heels are different. I have that to hold over Her."
    "After all…"

    scene bg_flashback_park with flash
    play music "audio/SAD - A Cool Electric Rainy Night by Mike Durek.mp3" fadein 2 volume 0.6
    jo "Mum always told me that green wasn't a good colour for me."
    show ex at top with dissolve
    ex "What? It looks great on you!"
    ex "I might be biassed though. {w}Green is my favourite colour."
    ex "It's just so energetic and full of life. {w}Calm and collected, you know?"
    jo "Energetic and calm?"
    ex "You know what I mean."
    jo "Some things hold multitudes?"
    ex "Always the big words with you."
    
    stop music fadeout 2
    scene bg_office_desks with flash
    "Maybe the sight of me scowling at my desk is enough to put anyone else off approaching me, but at the end of the day, Alex still drops by."
    
    play music "audio/GENERAL 3 - Thursday Afternoon by saavane.mp3" fadein 1 volume 0.6
    show al at top with dissolve
    al "Hey, just wanted to let you know we got approval for the next stage of the Bittenmore case."
    jo "Oh, that's good news."

    show al sad at top
    al "...And… Well…{w} Sorry, I just wanted to apologise if I made you upset today. Sorry."
    al "But I also understand if you're still upset though and don't want to talk about it."
    "I feel a little annoyed already that she's making assumptions about how upset I am, but I appreciate her giving me an out."
    jo "I think I just need to sleep on it."
    "I offer her a tentative smile."

    show al happy at top

    al "Alright, well, I'll see you tomorrow then!"
    jo "See you."

    stop music fadeout 0.6
    hide al with dissolve
    "I glance at the clock. I've somehow managed to go an hour over my preferred time off."
    "Instinctively, I look around to make sure no one is coming my way with a last minute request."
    "I'm so mentally worn out, I don't think I can take much more." 
    jo "Well, the best remedy for too many thoughts is a way to have no thoughts."
    "Where should I go to get that fix?"
    menu:
        "Head home and sleep all the bad vibes off.":
            jump firstWeekGoHome

        "Go to the bar and drink all the bad vibes away.":
            $ weekOneGoOut = True
            jump firstWeekGoBar
    #—--------- HOME
label firstWeekGoHome:
    "Even standing up is a chore. I can feel my heels cutting into my feet in a way I must not have felt all day through sheer willpower."
    jo "Best to get home as soon as possible."
    
    scene bg_transition_subwaysign with fade
    jo "Ow."
    scene bg_street_night with fade
    jo "Ow."
    scene bg_flat_stairs with fade
    jo "Owwww."

    "Let's just… let's just sit on the stairs."
    "Maybe forever."
    jo "Why did I think this was a good idea…"
    jo "I can't even take them off, they're actually stuck to my skin."
    jo "I would kill to have a massage right now."

    play sound "audio/sfx/36-sfx_samdescendingstairs.ogg" volume 0.3
    pause(4)

    play music "audio/SAM 2 - Windows Down by Holizna CC0.mp3" fadein 2 volume 0.6
    show sa home_neutral at top with dissolve
    sa "I thought I heard you whining."
    jo "How? Don't you usually have headphones on?"
    sa "Was coming down to get my mail. And besides, your voice is one of those unblockable frequencies even with noise cancelling, like a baby crying. Whaa, whaaa."
    jo "You try wearing brand new heels for a full work day. See if you don't 'whaa whaa' yourself."
    show sa home_amused at top
    sa "And why did you decide that was a good idea?"
    jo "I… I guess I just wanted to… look you know… like I can dress up too. Clean up well."
    sa "You already do that every day for work."
    jo "Yeah well… maybe I wanted to impress someone."
    "I wince."
    jo "Not at work, of course. Just… in general."
    sa "You know, your ex can't see what you look like at work."
    jo "I was so vague about it. How did you know?"
    show sa home_neutral at top
    sa "You're more predictable than you think." 
    sa "And prone to not knowing what's healthy and what's not."
    "Well. {w}Sam speaks from experience, considering our mutual history. {w}I wince again."
    sa "Also, I'm friends with him on Tangram."
    sa "Anyway, I know you're not looking for advice, but maybe consider only doing things that make you happy, you know?"
    sa "At least, that's how I get around doing too much for other people. How I keep myself safe from bad, foot breaking decisions."
    "I stick my tongue out at him. {w}Sam continues unfazed."
    sa "Then, if the decision you made goes sideways, you don't really regret it because you stuck to your guns or it made you genuinely happy."
    sa "Of course, some part of this relies on knowing the difference between confidence and hubris and I think you have a special brand of shamelessness that stops you from thinking before you leap."
    jo "I'm not shameless. {w}I have plenty of shame."
    sa "Mmm… not enough that you've learned your lesson. {w}I think I should leave you here to let you think on it some more."
    jo "No please. {w}Help me up the stairs."
    jo "I can think about things in the comfort of my own bed."
    sa "....."
    jo "Okay, I might go right to sleep but please, you can't leave me here."

    show sa home_amused at top
    sa "Fine, but you owe me three cans of cat food."

    show sa home_neutral at top
    jo "For your dinner?"
    "Sam rolls his eyes as he leans in to help me up."
    jo "Speaking of, what are you having for dinner?"
    sa "Why do you want to know?"
    jo "Don't worry, I'm not asking you out."
    sa "You would be getting a resounding 'no' if you were."
    jo "Yes, I'm aware."
    jo "...Doesn't hurt to try though every once in a while, right?"

    show sa home_annoyed at top
    sa "A no is a no."

    show sa home_neutral at top
    jo "Alright, alright. I'm just asking– about dinner, not dinner with you–I just remembered that I spent all weekend shopping for clothes but I never picked up more groceries."
    sa "So…"
    "So…I could ask Sam if he wants to go with me to get groceries…"
    "No, that feels like asking too much."
    "But if I got take-away…"
    "Well, there's a chance he might still say no so…how can I phrase this in a way that will convince him to come with?"

    stop music fadeout 1
    menu:
        "\"Do you want anything if I'm getting kebabs?\"":
            $ goodChoiceSam+=1

            "Sam stops to think about my offer."

            show sa home_happy at top
            sa "To be honest, I haven't had a proper meal today–very unhealthy, I know."
            show sa home_shocked disgust at top
            "Sam's stomach grumbles as if to support the point and he laughs."
            hide sa home_shocked disgust
            show sa home_laughing at top
            sa "Alright, yes, kebabs sound pretty damn delicious right now. {w}I'll take you up on your offer."
            jo "Great! {w}Let me just change shoes and I'll be on my way. As soon as I can. Which is, you know, whenever I can walk with a little less pain."

        "\"I'm getting a kebab and I'm ordering something for you too.\"":

            "Sam stops walking."
            sa "Huh. {w}And if I said I wasn't hungry, what then?"
            jo "Uh… well… {w}It's good that you said that."
            jo "Now I know. {w}Happy to eat alone."
            jo "But I knew you were going to turn me down anyway so…"
            show sa home_amused sigh at top
            "Sam sighs and gives me a tired smile."
            sa "Since you know me so well, I would've thought you'd know to ask. {w}I'm not a big fan of having decisions made for me."
            "Oh right. {w}I did know that. {w}Sam's pet peeve is when people assume they know the best for him."
            jo "Sorry. {w}You don't have to go with me–"
            hide sa home_amused sigh
            show sa home_neutral at top
            sa "But, the good news is I actually am hungry. And luckily, I've got nothing against getting kebabs with you."
            sa "I can order something for myself though, no worries about having to bribe me with free food."
            jo "Really? I mean, alright, give me a moment to change my shoes and then we can be on our way."

    play music "audio/SAM 2 - Windows Down by Holizna CC0.mp3" fadein 2 volume 0.6
    show sa home_neutral at top
    sa "What, you're going to walk there?"
    jo "Yeah, why not?"
    "Sam gestures at my feet."
    sa "Confidence or hubris?"
    jo "Yeah but it makes me happy to get kebabs for us."

    hide sa home_neutral
    scene bg_flat_hall with dissolve

    "As we reach the top step and enter the upper level of the building, I grimace in pain."
    show sa home_neutral at top with dissolve
    sa "..."
    show sa home_neutral sweat at top
    sa "I'm not doubting your ability to get your own kebab but how about this: you call in the order and I pick it up?"
    jo "No, I couldn't do that. {w}I offered."

    hide sa home_neutral sweat
    show sa home_neutral at top
    sa "Alright but here's my counter offer. {w}You order, I pick up, and you catsit while I'm gone."
    "I waver at the word 'sit', feeling like I'm on the verge of irreparable damage to my feet already."
    jo "You drive a hard bargain."
    sa "Final answer?"
    jo "Fine, fine, yes, you can pick up the kebabs since you're willing and I'll sit. {w}I mean catsit."
    show sa home_amused at top
    "Sam smirks at my obvious Freudian slip."
    sa "You can still stop by your place to change first, if you want. {w}Otherwise, you're going to get cat hair on your clothes."
    jo "Eh, I can take a little fur."
    sa "Alright but don't say I didn't warn you–they're all shedding like crazy."

    scene black with fade
    play sound "audio/sfx/45-sfx_samopendoor.ogg" volume 0.3
    pause(2)
    scene bg_flat_sam with fade

    show sa home_neutral at top with dissolve
    jo "Feels like I haven't been in here in forever."
    "Sam raises an eyebrow."
    sa "You were here early last month."
    jo "Oh."
    "Right. {w}Probably right after the breakup."
    jo "Sorry about that."
    sa "About your last visit? No, don't worry about it. {w}You weren't exactly at your peak state to be the perfect house guest."
    jo "Mmm."

    play sound "audio/sfx/37-sfx_catmrp.ogg" volume 0.3
    ex "Mrrp."

    "I feel something rub against my leg."
    "Staring up at me with glistening, blue eyes is a very fluffy white cat."
    jo "How are you GarJo?"

    hide sa home_neutral with dissolve
    show sa home_neutral at topright with dissolve
    show garlic at left with dissolve
    play sound "audio/sfx/38-sfx_catmrao.ogg" volume 0.3
    gar "Mrao."

    "She leans into my palm as I run my hand down her back."
    "Within seconds, I feel another warm, furry body pressing into my other leg."
    "This time, it's a lithe tuxedo cat, winding around my heels."
    play sound "audio/sfx/39-sfx_catpurr.ogg" volume 0.3
    jo "Miss Scallion."
    hide garlic with dissolve
    show garlic with dissolve
    show rapscallion at left with dissolve
    
    "Rapscallion purrs."

    show sa home_amused at topright
    sa "If you keep petting them, they'll never let you sit down."
    sa "Do you need help getting your shoes off?"
    jo "Um… yes, thanks. Seems like we're doing this every week."
    sa "Your fault for being shoe challenged."

    show sa home_neutral at topright
    "Sam tries to remove my heels as gently as possible but it still hurts. {w}I feel blood flooding into my numb toes as well as the telltale sign of blisters having formed."
    jo "Owwww."
    show sa home_happy at topright
    sa "You're free now, Cinderella."
    sa "C'mon ladies, let her pass."

    hide garlic with dissolve
    hide rapscallion with dissolve

    show sa home_neutral at topright
    "Sam leads my hobbling self to the couch where an orange cat is already loafing with a wary expression on its face."
    sa "Ginger's a bit bitey today so watch yourself."
    jo "Mr. Gingersnap is always bitey. {w}A big spicy boy."
    show ginger with dissolve
    "Gingersnap blinks ever so slowly at me and then looks away."
    hide ginger with dissolve
    sa "You're ordering by phone, right?"
    jo "Oh, right."
    "Sam gives me his order and I make the call"
    jo "They said they'll be ready in 20 minutes."

    hide sa with dissolve
    show sa home_amused at top with dissolve
    
    sa "Cool, I'll be on my way then. {w}You good here?"
    jo "Yeah."
    sa "Alright. Back in a minute."

    hide sa with dissolve
    play sound "audio/sfx/26-sfx_samleaves_doorclose.ogg" volume 0.3
    stop music fadeout 0.2

    "The flat is unnaturally silent once Sam is gone–if only for a moment."
    "Almost as soon as the thought passes my mind, the room is filled with a plaintive meow that gets progressively agitated."

    show garlic with dissolve
    play sound "audio/sfx/40-sfx_catmeowloud.ogg" volume 0.3

    gar "MEOW"

    "Garlic screams into the void at being abandoned."
    jo "GarJo, I'm right here."

    "She dismisses my presence in a single glance and continues to meow demandingly."

    #sfx continued meowing
    show rapscallion at left with dissolve
    "Rapscallion joins in the fray shortly afterwards, meowing and eyeing the kitchen counter tops with clear premeditated intent."
    play sound "audio/sfx/41-sfx_catmeowmultiple.ogg" volume 0.3

    jo "Not you too, Scallion."
    "Ginger bristles a bit and yawns. {w}He hops off the couch and smoothly segues into a full body stretch."

    show ginger at right with dissolve
    "I watch him warily as he pauses to swipe halfheartedly at my phone on the coffee table… {w}Then my keys… {w}Then my purse."
    "I can just imagine the fallout of Sam returning to find his cats committing their devious kitty crimes under my watch." 
    jo "Maybe I can placate them with treats?"
    "As far as I know, Sam isn't one to over-pamper his cats with extra snacks but, like most cat owners, he does have emergency treats tucked away."
    "I get up, wincing as I put pressure on my feet."
    jo "Treats, treats, treats…"
    "As I look through the cabinets, Garlic, Scallion, and even Ginger start winding themselves around my ankles."
    jo "I see you already know what's up."
    jo "I guess it's faster just to text Sam and ask where they are. {w}Even if it gets me a lecture about cat nutrition."
    "I grab my phone and send Sam a message, only to hear a soft pinging noise from inside the same room."
    
    play sound "audio/sfx/43-sfx_textnotif.ogg" volume 0.3

    "The sound came from a mobile on the dining table that I didn't see before."
    jo "No way, did he leave his phone here?"
    "A rare occurrence. Sam usually has a tight grip on his belongings."
    jo "He shouldn't need it to pick up the order but…"
    "Another ping."
    "I glance at the notifications lighting up the screen."
    "It's a text with many heart and heart related emojis."
    jo "Is Sam dating someone new?"
    "As far as I knew, he wasn't even looking to be in a relationship."

    play sound "audio/sfx/43-sfx_textnotif.ogg" volume 0.3
    "Another text message notification sound goes off."

    menu: 
        "Read the messages as they come in.":
            "Even driven by pure curiosity, I feel a little guilty as I quickly peruse the preview of the incoming text."
            jo "Well, it's not like I'm unlocking his phone to read the messages. I just happened to glance at them as the notifications came in."
            "The next message reads \"So cute!!\""
            jo "Message from…whoever B \"theatre masks emoji\" is."
            "I can't help but start to wonder who this mystery person is as well as what Sam is sending them to warrant a \"So cute\" with two exclamation marks."
            jo "Not that I have any say over Sam's social life."
            "But I feel a little possessive, if only because I don't fully understand the context of the relationship here."
            
            play sound "audio/sfx/44-sfx_catmeow.ogg" volume 0.3
            gar "Meow."

            "I'm jolted out of my racing thoughts."
            jo "R-right. Kitties."

        "Don't read any more messages.":
            $ goodChoiceSam+=1

            "As much as I am dying to know who…\"B theatre masks emoji\" is and why they're sending hearts to Sam, the warning bells go off in my head."

            "It just feels wrong to pry."
            "It's not like I'm his jealous girlfriend anyway. And well…I have enough of that happening in my life already, even if it's from the position of an ex-girlfriend."
            jo "You didn't see anything, [playerName!q]."
            "I step away from Sam's phone and actively try to think about other things."

            play sound "audio/sfx/44-sfx_catmeow.ogg" volume 0.3
            gar "Meowrao."
            jo "Oh right, treats."


    hide garlic with dissolve
    pause(1)
    hide rapscallion with dissolve
    "Suddenly, Garlic runs for the door. Scallion hops down from where she was standing on the counter, having snuck up in my moment of weakness." 
    hide ginger with dissolve
    show ginger with dissolve
    "Ginger walks by as if to also approach the door but instead tackles my foot and nips a few toes."
    jo "Ow, ow, please, Ginger, no biting."

    play sound "audio/sfx/45-sfx_samopendoor.ogg" volume 0.3
    "A second later, Sam opens the door."
    sa "Ginger, no."

    hide ginger with dissolve
    "Surprisingly obedient, Ginger stops kicking my heels and, after a moment, gets up to greet Sam like the others."

    show sa home_neutral at top with dissolve
    sa "Everything okay here?"
    jo "Just great!"
    "My words come out a little too enthusiastic to be convincing, though it's not like I actually did anything wrong."

    show sa home_amused at top
    sa "Cool. There was a little mixup but they gave us some extra food because it's the end of the night. {w}I was going to call you to let you know I was delayed a bit but I think I left my phone here."
    jo "You did."

    show sa home_annoyed at top
    "I wince. {w}Now he knows that I know his phone was here."
    "Except on second thought, I did have a valid reason…"
    jo "I tried to text you to ask if you had any cat treats."

    show sa home_neutral at top
    sa "Oh were they giving you a hard time?"
    jo "Nothing too bad."
    "Instead of launching into his thoughts on cat parenting and rewards, like I expected, Sam picks up his phone and peruses it momentarily before putting it away in his pocket."
    sa "Shall we eat?"
    "I feel a weird sort of pride in being placed higher up in priority than the mysterious texter."
    sa "[playerName!q]? Why are you smiling to yourself?"
    jo "Just so excited to eat!"

    show sa home_happy at top
    "Sam laughs and hands me my food as a chorus of meows rise up from the cats who insist they deserve a share."

    jump weekOneEnding

    # —--------- BAR
label firstWeekGoBar:
    
    "They say alcohol is the best medicine for tired feet."
    "No, no one says that."
    "I still find myself heading to the Better Days Bar anyway."
    
    scene bg_bar with fade
    play sound "audio/sfx/46-sfx_barambience2.ogg" volume 0.3

    show be at top with dissolve
    play music "audio/BAR 3 - Detailing by Blue Dot Sessions.mp3" fadein 1 volume 0.6
    be "[playerName!q]."
    jo "Hi Bernard. Busy in here today, huh?"
    be "Stag do pub crawl. {w}They've been here for a while so they should be on their way out soon." 
    "We both watch as one of the men in the stag party attempts to drunkenly toss a ping pong ball into a haphazard formation of red cups."

    play sound "audio/sfx/47-sfx_barcheer1.ogg" volume 0.3

    "He misses and everyone cheers."

    show be at top 
    be "Anyway, what can I get you today?"
    jo "Uh… what do you have that's good for numbing pain?"
    
    show be amused at top
    be "That bad of a day?"
    jo "Well yes and no. {w}But really my feet are just killing me. {w}Though I wouldn't say that I couldn't be in a better mental state too."

    show be annoyed at top
    "Bernard says something to himself, not quietly, but not particularly directed at me either."
    be "Give me a bowl of wine. I have not that alacrity of spirit, nor cheer of mind that I was wont to have."
    "I do a double take, not sure if I just suddenly stopped understanding English or if Bernard has stopped speaking it."
    jo "..."
    jo "Is that… a reference to something?"
    
    show be shockmark at top 
    "Bernard looks surprised and then smiles."

    hide be shockmark
    show be happy at top 
    be "Richard III."
    be "The play, not the king."
    
    hide be happy
    show be at top
    jo "Shakespeare, right? We only did Macbeth and Romeo and Juliet in school. I think Hamlet too, but if I'm being honest, I got by without fully reading that one."
    be "It's pretty interesting rereading them as adults outside of an academic setting."
    jo "I'll take your word for it. {w}In my opinion, Shakespeare is best left to historians and other boring people."

    show be questionmark at top
    
    "Bernard gives me a strange look."
    "Some tidbit of forgotten information passes through my mind, too fast to really let sink in."
    "Ah wait. {w}Wait, wait, wait."
    "Bernard… {w}Bernard is an actor."
    jo "And the interesting people! {w}Like theatre people!"
    jo "D-do you have other quotes about drinks that you just have to know while working in a bar?"
    "Bernard laughs."

    hide be questionmark
    show be amused at top
    be "It's a personal choice, not a mandatory curriculum, no."
    "Bernard passes my drink over the counter."
    
    play sound "audio/sfx/48-sfx_drinkpass.ogg" volume 0.3

    be "Good wine is a good familiar creature, if it be well used."
    jo "Let me guess… A Midsummer's Night's Dream?"
    be "Othello."
    be "Although, that line is uttered by the villain trying to guilt someone they already got drunk once into unknowingly participating in a malicious plot against his boss."
    be "So… {w}Perhaps not the thing for your bartender to say as they offer you a drink."

    show be happy at top
    jo "You're not going to convince me to plot against my boss?"
    be "Not this time."
    "A loud cheer goes up behind me as the members of the stag do celebrate another miss."
    
    play sound "audio/sfx/49-sfx_barcheer2.ogg" volume 0.3

    hide be happy 
    show be at top
    be "A lesson in picking your friends and not letting other people control the narrative. {w}And, I suppose, drinking in moderation."
    jo "What, beer pong?"
    be "The point of Othello."

    hide be with dissolve
    "Bernard leaves me alone with my thoughts as he goes to pour someone else a drink."
    "I remember that I was lamenting about that exact thing earlier: not having control over my narrative."
    "How did Bernard know? Special bartender senses?"
    "Although… {w}I guess Bernard doesn't have much control over how his work day goes either, what with the rowdy bachelors and all."
    "When Bernard returns, I decide to cut him some slack by actively not talking about myself. What's an interesting conversation topic?"

    stop music fadeout 1
    menu: 
        "Ask Bernard about his life.":
            $ goodChoiceBernard+=1

            show be at top with dissolve
            play music "audio/BAR 3 - Detailing by Blue Dot Sessions.mp3" fadein 1 volume 0.6

            jo "How are things recently, Bernard?"
            be "In the bar? Not too bad."
            jo "And in life?"
            be "Not too bad."
            jo "Right."
            jo "Nothing you want to get off your chest?"
            jo "I feel like I complain to you quite a bit, is all. {w}I'm here to reverse the roles and listen for a bit if you'd like?"

            show be amused at top
            "Bernard smiles."
            be "That's very nice of you."
            "Bernard picks up a wine glass and starts polishing it."
            be "Well, if I'm being honest, I've been kind of stressed lately."
            jo "Lot of disorderly drunks recently?"

            show be happy tinyflowers at top
            be "I'm in a play right now, in the leading role."
            jo "Oh wow, congratulations!"
            "I never would have guessed. Bernard's here all the time as far as I know."
            jo "When do you find time to practise?"
            
            hide be happy tinyflowers
            show be at top
            be "Most of our rehearsals are during the day. Just upstairs actually."
            "I glance at the ceiling. {w}I knew a lot of pubs had small-scale theatres above them, but I didn't realise this bar was one of those places."
            "I guess I wasn't paying enough attention to the people around me."
            be "I also do a smidge of practice at home after work."
            be "It's no West End production, obviously, but I still need to bring my best."
            "Bernard sets the glass down and picks up another."
            be "I know the words by heart but I still get nervous."
            be "We have about a month left of rehearsals so… {w}Just enough time to start panicking, if I'm not careful."

            show be amused at top
            "Bernard gives me a wan smile."
            be "The closer we get to the opening, the more dreams I have that I'm going to walk on stage and just freeze."

            show be annoyed at top
            be "I know it's irrational. {w}You'd think I'd never acted in my life. {w}I've never been in a leading role, though, so that's probably contributing to my nerves. {w}And nightmares."
            "Bernard moves onto a third glass."
            be "It's just that if I get this right, I know I can dazzle the crowd and maybe impress some important people."

            hide be annoyed
            show be at top
            be "But you know, you can't control what the audience thinks of you. {w}What they bring with them into the theatre and what they take out of it. {w}All I can do is give my best performance. Something I'm satisfied with."
            be "That's true in all of life isn't it?"
        
        "Ask Bernard for advice.":
            show be at top with dissolve
            play music "audio/BAR 3 - Detailing by Blue Dot Sessions.mp3" fadein 1 volume 0.6
            jo "Bernard… Have you ever tried to change who you were to match someone else's ideal?"
            show be annoyed at top
            be "Hmm…"
            be "I suppose I run into that problem a good bit as an actor."
            be "As much as anyone can technically play any role in theatre. {w}And we certainly have seen it happen throughout history. {w}There are… preferred conventions that people tend to fall back on."
            
            hide be annoyed
            show be at top
            be "I'm lucky to be working at a smaller scale where there's less pressure to conform, but it still looms overhead."
            jo "Oh."
            "That sounds difficult indeed. {w}But I guess I meant…"
            jo "What about in your personal life?"

            show be annoyed at top
            "Bernard visibly hesitates."
            be "My personal life?"
            "Bernard spends so long staring at the glass he's polishing that I wonder if I've made a blunder and asked something too personal after all."
            be "Thinking back, there were a few instances, but… {w}It was a long time ago."
            be "I eventually learned that I shouldn't pretend to be someone that I'm not for other people's approval."
            be "Funny to say that considering my line of work."
            "It takes me a second to remember he's referring to acting not bartending."
            be "Especially when it comes to relationships that are based in communication, it's best to just be yourself."
            "Did Bernard get out of a relationship that broke down from miscommunication too?"
            be "Compromising yourself for someone else is a surefire way to feel like garbage all the time."
            "I do indeed feel like garbage."
            "I down the rest of my drink."
            jo "What did you do to not feel gross?"
            
            hide be annoyed
            show be at top
            be "Well, first, giving myself room to feel that way was important. {w}I had to recognize what I was feeling and why I felt that way."
            be "And then, afterwards, I made sure that any improvements I made upon myself were actually worth something. {w}That I was doing things to be happy or to grow as a person in a positive direction. {w}That's the best way to keep moving forward."
            jo "I guess that makes sense."

            show be happy at top
            "Bernard smiles."
            be "Of course, taking my advice is also something you should think about in your own terms. {w}If it makes you happy or helps you improve, by all means…"

    hide be happy
    show be at top
    "I realise this might be the most I've ever heard Bernard speak without interruption."
    "He has a nice voice, well suited for an actor."
    "He smiles suddenly. He has a nice smile too."
    be "What is it?"
    jo "Oh god, was I staring?"
    jo "Sorry, was just thinking you have the kind of voice people would go wild over in the youtube comments."
    be "Oh."

    show be laughing laughter at top
    "Bernard laughs."
    be "That's quite the compliment."

    hide be laughing laughter
    show be at top
    jo "I guess I never listened closely before, what with all the usual noises in the bar."
    "From behind, the stag do group lets out a loud cheer, even louder than before."
    jo "I thought they would have left by now."

    hide be with dissolve
    "One of the party approaches the bar and Bernard steps away to fulfil their order." 

    show be at top with dissolve
    "When Bernard returns, he gestures towards the man who's waiting at the counter."
    be "Would you like another drink? The \"gentleman\" down there is buying."
    "I turn and accidentally make eye contact with said \"gentleman\"."
    "He grins and waves."
    "Am I feeling another drink?"
    "Tomorrow is another work day. {w}I probably shouldn't but…it might make me feel better?"
    "A more rational part of me recognises that the \"feel better\" part is going to be temporary."
    "Bernard waits patiently for my answer."

    stop music fadeout 1
    menu: 
        "Accept.":
            $ acceptBernardDrink = True
            "Why not."
            jo "Let's have another then."
            "Benard nods and pours another drink for me."
            "I raise the glass to the stranger who raises his own."

            play sound "audio/sfx/51-sfx_booing.ogg" volume 0.3
            "We each take a big sip of our respective drinks before he returns to his friends. They let out a chorus of boos."
            "The combination of the sound and the additional drink make my head spin a little."

        "Decline.":
            "Better not."
            jo "I think I'm good for the night."
            "Bernard shakes his head at the man."

            play sound "audio/sfx/51-sfx_booing.ogg" volume 0.3
            "The stranger raises a glass to me and heads back to his loudly booing friends."

    play music "audio/BAR 3 - Detailing by Blue Dot Sessions.mp3" fadein 1 volume 0.6

    be "That was the tamer version of that dare that I've seen."
    jo "That was a dare?"
    be "Most likely, yes. I've seen a few where one of them gets sent to ask someone out as punishment."
    be "Usually doesn't end well but sometimes you get a couple… couples."
    jo "Felt like a cop out then."

    show be laughing laughter at top
    "Bernard laughs."
    be "Were you looking to be asked out?"

    hide be laughing laughter
    show be at top
    jo "...No."
    be "Well, I say good on him, not getting swayed by his friends. Keeping his distance was a respectful move."

    
    if acceptBernardDrink:
        show be amused at top
        jo "You know, I think I've had enough for today after all."
        "Seeing a random stranger have more conviction to be themself in the face of social pressure makes me want to go to bed."
        "Or maybe it's just bedtime regardless."
        jo "Gonna head out now, Bernard. Cheers."
        be "See you around. {w}Get home safe."

    stop music fadeout 1
#---------------
label weekOneEnding:
    scene bg_flat_mc_dark with fade

    if weekOneGoOut:
        "I stagger into my flat. {w}My feet are screaming from the trip home and the alcohol in my system and god, am I eager to be rid of these heels."
        "With some difficulty, I peel them off and discard them amongst my other shoes."
    else: 
        "I get back to my flat, full but tired, with my feet still in subpar condition."
        "My heels, which I decided to leave off for the rest of the night, are dumped haphazardly onto my shoe rack."

    "For some reason, {w}I'm saddened by the sight of the new shoes, creased with one day's wear and the clear signs of something shoved into a container that was an ill fit."
    jo "Do shoes count as a container?"
    "That silly line of thought doesn't really hide the sudden melancholia I feel."
    "I made the choice to wear those heels after all, even if I could have predicted the aftermath. {w}Was it really worth the damage to both my feet and the shoes though?"

    if weekOneGoOut:
        show be happy at top with dissolve
        "Bernard's words about being authentic to myself rather than pretending to meet someone else's standards come to mind."
        "I thought I was meeting my own standards, honestly…so why do I feel so much regret?"
        hide be happy with dissolve
    else:
        show sa happy at top with dissolve
        "Sam's words about not doing anything that doesn't make me personally happy come to mind."
        "I thought it did make me happy at the time…so why do I have so much lingering regret?"
        hide sa happy with dissolve

    "Regret about… {w}Just the shoes right?"
    
    scene bg_flat_mc_bed with dissolve
    play sound "audio/sfx/27-sfx_gettingintobed.ogg" volume 0.3

    play music "audio/SAD - A Cool Electric Rainy Night by Mike Durek.mp3" fadein 0.5

    "As I sink into bed, the Tangram photo I was purposefully not thinking about flashes in my mind."
    "They looked happy and perfect together. {w}Well matched."
    "Unlike the damage that was wrought by two people desperately trying to fit each others' incompatible moulds."
    jo "What if I had kept at it though? {w}Would it have worked out?"
    "Like heels that are eventually broken in?"
    "Or would that have just led to more hurt in the end? {w}More than what a few bandages could repair?"
    "Did I do the right thing by removing myself when I did?"
    jo "No use dwelling on 'what-ifs.'"
    "But even as I close my eyes, that's all that fills my mind: a nightmarish spectacle of parallel worlds where we made it work one way or another."

    play sound "audio/sfx/28-sfx_poetrytyping.ogg" volume 0.3
    scene black with fade
    show cringepoetry2 with dissolve

    "It’s like you’ve made a home in the marrow of my bones"
    "And wrapped yourself around every blood vessel "
    "Until my cells stopped needing oxygen and started wanting"
    "You."
    
    stop music fadeout 1
    hide cringepoetry2 with dissolve
    
    return