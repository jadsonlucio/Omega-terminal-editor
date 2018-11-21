import curses
from .screen_text import Text
from .events import Events

class Screen(Events):
    def __init__(self, title, width, height, posX, posY, file_path = None):
        self.title = title
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.cursorX = 0
        self.cursorY = 0 
        self.text = Text(file_path = file_path)
        self.text.set_screen_text(self.width, self.height)

    def update(self):
        pass

    def get_text(self):
        return self.text._value
    
    def key_pressed(self, event):
        self.text._value = self.text._value + chr(event.key_code)

    def cursor_move(self, event):
        side = event.side
        self.cursorX = self.cursorX + side[0]
        self.cursorY = self.cursorY + side[1]
    
    def exit(self, event):
        self.text.save(close = True)

    @property
    def abs_mouse_pos(self):
        return self.cursorX + self.posX ,self.cursorY + self.posY

    def rel_mouse_pos(self):
        return self.cursorX, self.cursorY
