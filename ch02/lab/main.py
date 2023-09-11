import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here

michelangelo.speed(1) # I changed the turtles' speed to make it easier to see what's happening
leonardo.speed(1)

# Race 1
michelangelo.forward(random.randrange(101))
leonardo.forward(random.randrange(101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Race 2  
random_turtle_amount = range(random.randrange(11)) # Had to use the 'range' function to actually get a list with a random size 1-10 for the 'for' loop to draw from with 'i'
for i in random_turtle_amount:
    michelangelo.forward(random.randrange(11))
    leonardo.forward(random.randrange(11))

window.exitonclick()
# PART B - complete part B here
pygame.init()

window = pygame.display.set_mode()
window.fill("white")
pygame.display.flip()
pygame.time.wait(500)

def draw_polygon(num_sides, side_length, color):
    
    # Function that can be called, given the number of sides, length of sides, and color of object
    # Can be used to draw shapes with these parameters, and then resets the screen to white and the 'points' list to empty so it can be used again to make a new shape

    points = []
    xpos = 1000
    ypos = 500

    for i in range(num_sides):
     angle = 360/num_sides
     radians = math.radians(angle * i)
     x = xpos + side_length * math.cos(radians)
     y = ypos + side_length * math.sin(radians)
     points.append([x, y])

    pygame.draw.polygon(window, color, points, 5)
    pygame.display.flip()
    pygame.time.wait(1000)

    window.fill("white")
    pygame.display.flip()
    pygame.time.wait(1000)

draw_polygon(3, 100, "green") #Triangle
draw_polygon(4, 100, "blue") #Square
draw_polygon(6, 100, "black") #Hexagon
draw_polygon(20, 100, "purple") #Icosagon
draw_polygon(100, 100, "gray") #Hectagon
draw_polygon(360, 100, "orange") #Circle