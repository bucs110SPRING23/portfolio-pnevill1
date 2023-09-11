import turtle

num_sides = input("How many sides would you like?:")
num_sides = int(num_sides)

length_sides = input("How long would you like your sides?:")
length_sides = int(length_sides)

internal_angle = 360/num_sides

window = turtle.Screen()

my_turtle_obj = turtle.Turtle()
my_turtle_obj.color("orange")

for i in range(num_sides):
    my_turtle_obj.forward(length_sides)
    my_turtle_obj.left(internal_angle)

window.exitonclick()