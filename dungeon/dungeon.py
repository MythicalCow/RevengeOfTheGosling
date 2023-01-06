# import pygame module in this program
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
width = 1200
height = 800

win = pygame.display.set_mode([width, height])

# set the pygame window name
pygame.display.set_caption("A Textbook Adventure")

file = open("introduction.txt", "r")
introduction = file.readlines()
file.close()

file = open("node1.txt", "r")
node1txt = file.readlines()
file.close()



# Indicates pygame is running
run = True

intro_node = False
first_node = False


my_font = pygame.font.SysFont('Raleway', 40, bold=True)
text_surface = my_font.render("A Textbook Adventure", False, (255, 255, 255))
text_rect = text_surface.get_rect(center=(width/2, height/2))
win.blit(text_surface, text_rect)

my_font = pygame.font.SysFont('Raleway', 15, bold=True)
text_surface = my_font.render("Press Down Arrow To Start", False, (255, 255, 255))
text_rect = text_surface.get_rect(center=(width/2, height-40))
win.blit(text_surface, text_rect)

while run:
	# creates time delay of 10ms
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
        # stores keys pressed
        #elif event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

                # if left arrow key is pressed

        #INTRODUCTION KEYPRESSES
        
        if keys[pygame.K_DOWN] and intro_node == False:
            intro_node = True
            win.fill((0, 0, 0))
            pygame.time.delay(500)


        if keys[pygame.K_DOWN] and intro_node == True and len(introduction) > 0:
            #print text on screen
            win.fill((0, 0, 0))
            my_font = pygame.font.SysFont('Times New Roman', 20)
            text_surface = my_font.render(introduction[0], False, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width/2, height/2))
            win.blit(text_surface, text_rect)
            introduction.pop(0)
            pygame.time.delay(500)
        
        if len(introduction) == 0 and first_node != True:
            intro_node = False
            win.fill((0, 0, 0))
            pygame.time.delay(500)
            first_node = True

            #INTRODUCTION KEYPRESSES


        if keys[pygame.K_DOWN] and first_node==True and len(node1txt) > 0:
            #print text on screen
            win.fill((0, 0, 0))
            my_font = pygame.font.SysFont('Times New Roman', 20)
            text_surface = my_font.render(node1txt[0], False, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width/2, height/2))
            win.blit(text_surface, text_rect)
            node1txt.pop(0)
            pygame.time.delay(500)
        
        if len(node1txt) == 0:
            first_node = False
        



    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
