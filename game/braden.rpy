label scene_braden_start:
    scene house_front onlayer bg

    show img_anna at anna_pos

    "You have no problems finding Braden’s house, you arrive on time and pull up into the driveway."
    
    "Immediately you notice the door opens, he’s there waiting with a warm smile and a friendly wave." 

    show img_braden at braden_pos
    
    "You weren’t expecting that." 
    
    "He leaves the house and starts to walk towards your car."

menu greeting:
    "What will you do before he reaches your car?"

    "Update your partner":
        "You text the address to your partner back at the police station."
        jump after_greeting

    "Discretely arm yourself":
        "You grabbed your pistol from your car and discretely put it into your purse."
        jump after_greeting

    "Turn on tape recorder":
        "You switched on your tape recorder."
        jump after_greeting

label after_greeting:
    "Braden smiles as you open the car door."

    braden "Hi Anna, nice to meet you! I’m glad you didn’t have any trouble finding the place I know I’m a bit out of the way."

    anna "It was no problem at all. The property looks gorgeous."

    braden "It’s been in the family for generations, I’ll have to give you the grand tour later. For now let me show you around the house."

    "You follow Braden into the house, it’s neat clean and orderly." 

    scene room1 onlayer bg
    
    "He takes your jacket for you, but you keep your purse held tight. When you get to the living room Braden announces."

    braden "I promised you dinner, but how about a drink first. What can I get you?"

menu dinner_choice:
    "What would you like to drink?"

    "Tea":
          anna "I’d love some tea."
          jump after_dinner_choice

    "Wine":
          anna "If you have any wine that’d be nice."
          jump after_dinner_choice

    "Water":
          anna "Just some water please."
          jump after_dinner_choice

label after_dinner_choice:
    braden "Of course,” He replies. “Just make yourself comfortable and I’ll be right back."

    "He smiles and walks off to the kitchen. To your estimation you’ll have about two minutes before he is back."
    
    "Enough time to take a closer look at one of his personal effects while he’s not watching."
    
    "Thanks to your years of investigating three items in particular stand out."

menu investigate_choice:
    "Which would you investigate?"

    "Old framed photograph":
        "It’s shabbiness distinguishes it from the rest of modern décor."
        jump photograph

    "Papers":
        "A messy bundle of folded papers on the desk, wrapped together with an elastic." 
        
        "The disorganized bundle is a stark contrast to neatly ordered room."

        jump papers

    "Cat figurines":
        "Three toy cat figurines lined up on the bookshelf. They seem oddly childish compared to the rest of the refined surroundings."

        jump figurines

label photograph:
    jump scene_braden_end

label papers:
    jump scene_braden_end

label figurines:
    jump scene_braden_end


label scene_braden_end:
    "To be continued.."
    
    # "THE END"
