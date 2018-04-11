# Chris Scene Images
image img_chris_1 = "chris/chris_1.png"
image img_chris_2 = "chris/chris_2.png"
image img_chris_3 = "chris/chris_3.png"
image img_chris_4 = "chris/chris_4.png"
image img_chris_5 = "chris/chris_5.png"
image img_chris_6 = "chris/chris_6.png"
image img_chris_7 = "chris/chris_7.png"
image img_chris_8 = "chris/chris_8.png"
image img_chris_9 = "chris/chris_9.png"
image img_chris_10 = "chris/chris_10.png"
image img_chris_11 = "chris/chris_11.png"

# Mock images
image img_chris_mock_1 = "chris/mock/mock_1.png"
image img_chris_mock_2 = "chris/mock/mock_2.png"
image img_chris_mock_3 = "chris/mock/mock_3.png"
image img_chris_mock_4 = "chris/mock/mock_4.png"
image img_chris_mock_5 = "chris/mock/mock_5.png"
image img_chris_mock_6 = "chris/mock/mock_6.png"
image img_chris_mock_7 = "chris/mock/mock_7.png"
image img_chris_mock_8 = "chris/mock/mock_8.png"
image img_chris_mock_9 = "chris/mock/mock_9.png"
image img_chris_mock_10 = "chris/mock/mock_10.png"
image img_chris_mock_11 = "chris/mock/mock_11.png"
image img_chris_mock_12 = "chris/mock/mock_12.png"
image img_chris_mock_13 = "chris/mock/mock_13.png"
image img_chris_mock_14 = "chris/mock/mock_14.png"
image img_chris_mock_15 = "chris/mock/mock_15.png"

# Mock-shoot images
image img_chris_mock_shoot_1 = "chris/mock/shoot/shoot_1.png"
image img_chris_mock_shoot_2 = "chris/mock/shoot/shoot_2.png"
image img_chris_mock_shoot_3 = "chris/mock/shoot/shoot_3.png"
image img_chris_mock_shoot_4 = "chris/mock/shoot/shoot_4.png"
image img_chris_mock_shoot_5 = "chris/mock/shoot/shoot_5.png"
image img_chris_mock_shoot_6 = "chris/mock/shoot/shoot_6.png"
image img_chris_mock_shoot_7 = "chris/mock/shoot/shoot_7.png"
image img_chris_mock_shoot_end = "chris/mock/shoot/shoot_end.png"

# Mock-not_shoot images
image img_chris_mock_not_shoot_1 = "chris/mock/not_shoot/not_shoot_1.png"
image img_chris_mock_not_shoot_2 = "chris/mock/not_shoot/not_shoot_2.png"
image img_chris_mock_not_shoot_3 = "chris/mock/not_shoot/not_shoot_3.png"
image img_chris_mock_not_shoot_end = "chris/mock/not_shoot/not_shoot_end.png"

# Serious images
image img_chris_serious_1 = "chris/serious/serious_1.png"
image img_chris_serious_2 = "chris/serious/serious_2.png"
image img_chris_serious_3 = "chris/serious/serious_3.png"
image img_chris_serious_4 = "chris/serious/serious_4.png"
image img_chris_serious_5 = "chris/serious/serious_5.png"
image img_chris_serious_6 = "chris/serious/serious_6.png"
image img_chris_serious_7 = "chris/serious/serious_7.png"
image img_chris_serious_8 = "chris/serious/serious_8.png"
image img_chris_serious_9 = "chris/serious/serious_9.png"
image img_chris_serious_end = "chris/serious/serious_end.png"

label scene_chris_start:

    scene

    # Story flags
    $ shoot = False

    scene img_chris_1 onlayer bg

    "You arrive at his house door – a thick wooden door with a hint of rot."
    
    "You vaguely smell the metallic iron smell from outside."

    scene img_chris_2 onlayer bg
    
    "Such smell is common when iron in blood react with oils in your skins, resulting in release of molecules that we are sensitive to and identify as ‘metallic’ smell."

    scene img_chris_3 onlayer bg
    
    "Therefore, he either has a giant iron statue in his house that he regularly touches or he might be a serial killer."

    scene img_chris_4 onlayer bg

    "You knock on the door and to your surprise, within milliseconds, Chris opens the door as if he was waiting for your arrival right behind the door."

    chris "Hi Anna! Please come in! Nice to meet you."

    scene img_chris_5 onlayer bg

    "Briefly setting your suspicion aside for a moment, you greet him back with a pleasant smile."

    anna "Thanks! Nice to meet you too!"

    scene img_chris_6 onlayer bg

    "You enter his apartment, only to be greeted by even stronger scents of iron." 
    
    "You have major glances at your surroundings only to find a very ordinary apartment. No source of iron in sight."

    scene img_chris_7 onlayer bg
    
    "You conclude that the smell must be coming from the basement."

    scene img_chris_8 onlayer bg

    "You catch a glimpse of a sketchbook lying on the ground."

    scene img_chris_9 onlayer bg

    anna "I didn’t know you draw. May I examine them?"

    scene img_chris_10 onlayer bg

    chris "Of course!"

    scene img_chris_11 onlayer bg

    "You find many drawings of women’s clothes and naked women, some appear to be depicted to be dead." 

