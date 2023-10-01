import pygame
import math
import random

pygame.init()

# My screen is 1920 x 1080 by default so needed to change to 1080 x 1080
window = pygame.display.set_mode([1080, 1080])
window.fill("cadetblue1")

# Setting up the dartboard
pygame.draw.circle(window, "brown1", (540, 540), 540)
pygame.draw.circle(window, "black", (540, 540), 540, 3)
pygame.draw.line(window, "black", (540, 1080), (540, 0))
pygame.draw.line(window, "black", (0, 540), (1080, 540))

# Making the squares to place bets with
rect1 = pygame.rect.Rect(120, 400, 75, 75)
pygame.draw.rect(window, "green", rect1)
pygame.draw.rect(window, "black", rect1, 3)
rect2 = pygame.rect.Rect(960, 400, 75, 75)
pygame.draw.rect(window, "blue", rect2)
pygame.draw.rect(window, "black", rect2, 3)
pygame.display.flip()

# In this while loop I get a result for 'choice' based on which rectangle you click in, to signify your bet
made_choice = False

while not made_choice:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
              if int(event.pos[0]) <= 195 and int(event.pos[0]) >= 45 and int(event.pos[1]) <= 475 and int(event.pos[1]) >= 325:
                    choice = 0
                    pygame.draw.circle(window, "brown1", (540, 540), 540)
                    pygame.draw.circle(window, "black", (540, 540), 540, 3)
                    pygame.draw.line(window, "black", (540, 1080), (540, 0))
                    pygame.draw.line(window, "black", (0, 540), (1080, 540))
                    pygame.display.flip()
                    made_choice = True
            if int(event.pos[0]) <= 1035 and int(event.pos[0]) >= 885 and int(event.pos[1]) <= 475 and int(event.pos[1]) >= 325:
                    choice = 1
                    pygame.draw.circle(window, "brown1", (540, 540), 540)
                    pygame.draw.circle(window, "black", (540, 540), 540, 3)
                    pygame.draw.line(window, "black", (540, 1080), (540, 0))
                    pygame.draw.line(window, "black", (0, 540), (1080, 540))
                    pygame.display.flip()
                    made_choice = True

# After a bet is made, this loop goes through ten rounds for each 'player', tallies their scores, and draws their darts on screen
while made_choice:
    score_p1 = 0
    score_p2 = 0
    for x in range(10):
        rand_x_p1 = random.randrange(1081)
        rand_y_p1 = random.randrange(1081)
        distance_from_center = math.hypot(540-rand_x_p1, 540-rand_y_p1)
        is_in_circle = distance_from_center <= 540
        if is_in_circle:
            dart_color = "green"
            score_p1 = score_p1+1
        else:
            dart_color = "aquamarine3"
        pygame.draw.circle(window, dart_color, (rand_x_p1, rand_y_p1), 20)
        pygame.draw.circle(window, "black", (rand_x_p1, rand_y_p1), 20, 2)
        pygame.display.flip()
        pygame.time.wait(750)

        rand_x_p2 = random.randrange(1081)
        rand_y_p2 = random.randrange(1081)
        distance_from_center = math.hypot(540-rand_x_p2, 540-rand_y_p2)
        is_in_circle = distance_from_center <= 540
        if is_in_circle:
            dart_color = "blue"
            score_p2 = score_p2+1
        else:
            dart_color = "royalblue1"
        pygame.draw.circle(window, dart_color, (rand_x_p2, rand_y_p2), 20)
        pygame.draw.circle(window, "black", (rand_x_p2, rand_y_p2), 20, 2)
        pygame.display.flip()
        pygame.time.wait(750)
    break

# Here I use the scores and the choice of bet to decide what message will be at the end
if score_p1 > score_p2:
    if choice == 0:
        winner = "Player 1 Wins, You Win!"
    if choice == 1:
        winner = "Player 1 Wins, You Lose!"
elif score_p2 > score_p1:
    if choice == 0:
        winner = "Player 2 Wins, You Lose!"
    if choice == 1:
        winner = "Player 2 Wins, You Win!"
elif score_p1 == score_p2:
    winner = "      It's a Tie! You Lose!"
font = pygame.font.Font(None, 72)
text = font.render(winner, True, "white")
window.blit(text, (250, 100))
pygame.display.flip()
pygame.time.wait(2000)

pygame.quit()