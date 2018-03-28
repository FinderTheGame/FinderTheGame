# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define anna = Character("Anna")

image test = "Test.jpg"
image img_anna neutral = "anna.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene test

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show img_anna

    # These display lines of dialogue.

    anna "You've created a new Ren'Py game."

    anna "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
