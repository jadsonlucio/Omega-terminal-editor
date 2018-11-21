import os
import curses
from .terminal.screen  import Screen
from .terminal.events import Event
from .constants import DIRECTIONAL_KEYS

class Editor():
    def __init__(self):
        self.running = False
        self.screens = []
        self.events_queue = [] 
        self.window = curses.initscr()
        self.window_max_size = self.window.getmaxyx()
        self.active_screen = None
    
    def run(self):
        self.running = True
        self.mainloop()

    def mainloop(self):
        while self.running:
            self.window.clear()
            self.window.addstr(0, 0, self.active_screen.get_text(), curses.COLOR_WHITE)
            self.window.move(*self.active_screen.abs_mouse_pos)
            self.window.refresh()

            k = self.window.getch()
            if k == ord('q'):
                self.running = False
                self.quit()
                self.events_queue.append(Event("exit", True))
            if k in DIRECTIONAL_KEYS:
                self.events_queue.append(Event("cursor_move", side = DIRECTIONAL_KEYS[k]))

            self.events_queue.append(Event("key_pressed", key_code = k))
            self._treat_events()

    def quit(self):
        curses.endwin()

    def _treat_events(self):
        for event in self.events_queue:
            if event.global_event:
                for screen in self.screens:
                    screen.event_call(event)
            else:
                self.active_screen.event_call(event)


        self.events_queue = []

    def _create_screen(self, screen_width = None, screen_height = None, posX = 0, 
                                                     posY = 0, file_path = None):
        screen_width = self.window_max_size[0] if not screen_width else screen_width
        screen_height = self.window_max_size[1] if not screen_height else screen_height
        screen = Screen("New file",screen_width, screen_height, posX, posY, file_path)

        self.active_screen = screen
        self.screens.append(screen)

    def _destroy_screen(self, index = 0):
        screen = self.screens.pop(index = index)
        if screen == self.active_screen:
            self.active_screen = self.screens[0]

