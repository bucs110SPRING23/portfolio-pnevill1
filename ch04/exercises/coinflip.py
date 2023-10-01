import turtle
import random

window = turtle.Screen() 
window.bgcolor('lightblue')

myturt = turtle.Turtle() 
myturt.color('orange')
myturt.shape('turtle')

myturt.goto(0, 0)

for x in range(50):
    coin = random.randrange(2)
    myturt_pos = myturt.position()
    myturt_x = myturt_pos[0]
    myturt_y = myturt_pos[1]
    print(int(myturt_x), int(myturt_y))
    if myturt_x > 400:
        break
    if myturt_y > 400:
        break
    if myturt_x < -400:
        break
    if myturt_y < -400:
        break
    if coin == 0:
        angle = myturt.heading()
        myturt.setheading(angle-90)
    if coin == 1:
        angle = myturt.heading()
        myturt.setheading(angle+90)
    myturt.forward(100)