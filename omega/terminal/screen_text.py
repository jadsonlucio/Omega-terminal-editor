import os

class Text():
    def __init__(self, posX = 0, posY = 0,file_path = None):
        self.posX = posX
        self.posY = posY

        self._value = ""
        self._lines = []
        self._screen_text = None
        self.file = None

        self.file_path = file_path

    def save(self, close = False):
        self.file.write(self._value)
        if close:
            self.file.close()

    def load(self):
        if os.path.isfile(self.file_path):
            self.file = open(self.file_path, 'r+')
        else:
            self.file = open(self.file_path, 'w+')

        self._value = "".join(self.file.readlines())
        self._lines = self.file.readlines()

    def update(self):
        self._lines = [line+"\n" for line in self.text.split("\n")]

    def get_screen_text(self, screen_width, screen_height):
        text = ""
        array_linhas = self._lines[self.posY:self.posY + screen_width]
        for linha in array_linhas:
            if self.posX < len(linha):
                if (len(linha) - self.posX) > screen_height:
                    text = text + linha[self.posX : self.posX + screen_height] + "\n"
                else:
                    text = text + linha[self.posX:]
            else:
                text = text + "\n"

        return text
    
    def set_screen_text(self, screen_width, screen_height):
        self._screen_text = self.get_screen_text(screen_width, screen_height)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        self._file_path = file_path
        if file_path:
            self.load()

    def __get__(self, instance, owner):
        return self._screen_text
    

  
if __name__ == "__main__":
    obj = Text(file_path = "test.txt")
    print(obj._get_screen_text(20,50))
