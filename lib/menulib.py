from pybricks.parameters import Button
from pybricks.tools import wait


class TextMenu:
    """A simple text-based menu for the EV3 screen."""

    def __init__(self, ev3, title, rows, items):
        """
        Initialize a text menu.

        Args:
            ev3: EV3Brick instance.
            title: Menu title.
            rows: Maximum number of menu rows. Currently unused and
                  reserved for future scrolling support.
            items: List of menu item strings.
        """
        self.ev3 = ev3
        self.title = title
        self.rows = rows
        self.items = items
        self.selected = 0

    def _refresh(self):
        """Refresh the menu display."""

        self.ev3.screen.clear()

        self.ev3.screen.print(self.title)
        self.ev3.screen.print()

        start = self.selected // self.rows * self.rows
        end = start + self.rows
        if end > len(self.items):
            end = len(self.items)

        for index in range(start, end):
            prefix = ">" if index == self.selected else " "
            self.ev3.screen.print("{} {}".format(prefix, self.items[index]))

    def _wait_for_button_release(self):
        """Wait until all buttons have been released."""

        while self.ev3.buttons.pressed():
            wait(10)

    def run(self):
        """
        Display the menu.

        Returns:
            The selected menu item, or -1 if the menu is cancelled.
        """

        self._refresh()

        while True:
            buttons = self.ev3.buttons.pressed()

            if Button.UP in buttons:
                if self.selected > 0:
                    self.selected -= 1
                    self._refresh()

                self._wait_for_button_release()

            elif Button.DOWN in buttons:
                if self.selected < len(self.items) - 1:
                    self.selected += 1
                    self._refresh()

                self._wait_for_button_release()

            elif Button.LEFT in buttons:
                self._wait_for_button_release()
                return -1, None

            elif Button.CENTER in buttons or Button.RIGHT in buttons:
                self._wait_for_button_release()
                return self.selected, self.items[self.selected]

            wait(10)
