class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def rectangle_area(self):
        return self.width*self.height
newRectangle = Rectangle(5,10)
print("Area: " + str(newRectangle.rectangle_area()))
