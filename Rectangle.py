from Point import Point
import turtle

class Rectangle:
    # "What the class is DEFINED by"
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    '''Add a class that calculates the area
    of the rectangle
    '''

    def area(self):
        """dont need point1/point2
        because its defined by rectangle class
        already and can be called anytime"""

        return ((self.point2.x - self.point1.x) * \
                (self.point2.y - self.point1.y))
    
class GraphicalRectangle(Rectangle):
    
    def draw(self,canvas):
        
        # Pen off canvas
        canvas.penup()

        # Goes to entered coordinate
        canvas.goto(self.point1.x, self.point1.y)

        # Pen on canvas
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

        turtle.done()

