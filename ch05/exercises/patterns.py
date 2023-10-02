def star_pyramid():
    num_rows = int(input("How many rows?:"))
    for x in range(num_rows):
        star_str = "*" * (x+1)
        print(star_str)

star_pyramid()

def rstar_pyramid():
    num_rows = int(input("How many rows?:"))
    for x in range(num_rows):
        star_str = "*" * (num_rows-x)
        print(star_str)

rstar_pyramid()