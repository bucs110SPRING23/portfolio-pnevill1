import pygame
import math
import random

pygame.init()

# My screen length is 1920, and height is 1080 by default

window = pygame.display.set_mode([1080, 1080])
window.fill("cadetblue1")

# Setting up the dartboard
pygame.draw.circle(window, "brown1", (540, 540), 540)
pygame.draw.circle(window, "black", (540, 540), 540, 3)
pygame.draw.line(window, "black", (540, 1080), (540, 0))
pygame.draw.line(window, "black", (0, 540), (1080, 540))
pygame.display.flip()
pygame.time.wait(1000)

# This is the loop that draws darts in random locations and determines whether or not they're inside the dartboard
for x in range(10):
    rand_x = random.randrange(1081)
    rand_y = random.randrange(1081)
    distance_from_center = math.hypot(540-rand_x, 540-rand_y)
    is_in_circle = distance_from_center <= 540
    if is_in_circle:
        dart_color = "green"
    else:
        dart_color = "red"
    pygame.draw.circle(window, dart_color, (rand_x, rand_y), 20)
    pygame.draw.circle(window, "black", (rand_x, rand_y), 20, 2)
pygame.display.flip()
pygame.time.wait(2000)