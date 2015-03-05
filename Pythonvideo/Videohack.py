from graphics import *
import random
import math

colour = 0
width = 0
move= 0
moveback = 600
bordercolour = 255
bordercolour1 = 0
datafile = open("data.txt", 'r')
data = datafile.readlines()
window = GraphWin("Visualisation", 600, 600)

background = Rectangle(Point(0, 0), Point(601, 601))
background.setFill(color_rgb(255, 255, 255))
background.draw(window)

for stringvalue in data:
    colour+=7
    width+=0.1
    move+=18
    moveback-=18
    bordercolour-=7
    bordercolour1+=7
    time.sleep(1)
    intvalue = math.floor(float(stringvalue))
    ball = Circle(Point(moveback, 300), intvalue)
    ball.setOutline(color_rgb(bordercolour, bordercolour, bordercolour))
    ball.setWidth(width)
    ball.setFill(color_rgb(colour, colour, colour))
    ball.draw(window)
    ball = Circle(Point(move, 150), intvalue)
    ball.setOutline(color_rgb(bordercolour1, bordercolour1, bordercolour1))
    ball.setWidth(width)
    ball.setFill(color_rgb(colour, colour, colour))
    ball.draw(window)
    ball = Circle(Point(move, 450), intvalue)
    ball.setOutline(color_rgb(bordercolour1, bordercolour1, bordercolour1))
    ball.setWidth(width)
    ball.setFill(color_rgb(colour, colour, colour))
    ball.draw(window)

window.getMouse()