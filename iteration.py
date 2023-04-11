from random import randint
import turtle
import math

# =============== Class Definitions =========================
class Point: 
    # __init__ "What the class is DEFINED by"
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """ 
        Takes in argument of rectangle object
        """
        if rectangle.point1.x < self.x < rectangle.point2.x and \
            rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
        
    def distance_from_point(self, point):
        """
        Returns the distance from current point to another point
        Argument should be a Point object
        """
        distance = math.sqrt((self.x - point.x) **2 + (self.y - point.y)**2)        
        print(f"Distance is: {distance}")
        return distance

class GraphicalUserPoint(Point):

    def draw(self, canvas, size = 5, color = 'red'):
        """Draws a point on the canvas"""
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
        turtle.done() #Locks out the drawing

class Rectangle:
    # "What the class is DEFINED by"
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    """Add a class that calculates the area
    of the rectangle
    """
    

    def area(self):
        """Calculates the area"""

        return ((self.point2.x - self.point1.x) * \
                (self.point2.y - self.point1.y))
    
class GraphicalRectangle(Rectangle):
    
    def draw(self,canvas):
        """Draws the rectangle. Takes canvas object as argument"""
        # Pen off canvas
        canvas.penup()

        # Goes to entered coordinate
        canvas.goto(self.point1.x, self.point1.y)

        # Pen on canvas
        canvas.pendown()

        # Draw the rectangle
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

# =================End Class Definitions=========================


# Create the random rectangle object
rectangle = GraphicalRectangle((Point(randint(0,400), randint(0,400))), \
                       Point(randint(10,400), randint(10,400)))

# User input
user_input = GraphicalUserPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess the area: "))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

#Print out the game result
print(f"Was your guessed point was inside the reactangle? {user_input.falls_in_rectangle(rectangle)}")
print(f"Your area guess was off by: {rectangle.area() - user_area}")

# Creates an instance of the canvas
mycanvas = turtle.Turtle()
rectangle.draw(mycanvas)
user_input.draw(mycanvas)