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

label start:
  
# The game starts here.
menu scene_select:
    "Select a scene:"

    "Chris":
        jump scene_chris_start

    "Other":
        "THE END" 
        
