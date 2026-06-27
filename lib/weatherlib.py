import os

class WeatherFetcher:
    def __init__(self, city_name):
        """
        初始化城市名称
        """
        self.city = city_name
        
        # API 1 (语音专用)：%C(状态) %t(温度) %h(湿度) %w(风速)
        self.curl_speech = 'curl --silent -k -L --max-time 4 "http://wttr.in/{}?format=%C,+%t,+humidity+%h,+wind+%w"'.format(self.city)
        
        # API 2 (屏幕专用)：?0 代表只显示当前天气表格，T 代表无彩色控制符
        self.curl_screen = 'curl --silent -k -L --max-time 4 "http://wttr.in/{}?0&T"'.format(self.city)

    def get_weather_speech(self):
        """
        核心方法更名：專供主程序語音朗讀。
        返回您定制的可读数据字符串
        """
        try:
            with os.popen(self.curl_speech) as pipe:
                result = pipe.read().strip()
            
            # 防御性退守逻辑保持不变
            if not result or "404" in result or "Error" in result or "Unknown" in result:
                return "Cannot get weather data for {}".format(self.city)
                
            return result
        except Exception:
            return "Cannot get weather data for {}".format(self.city)

    def get_screen_weather(self):
        """
        API 2：专供 EV3 屏幕物理排版打印。
        返回 wttr.in/?0 的精简当前天气纯文本数据
        """
        try:
            with os.popen(self.curl_screen) as pipe:
                result = pipe.read() # 获取多行精简 ASCII 文本
                
            if not result or "404" in result or "Error" in result:
                return "Network Error"
            return result
        except Exception:
            return "Network Error"
