import sys
import curses
from omega.editor import Editor
from omega.exceptions.exceptions import traceback

if __name__ == "__main__":
    args = sys.argv
    file_path = None
    if len(args) == 2:
        file_path = args[1]

    editor = Editor()
    editor._create_screen(file_path = file_path)
    try:
        editor.run()
    except:
        curses.endwin()
        print(traceback.format_exc())