import pygame

def main(x):

    def threenp1(n):

        # This function calculates the number of iterations of 3n+1 for each number in a range

        count = 0
        while n > 1.0:
            count = count+1
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
        return count
        
    def threenp1range(upper_limit):

        # This function creates a dictionary and assigns the amount of iterations of the 3n+1 formula a number must go through to said number 

        threenplus1_iters_dict = {}
        for i in range(2, upper_limit+1):
            iters = threenp1(i)
            threenplus1_iters_dict.update({i: iters})
        return threenplus1_iters_dict

    def graph_coordinates(threenplus1_iters_dict):

        # This is the function that handles all the graphing and calculates the maximum of said graph

        pygame.init
        display = pygame.display.set_mode()
        display.fill("white")

        coords = list(threenplus1_iters_dict.items()) # Turning my dictionary into a list of tuples that can be read by the pygame.draw.lines function
        pygame.draw.lines(display, "black", False, coords)
        
        width, height = display.get_size() # Scaling and flipping my graph to more appropriately represent the data
        new_display = pygame.transform.flip(display, False, True)
        display.blit(new_display, (0, 0))
        new_display = pygame.transform.scale(new_display, (width * 3, height * 3)) # Trying to scale the height seems to put the graph way off the screen
        display.blit(new_display, (0, -2160))
        pygame.display.flip()
        pygame.time.wait(2000)

        coords_len = len(coords) # These variables are used in the following for loop to choose the proper max amount of iterations of the graph
        max_so_far = 0
        max_coord = 0

        for x in range(coords_len):
            coords_list = coords[x]
            if coords_list[1] >= max_so_far:
                max_so_far = coords_list[1]
                max_coord = coords_list[0]
            elif coords_list[1] < max_so_far:
                pass

        pygame.font.init() # This section writes a message stating the max number of iterations and which number it was associated with
        font = pygame.font.Font(None, 48)
        message = "The max number of iterations is "+str(max_so_far)+" for the number "+str(max_coord)
        msg = font.render(message, False, "black")
        display.blit(msg, (10, 10))
        pygame.display.flip()
        pygame.time.wait(2000)
        
    graph_coordinates(threenp1range(x))

main(327) # 327 is a dummy number that I chose because it will have the maximum iterations of its graph as the final number in said graph