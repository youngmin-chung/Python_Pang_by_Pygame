import pygame
import os
############################################################
pygame.init() # initiate (mandatory)

# screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


#screen title
pygame.display.set_caption("PANG") # game name

# FPS
clock = pygame.time.Clock()


############################################################
# 1. Initiate user game ( Background, game image, coordinates, speed, font and etc.)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")


#background image
background = pygame.image.load(os.path.join(image_path,"bg.png"))

#stage
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # character is on the stage

#character
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width= character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True # Is game running or not?!
while running:
    dt = clock.tick(60) # set the FPS on the screen

    # 2. Events (keyboard, mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Does a closing event occur or not
            running = False

    # 3. Character location

    # 4. collision management

    # 5. draw on screen
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # background image update

#pygame close
pygame.quit()