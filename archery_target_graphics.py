## An archery target consists of a central circle of yellow surrounded
## by concentric rings of red, blue, black, and white. Each ring has the
## same width, which is the same as the radius of the yellow circle. Write
## a function that draws such a target. HINT: Objects drawn later will appear
## on top of objects drawn earlier.

from graphics import *

def archery():
    win = GraphWin('Target')
    
    # Establishes a central point for all the circles
    center = Point(99, 99)
    
    # Creates the properties of the circles
    whitecirc = Circle(center, 90)
    blackcirc = Circle(center, 72)
    bluecirc = Circle(center, 54)
    redcirc = Circle(center, 36)
    yellowcirc = Circle(center, 18)
    whitecirc.setFill('white')
    blackcirc.setFill('black')
    bluecirc.setFill('blue')
    redcirc.setFill('red')
    yellowcirc.setFill('yellow')
    
    # Draws the circles
    whitecirc.draw(win)
    blackcirc.draw(win)
    bluecirc.draw(win)
    redcirc.draw(win)
    yellowcirc.draw(win)
