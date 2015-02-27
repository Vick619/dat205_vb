from graphics import *
import random
import math

datafile = open("data.txt", 'r')
data = math.floor(1).datafile
window = GraphWin("Visualisation", 600, 600)

background = Rectangle(Point(0, 0), Point(601, 601))
background.setFill(color_rgb(255, 255, 255))
background.draw(window)

for draw in data:
    ball = Circle(Point(data, data), 60)
    ball.setFill(color_rgb(100, 100, 100))
    ball.draw(window)

window.getMouse()