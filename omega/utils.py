class Rect():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
    
    def move(self, x ,y):
        self.x = self.x + x
        self.y = self.y + y