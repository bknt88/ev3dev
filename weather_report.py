#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from lib.menulib import TextMenu
from lib.weatherlib import WeatherFetcher

# 初始化 EV3 主机
ev3 = EV3Brick()

# 语音配置
ev3.speaker.set_volume(90)
ev3.speaker.set_speech_options(language="en", voice="f2", speed=160)

# 预设城市列表
cities_menu = ["Beijing", "Stockholm", "Changsha"]

# 初始化菜单并绘制
menu = TextMenu(ev3, cities_menu)
menu.draw()

while True:
    choice_index = menu.get_choice()
    
    if choice_index is not None:
        selected_city = cities_menu[choice_index]
        
        # 屏幕即时等待提示
        ev3.screen.clear()
        ev3.screen.print("Connecting IoT...\nFetching {}...".format(selected_city))
        
        # 实例化天气业务对象
        fetcher = WeatherFetcher(selected_city)
        
        # 核心调用：调用全新更名后的 get_weather_speech 方法
        screen_data = fetcher.get_screen_weather()       # 拿精简表格
        speech_string = fetcher.get_weather_speech()     # 核心更名處：拿定制可讀字串
        
        # 屏幕端高级局回显
        ev3.screen.clear()
        ev3.screen.print(screen_data) # 在 size=12 小字体下完整塞进屏幕
        
        # 完美对接：朗读定制的可读字串数据
        ev3.speaker.say(speech_string)
        
        while not ev3.buttons.pressed():
            wait(50)
            
        # 刷新返回主菜单
        menu.draw()

