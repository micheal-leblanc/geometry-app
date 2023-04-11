import math
import turtle

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
            print("In the rectangle")
            return True
        else:
            print ("Outside the rectangle")
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

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot()
