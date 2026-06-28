#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font
from lib.menulib import TextMenu  # Import your custom menu library

# Initialize EV3
ev3 = EV3Brick()

# Audio settings
ev3.speaker.set_volume(80)
ev3.speaker.set_speech_options(language="en", voice="f2", speed=155)
text_font = Font(family='courier', size=12)
ev3.screen.set_font(text_font)

menu_title = "Speaker Test"
# 1. Define your display options array
menu_items = [
    "Weather Status",
    "Work Status",
    "Weekend Alert",
    "Insult User",
    "SB wife"
]

# Initialize the menu with the options array
menu = TextMenu(ev3, menu_title, rows=5, items=menu_items)

# 2. Define corresponding audio strings (synchronized by array index)
speech_texts = [
    "The weather is so nice today.",
    "It's a work day today.",
    "Finally it will be weekend tomorrow.",
    "You dummy ass!",
    "Wang Jing is so beautiful."
]

# Main Interaction Loop
while True:
    # Continuously check for user choice
    choice_index, _ = menu.run()
    
    # If the user selected an item (CENTER pressed)
    if choice_index == -1:
        ev3.screen.clear()
        ev3.screen.print("Exiting Menu Context")
        wait(1000)
        break

    # Trigger text-to-speech using the synchronized speech index
    ev3.speaker.say(speech_texts[choice_index])
        
