# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters
define anna = Character("Anna")
define chris = Character("Chris")
define braden = Character("Braden")

# Character Images
image img_anna = im.Flip("anna.png", True)
image img_chris = "chris.png"
image img_braden = "braden.png"

# Character Images positions
transform anna_pos:
    xpos 450
    ypos 200
    zoom 0.8

transform chris_pos:
    xpos 800
    ypos 160
    zoom 0.8

# Backgrounds
image room1 = "room_1.png"
image room2 = "room_2.png"

# The game starts here.

label start:

    # Story flags
    $ shoot = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house_front onlayer bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show img_anna at anna_pos

    # scene house

    "You arrive at his house door – a thick wooden door with a hint of rot."
    
    "You vaguely smell the metallic iron smell from outside."
    
    "Such smell is common when iron in blood react with oils in your skins, resulting in release of molecules that we are sensitive to and identify as ‘metallic’ smell."
    
    "Therefore, he either has a giant iron statue in his house that he regularly touches or he might be a serial killer."

    "You knock on the door and to your surprise, within milliseconds, Chris opens the door as if he was waiting for your arrival right behind the door."

    show img_chris at chris_pos

    chris "Hi Anna! Please come in! Nice to meet you."

    "Briefly setting your suspicion aside for a moment, you greet him back with a pleasant smile."

    anna "Thanks! Nice to meet you too!"

    "You enter his apartment, only to be greeted by even stronger scents of iron." 

    scene room1 onlayer bg
    
    "You have major glances at your surroundings only to find a very ordinary apartment. No source of iron in sight."
    
    "You conclude that the smell must be coming from the basement."

    "You catch a glimpse of a sketchbook lying on the ground."

    # show img_sketchbook

    "" # empty line, wait for user input to hide img_sketchbook

    # hide img_sketchbook

    # show img_anna_pointing

    anna "I didn’t know you draw. May I examine them?"

    chris "Of course!"

    "You find many drawings of women’s clothes and naked women, some appear to be depicted to be dead." 

menu sketchbook:
    "Impulsively, you respond loudly in the following manner:"
    
    "Half-jokingly and with a hint of mockery":
        "This is a little creepy to be honest. I can’t even imagine what is hiding in your basement."
        jump sketchbook_mock

    "Serious":
        "Nice drawing. But I have to ask, what’s this smell of iron by the way?"
        jump sketchbook_serious

    "Nice cop":
        "They’re really nice! I’d love to see some more later!"
        jump sketchbook_nice

label sketchbook_mock:
    "Chris seems slightly rattled."
    
    chris "I disagree. You can’t judge me based on my personal taste in art."

    anna "Apologies. I meant it as a joke. But you gotta admit it is a bit unusual."

    "He suddenly pulls your hand, and thus your body forward violently."
    
    "You don’t know whether it is the result of him slipping or trying to intentionally harm you."
    
    "Your muscle memory from years of training makes you pull out your revolver and blindly shoot this man twice."
    
    "One grazes his arm, but the other one is more fatal. It has hit his stomach, penetrating his internal organs."

    chris "I just… wanted to show … my art.. Fuck you… What are you? A serial killer?.."

    "You stand there awkwardly. You look around only to find a giant metal statue standing before you, without a doubt, that is the source of the metallic smell."
    
    "You fucked up big time."

    anna "It’s your own damn fault! Why did you pull me so violently?"

    chris "I had no idea it was violent.. I just wanted to surprise you (he coughs repeatedly) I’m going to sue you until you are bankrupt! My daddy is a millionaire! You’ll regret this!"

    "You definitely don’t have the financial stability to risk it. Finishing him off might be a good idea." 
    
    "Should you shoot this man one more time? You are confident in your ability to lie about the incident to get away with minor punishment."

menu shoot:
    "What do you do?"

    "Yes. This guy is an ass.":
        $ shoot = True
        "His insults do not sit right with your ego. You are a big deal."

        anna "Who are you talking to right now? I am the detective responsible for arrests of over 100 big time criminals." 

        anna "I was handpicked by the commissioner to find the biggest serial killer in the history. You can’t threaten me, I am the threat!"

        "You plant a bullet deep into his heart. He squeals for 5 seconds, and then he was gone. You notice that your audio recording has been streaming into the cloud by accident."

        "Your life is now really fucked big time."

        jump epilogue

    "No! Killing is wrong!":
        "You quickly radio your headquarter for ambulance support. Your life will be slightly difficult from now on." 
        
        "But at least you did the right thing."

        jump epilogue


label sketchbook_serious:
    "Chris looks composed, as if he’d expected it."

    chris "I’m not sure if I’m comfortable with you enough to show you right now."

    "As you head further down the stairs, a giant iron statue appears." 
    
    "He kindly but seriously explain how he is creating it for an art show. All mystery has been solved and it’s clear that the smell came from this big ass iron statue."

    chris "This is the source of the smell. I hope you didn’t think I was a serial killer of something! Hahaha"

    anna "Of course not! haha. It really is a beautiful piece of art work."

    "You make something up about you having to leave immediately. You both say farewell."

    jump epilogue

label sketchbook_nice:
    chris "Finally! Some appreciation for my art! Thank you very much!"

    anna "I’d really love to see the basement by the way. Can we please?"

    chris "(reluctantly) Ok fine. I’ll show you."

    "You two head down to the basement."
    
    "As soon as Chris opens the door, the smell of iron amplifies to the point you can taste it." 
    
    "You think to yourself: there must be a lot of blood down there, or it has got to be one big fucking iron statue."
    
    "Subconsciously, you slightly back away."

    chris "Follow me. You wanted this didn’t you?"

    "He grabs your hand firm. It could be a sign of affection towards me, or he’s trying to harm me." 
    
    "Offering resistance at this time does not sound like a good idea since you do not want to escalate things." 
    
    "You lay your other hand on your concealed revolver just in case."

    "As you head further down the stairs, a giant iron statue appears."
    
    "Lively, he begins explaining all the intricate details about the artwork he is working on."
    
    "Undoubtedly the smell of iron came from the body odor released as he was touching the statue during the creation of the art."
    
    "He kindly invites you to join his art project, in which you politely decline after serious reconsideration."

    jump epilogue
    
label epilogue:
    if shoot:
        "Despite his admission of his mistakes, you shot him in cold blood. Maybe you have the serial killer blood in you as well?"

    else:
        " Perhaps he won’t make a very good average joe since he has a giant fucking statue in his basement. However it’s clear that he really is a nice guy who loves his art. Just imagine if you accidently shot him after mistaking for a serial killer!"

    # This ends the game.
    "THE END"

    return
