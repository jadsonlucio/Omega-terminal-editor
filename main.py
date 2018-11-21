import sys
import curses
from pyterminal.editor import Editor

if __name__ == "__main__":
    args = sys.argv
    file_path = None
    if len(args) == 2:
        file_path = args[1]

    print(file_path)
    editor = Editor()
    editor._create_screen(file_path = file_path)
    editor.run()
