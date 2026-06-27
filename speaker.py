#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from lib.menulib import TextMenu  # Import your custom menu library

# Initialize EV3
ev3 = EV3Brick()

# Audio settings
ev3.speaker.set_volume(80)
ev3.speaker.set_speech_options(language="en", voice="f2", speed=155)

# 1. Define your display options array
menu_titles = [
    "Weather Status",
    "Work Status",
    "Weekend Alert",
    "Insult User",
    "SB wife"
]

# 2. Define corresponding audio strings (synchronized by array index)
speech_texts = [
    "The weather is so nice today.",
    "It's a work day today.",
    "Finally it's weekend.",
    "Fuck you! You dummy ass.",
    "Wang Jing daa shaa bee! Yee zao shun jiu gao woh!"
]

# Initialize the menu with the options array
menu = TextMenu(ev3, menu_titles)
menu.draw()  # Initial draw

# Main Interaction Loop
while True:
    # Continuously check for user choice
    choice_index = menu.get_choice()
    
    # If the user selected an item (CENTER pressed)
    if choice_index is not None:
        ev3.screen.print("\n... Speaking ...")
        
        # Trigger text-to-speech using the synchronized speech index
        ev3.speaker.say(speech_texts[choice_index])
        
        # Redraw menu interface after speech completes
        menu.draw()

