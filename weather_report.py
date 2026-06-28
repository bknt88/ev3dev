#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from lib.menulib import TextMenu
from lib.weatherlib import WeatherFetcher
from pybricks.media.ev3dev import Font
import sys

# 1. Initialize core hardware brick instance
ev3 = EV3Brick()

ev3.speaker.set_volume(90)
ev3.speaker.set_speech_options(language="en", voice="f2", speed=160)

# 2. Caller handles font setup completely
try:
    text_font = Font(family='courier', size=12)
except Exception:
    text_font = Font(size=12)

# Apply font scaling to the screen asset context globally
ev3.screen.set_font(text_font)

# 3. Define dataset layers for the menu instance
menu_title = "Realtime Weather"
cities = ["Stockholm", "Norrviken", "Malmo", "Uppsala", "Solna", "Göteborg", "Helenelund", "Beijing", "Changsha", "WuHhn", "Xian", "Shenzhen", "Shanghai", "Hainan", "Yangzhou", "Oslo", "Frankfurt", "Berlin", "Paris", "London", "Barcelona", "Newyork"]

# 4. Instantiate the decoupled text menu framework
menu = TextMenu(
    ev3=ev3,
    title=menu_title,
    rows=8,
    items=cities
)

def handle_selection(selected_city):
    """
    Processes the selection string. Instantiates the WeatherFetcher
    and handles data collection.
    """
    ev3.screen.clear()
    ev3.screen.print("Connecting...")
    ev3.screen.print("Fetching live data...")

    # Core Requirement: Instantiate engine with targeted location item
    fetcher = WeatherFetcher(selected_city)

    screen_data = fetcher.get_screen_weather()
    speech_string = fetcher.get_weather_speech()

    # Render clean output results to LCD canvas
    ev3.screen.clear()
    ev3.screen.print(screen_data)
    ev3.speaker.say(speech_string)

    while not ev3.buttons.pressed():
        wait(100)

# 5. Application Lifecycle Thread Loop
def main():
    while True:
        # Run menu state machine loops until confirmation actions occur
        index, item = menu.run()

        if index == -1:
            # Escape route selected (Button.LEFT pressed)
            ev3.screen.clear()
            ev3.screen.print("Exiting Menu Context")
            wait(1000)
            break
        else:
            # Route active string value to target fetcher method
            handle_selection(item)

if __name__ == "__main__":
    main()

