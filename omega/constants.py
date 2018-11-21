import curses

DIRECTIONAL_KEYS = {
    curses.KEY_DOWN : (1,0),
    curses.KEY_UP : (-1,0),
    curses.KEY_RIGHT : (0, 1),
    curses.KEY_LEFT : (0, -1)
}