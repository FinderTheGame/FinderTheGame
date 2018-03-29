# Characters
define anna = Character("Anna")
define chris = Character("Chris")
define braden = Character("Braden")

# Character Images
image img_anna = im.Flip("anna.png", True)
image img_chris = "chris.png"
image img_braden = im.Flip("braden.png", True)

# Character Images positions
transform anna_pos:
    xpos 450
    ypos 200
    zoom 0.8

transform chris_pos:
    xpos 800
    ypos 160
    zoom 0.8

transform braden_pos:
    xpos 800
    ypos 160
    zoom 0.8

# Backgrounds
image room1 = "room_1.png"
image room2 = "room_2.png"

label start:
    "You wake up groggy, your head is pounding and you feel like you have a knot in your stomach."
    
    "It’s been three and a half months with no leads on the killer. The stress of it makes you feel sick."
    
    "Three and a half months, three bodies so far, will there be a fourth?"

    "All you know is you have to act, there has to be something you can do."
    
    "You’re lead detective after all. Although never before has there been such a killer in your city. You have to find them."

    "You get to your computer, pouring over the case files for what seems like the thousandth time."
    
    "What do you know? You and your team has concluded the killer is male, mid to late thirties, and is likely to have some sort of educational background."

    "As you look at the photos of the victims, the girls, some nagging feeling stirs in you but you don’t know why."
    
    "They could have all been sisters, they bare a lot in common. That’s when you realize what it is that bothers you, they're like you."

    "All around the same age. All high-power career driven women, hell they even kind of look like you.  It doesn’t sit well, you feel especially sickened."

    "Another thought occurs to you, all victims were active on the popular dating app Finder."
    
    "Could the killer have been using it to narrow in on his victims? It’s unconventional but nothing else has worked."
    
    "You grab your phone and make a profile. Maybe you’re just his type."
  
# The game starts here.
menu scene_select:  
    "Select a scene:"

    "Chris":
        jump scene_chris_start

    "Braden":
        jump scene_braden_start        
