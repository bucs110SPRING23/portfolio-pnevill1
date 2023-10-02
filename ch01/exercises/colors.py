# Here I define my list of colors and state how many I have
my_color_list = ["red", "orange", "yellow", "green", "blue", "violet"]
print("I have", len(my_color_list), "colors in the rainbow. They are as follows:")

#Here I create a for loop which lists all of my colors
for x in my_color_list:
    print(x)
    if x == "violet":
        break