from pybricks.parameters import Button
from pybricks.media.ev3dev import Font
from pybricks.tools import wait

class TextMenu:
    def __init__(self, ev3_instance, options_array, font_size=12):
        """
        初始化自訂菜單。
        options_array: 選項文字陣列
        font_size: 字型大小，若外部未傳入則預設為 12 像素
        """
        self.ev3 = ev3_instance
        self.options = options_array
        self.current_index = 0
        self.total_options = len(options_array)
        
        # 核心優化：動態套用外部傳入（或預設）的點陣字型大小
        try:
            self.menu_font = Font(family='courier', size=font_size)
        except Exception:
            self.menu_font = Font(size=font_size)

        self.ev3.screen.set_font(self.menu_font)

    def draw(self):
        """
        清空螢幕並使用設定好的字型繪製帶有 > 游標的字符界面
        """
        self.ev3.screen.clear()
        self.ev3.screen.print("--- EV3 SELECT MENU ---")
        self.ev3.screen.print("^/v to select, [] to ok")
        self.ev3.screen.print("-----------------------")
        
        for i in range(self.total_options):
            if i == self.current_index:
                # 選中的項目：加上 > 前綴
                self.ev3.screen.print("> [{}] {}".format(i + 1, self.options[i]))
            else:
                # 未選中的項目：保持空白對齊
                self.ev3.screen.print("  [{}] {}".format(i + 1, self.options[i]))

    def get_choice(self):
        """
        監聽實體按鍵。
        返回選中的索引值 (int)，未確認則返回 None
        """
        pressed_keys = self.ev3.buttons.pressed()

        if Button.UP in pressed_keys:
            self.current_index = (self.current_index - 1) % self.total_options
            self.draw()
            wait(200)  # 防彈跳連點延遲

        elif Button.DOWN in pressed_keys:
            self.current_index = (self.current_index + 1) % self.total_options
            self.draw()
            wait(200)

        elif Button.CENTER in pressed_keys:
            wait(200)
            return self.current_index

        wait(50)
        return None

