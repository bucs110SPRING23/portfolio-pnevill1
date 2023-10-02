import turtle

num_sides = int(input("How many sides would you like?:"))
side_length = int(input("How long would you like your sides to be?:"))

def draw_eq_shape(myturt, num_sides, side_length):

    internal_angle = 360/num_sides

    window = turtle.Screen()

    for i in range(num_sides):
        myturt.forward(side_length)
        myturt.left(internal_angle)

    window.exitonclick()

myturt = turtle.Turtle()
myturt.color("green")
myturt.shape("turtle")

draw_eq_shape(myturt, num_sides, side_length)