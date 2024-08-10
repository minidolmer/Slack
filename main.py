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
grounded = False #Am i on the ground?
jump_count = 0
box_location = [200, 300]
box_size = [100, 20]

while True:
    screen.fill((150,250,250))
    pygame.draw.rect(screen, (29, 207, 195), (*box_location, *box_size))
    screen.blit(player_image,player_location)
    player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
    box_rect = pygame.Rect(box_location[0], box_location[1], box_size[0], box_size[1])
    
    if player_rect.colliderect(box_rect) and player_y_momentum > 0:
        player_location[1] = box_location[1] - player_image.get_height()
        player_y_momentum = 0
    
    if player_rect.colliderect(box_rect) and player_y_momentum > 0:
        player_location[1] = box_location[1] - player_image.get_height()
        player_y_momentum = 0
        grounded = True
        jump_count = 0
    
    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_location[1] = WINDOW_SIZE[1] - player_image.get_height()
        player_y_momentum = 0
        grounded = True
        jump_count = 0
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
            if event.key == K_SPACE and (grounded or jump_count < 2):
                player_y_momentum = -10
                grounded = False
                jump_count += 1
                print("jumping :D")
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