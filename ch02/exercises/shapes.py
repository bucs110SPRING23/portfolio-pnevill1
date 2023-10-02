import pygame
import math
pygame.init()

screen = pygame.display.set_mode()

pi = math.pi

screen.fill("white")
pygame.display.flip()

# Here I create rectancle shapes that define the arcs I use to overwrite parts of the circles to make it look more like the assigned picture
my_pygame_rect = pygame.Rect(900, 400, 200, 200)
my_pygame_rect_1 = pygame.Rect(880, 580, 240, 240)

# Here I create the circles that make up the snowman
pygame.draw.circle(screen, "gray", [1000, 500], 100, 5)
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.circle(screen, "gray", [1000, 700], 120, 5)
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.circle(screen, "gray", [1000, 350], 80, 5)
pygame.display.flip()
pygame.time.wait(1000)

# Here I draw arcs that cover parts of the circles to try and make them look more like a snowman
pygame.draw.arc(screen, "white", my_pygame_rect, pi/2.8, pi/1.55, 6)
pygame.display.flip()
pygame.time.wait(1000)

pygame.draw.arc(screen, "white", my_pygame_rect_1, pi/2.5, pi/1.65, 6)
pygame.display.flip()
pygame.time.wait(5000)