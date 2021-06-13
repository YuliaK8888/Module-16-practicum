class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def rectangle_items(self):    
        return self.x, self.y, self.height, self.height
newRectangle = Rectangle(5, 10, 15, 20)        
print(newRectangle.rectangle_items())       