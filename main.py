import pygame, sys, time
print("Welcome to my first PyGame platformer :D")
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Practising PyGame")

WINDOW_SIZE = (400,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

player_image = pygame.image.load("character.png") #blue cube (player)
player_image = pygame.transform.scale(player_image, (50,50))

moving_right = False
moving_left = False

player_location = [150,150]
player_y_momentum = 0

while True:
    screen.fill((150,250,250))
    
    screen.blit(player_image,player_location)
    
    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    if moving_right == True:
        player_location[0] += 6
    if moving_left == True:
        player_location[0] -= 6
    
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Commiting death")
            time.sleep(0.5)
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
                print("moving right")
            if event.key == K_a:
                moving_left = True
                print("moving left")
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
                print("not moving right")
            if event.key == K_a:
                moving_left = False
                print("not moving left")
            
    pygame.display.update()
    clock.tick(30)