menu sketchbook:
    "Impulsively, you respond loudly in the following manner:"
    
    "Half-jokingly and with a hint of mockery":
        scene img_chris_mock_1 onlayer bg

        "This is a little creepy to be honest. I can’t even imagine what is hiding in your basement."

        jump sketchbook_mock

    "Serious":
        scene img_chris_serious_1 onlayer bg

        "Nice drawing. But I have to ask, what’s this smell of iron by the way?"

        jump sketchbook_serious

    "Nice cop":
        "They’re really nice! I’d love to see some more later!"

        jump sketchbook_nice

label sketchbook_mock:
    scene img_chris_mock_2 onlayer bg

    "Chris seems slightly rattled."

    scene img_chris_mock_3 onlayer bg
    
    chris "I disagree. You can’t judge me based on my personal taste in art."

    scene img_chris_mock_4 onlayer bg

    anna "Apologies. I meant it as a joke. But you gotta admit it is a bit unusual."

    scene img_chris_mock_5 onlayer bg

    "He suddenly pulls your hand, and thus your body forward violently."

    scene img_chris_mock_6 onlayer bg
    
    "You don’t know whether it is the result of him slipping or trying to intentionally harm you."

    scene img_chris_mock_7 onlayer bg
    
    "Your muscle memory from years of training makes you pull out your revolver and blindly shoot this man twice."

    scene img_chris_mock_8 onlayer bg
    
    "One grazes his arm, but the other one is more fatal. It has hit his stomach, penetrating his internal organs."

    scene img_chris_mock_9 onlayer bg

    chris "I just… wanted to show … my art.. Fuck you… What are you? A serial killer?.."

    scene img_chris_mock_10 onlayer bg

    "You stand there awkwardly. You look around only to find a giant metal statue standing before you, without a doubt, that is the source of the metallic smell."

    scene img_chris_mock_11 onlayer bg
    
    "You fucked up big time."

    scene img_chris_mock_12 onlayer bg

    anna "It’s your own damn fault! Why did you pull me so violently?"

    scene img_chris_mock_13 onlayer bg

    chris "I had no idea it was violent.. I just wanted to surprise you (he coughs repeatedly) I’m going to sue you until you are bankrupt! My daddy is a millionaire! You’ll regret this!"

    scene img_chris_mock_14 onlayer bg

    "You definitely don’t have the financial stability to risk it. Finishing him off might be a good idea." 

    scene img_chris_mock_15 onlayer bg
    
    "Should you shoot this man one more time? You are confident in your ability to lie about the incident to get away with minor punishment."

menu shoot:
    "What do you do?"

    "Yes. This guy is an ass.":
        $ shoot = True

        scene img_chris_mock_shoot_1 onlayer bg

        "His insults do not sit right with your ego. You are a big deal."

        scene img_chris_mock_shoot_2 onlayer bg

        anna "Who are you talking to right now? I am the detective responsible for arrests of over 100 big time criminals." 
        
        scene img_chris_mock_shoot_3 onlayer bg

        anna "I was handpicked by the commissioner to find the biggest serial killer in the history. You can’t threaten me, I am the threat!"

        scene img_chris_mock_shoot_4 onlayer bg

        "You plant a bullet deep into his heart. He squeals for 5 seconds, and then he was gone. You notice that your audio recording has been streaming into the cloud by accident."

        scene img_chris_mock_shoot_5 onlayer bg

        "Your life is now really fucked big time."

        scene img_chris_mock_shoot_6 onlayer bg

        jump scene_chris_mock_end

    "No! Killing is wrong!":

        scene img_chris_mock_not_shoot_1 onlayer bg

        "You quickly radio your headquarter for ambulance support. Your life will be slightly difficult from now on."

        scene img_chris_mock_not_shoot_2 onlayer bg
        
        "But at least you did the right thing."

        jump scene_chris_mock_end


label sketchbook_serious:
    scene img_chris_serious_2 onlayer bg

    "Chris looks composed, as if he’d expected it."

    scene img_chris_serious_3 onlayer bg

    chris "I’m not sure if I’m comfortable with you enough to show you right now."

    scene img_chris_serious_4 onlayer bg

    "As you head further down the stairs, a giant iron statue appears." 

    scene img_chris_serious_5 onlayer bg
    
    "He kindly but seriously explain how he is creating it for an art show. All mystery has been solved and it’s clear that the smell came from this big ass iron statue."

    scene img_chris_serious_6 onlayer bg

    chris "This is the source of the smell. I hope you didn’t think I was a serial killer of something! Hahaha"

    scene img_chris_serious_7 onlayer bg

    anna "Of course not! haha. It really is a beautiful piece of art work."

    scene img_chris_serious_8 onlayer bg

    "You make something up about you having to leave immediately. You both say farewell."

    jump scene_chris_serious_end

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

    jump scene_chris_end
    
label scene_chris_mock_end:
    if shoot:
        scene img_chris_mock_shoot_7 onlayer bg

        "Despite his admission of his mistakes, you shot him in cold blood. Maybe you have the serial killer blood in you as well?"

        scene img_chris_mock_shoot_end onlayer bg

    else:
        scene img_chris_mock_not_shoot_3 onlayer bg

        " Perhaps he won’t make a very good average joe since he has a giant fucking statue in his basement. However it’s clear that he really is a nice guy who loves his art. Just imagine if you accidently shot him after mistaking for a serial killer!"

        scene img_chris_mock_not_shoot_end onlayer bg
        
    jump scene_chris_end

label scene_chris_serious_end:
    scene img_chris_serious_end onlayer bg

    jump scene_chris_end

label scene_chris_end:

    "THE END"

    # This ends the game.
    return
