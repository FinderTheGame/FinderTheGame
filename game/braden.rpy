# Braden Scene images
image img_braden_1 = "braden/braden_1.png"
image img_braden_2 = "braden/braden_2.png"
image img_braden_3 = "braden/braden_3.png"
image img_braden_4 = "braden/braden_4.png"
image img_braden_5 = "braden/braden_5.png"
image img_braden_6 = "braden/braden_6.png"
image img_braden_7 = "braden/braden_7.png"
image img_braden_8 = "braden/braden_8.png"
image img_braden_9 = "braden/braden_9.png"
image img_braden_10 = "braden/braden_10.png"
image img_braden_11 = "braden/braden_11.png"
image img_braden_12 = "braden/braden_12.png"
image img_braden_13 = "braden/braden_13.png"
image img_braden_14 = "braden/braden_14.png"
image img_braden_15 = "braden/braden_15.png"
image img_braden_16 = "braden/braden_16.png"
image img_braden_17 = "braden/braden_17.png"
image img_braden_choice_1 = "braden/braden_choice_1.png"
image img_braden_choice_2 = "braden/braden_choice_2.png"

# Braden Update images
image img_braden_update_1 = "braden/update/update_1.png"

# Braden Gun images
image img_braden_gun_1 = "braden/gun/gun_1.png"

# Braden Recorder images
image img_braden_recorder_1 = "braden/recorder/recorder_1.png"

# Braden Photograph images
image img_braden_photograph_1 = "braden/photograph/photograph_1.png"
image img_braden_photograph_tbc = "braden/photograph/photograph_tbc.png"

# Braden Papers images
image img_braden_papers_1 = "braden/papers/papers_1.png"
image img_braden_papers_tbc = "braden/papers/papers_tbc.png"

# Braden Figurines images
image img_braden_figurines_1 = "braden/figurines/figurines_1.png"
image img_braden_figurines_tbc = "braden/figurines/figurines_tbc.png"

label scene_braden_start:
    scene

    scene img_braden_1 onlayer bg

    "You have no problems finding Braden’s house, you arrive on time and pull up into the driveway."

    scene img_braden_2 onlayer bg
    
    "Immediately you notice the door opens, he’s there waiting with a warm smile and a friendly wave." 

    scene img_braden_3 onlayer bg
    
    "You weren’t expecting that." 

    scene img_braden_4 onlayer bg
    
    "He leaves the house and starts to walk towards your car."

    scene img_braden_choice_1 onlayer bg

menu greeting:
    "What will you do before he reaches your car?"

    "Update your partner":
        scene img_braden_update_1 onlayer bg

        "You text the address to your partner back at the police station."

        jump after_greeting

    "Discretely arm yourself":
        scene img_braden_gun_1 onlayer bg

        "You grabbed your pistol from your car and discretely put it into your purse."

        jump after_greeting

    "Turn on tape recorder":
        scene img_braden_recorder_1 onlayer bg

        "You switched on your tape recorder."

        jump after_greeting

label after_greeting:
    scene img_braden_5 onlayer bg

    "Braden smiles as you open the car door."

    scene img_braden_6 onlayer bg

    braden "Hi Anna, nice to meet you! I’m glad you didn’t have any trouble finding the place I know I’m a bit out of the way."

    scene img_braden_7 onlayer bg

    anna "It was no problem at all. The property looks gorgeous."

    scene img_braden_8 onlayer bg

    braden "It’s been in the family for generations, I’ll have to give you the grand tour later. For now let me show you around the house."

    scene img_braden_9 onlayer bg

    "You follow Braden into the house, it’s neat clean and orderly." 

    scene img_braden_10 onlayer bg
    
    "He takes your jacket for you, but you keep your purse held tight. When you get to the living room Braden announces."

    scene img_braden_11 onlayer bg

    braden "I promised you dinner, but how about a drink first. What can I get you?"

    scene img_braden_12 onlayer bg

menu dinner_choice:
    "What would you like to drink?"

    "Tea":
        scene img_braden_13 onlayer bg

        anna "I’d love some tea."

        jump after_dinner_choice

    "Wine":
        scene img_braden_13 onlayer bg

        anna "If you have any wine that’d be nice."

        jump after_dinner_choice

    "Water":
        scene img_braden_13 onlayer bg

        anna "Just some water please."

        jump after_dinner_choice

label after_dinner_choice:
    scene img_braden_14 onlayer bg

    braden "Of course,” He replies. “Just make yourself comfortable and I’ll be right back."

    scene img_braden_15 onlayer bg

    "He smiles and walks off to the kitchen. To your estimation you’ll have about two minutes before he is back."

    scene img_braden_16 onlayer bg
    
    "Enough time to take a closer look at one of his personal effects while he’s not watching."

    scene img_braden_17 onlayer bg
    
    "Thanks to your years of investigating three items in particular stand out."

    scene img_braden_choice_2 onlayer bg

menu investigate_choice:
    "Which would you investigate?"

    "Old framed photograph":
        scene img_braden_photograph_1 onlayer bg

        "It’s shabbiness distinguishes it from the rest of modern décor."

        jump photograph

    "Papers":
        scene img_braden_papers_1 onlayer bg

        "A messy bundle of folded papers on the desk, wrapped together with an elastic." 
        
        "The disorganized bundle is a stark contrast to neatly ordered room."

        jump papers

    "Cat figurines":
        scene img_braden_figurines_1 onlayer bg

        "Three toy cat figurines lined up on the bookshelf. They seem oddly childish compared to the rest of the refined surroundings."

        jump figurines

label photograph:
    scene img_braden_photograph_tbc onlayer bg

    jump scene_braden_end

label papers:
    scene img_braden_papers_tbc onlayer bg

    jump scene_braden_end

label figurines:
    scene img_braden_figurines_tbc onlayer bg
    
    jump scene_braden_end


label scene_braden_end:
    "To be continued.."
    
    # "THE END"
