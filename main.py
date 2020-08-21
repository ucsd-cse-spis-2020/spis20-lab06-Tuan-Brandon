import pygame

import os

# These are the dimensions of the background image for our game

screenLength = 800

screenHeight = 427 

dim_field = (screenLength, screenHeight)

x = 200
y = 200
width = 24
height = 26

goalx = 300
goaly = 100

def main():
    # initializing all graphics
    
    screen = pygame.display.set_mode(dim_field)

    clock = pygame.time.Clock()

    background = pygame.image.load(os.path.join("assets","background.jpg"))
    background = pygame.transform.scale(background, dim_field)
    
    playerStand = pygame.image.load(os.path.join("assets", "playerSprite.png")).convert()
    playerJump = pygame.image.load(os.path.join("assets", "playerSpriteJump.png")).convert()

    playerSprite = playerStand

    flagSprite = pygame.image.load(os.path.join("assets", "flagSprite.png")).convert()

    playerStand.set_colorkey((101, 141, 209))
    playerJump.set_colorkey((101, 141, 209))
    flagSprite.set_colorkey((0, 0, 0))


    rect_player = pygame.Rect(x, y, width, height)
    rect_flag = pygame.Rect(goalx, goaly, 100, 150)
    rect_goal = pygame.Rect(goalx+75, goaly+40, 20, 300)
    platform1 = pygame.Rect(100, 300, 200, 10)
    platform2 = pygame.Rect(500, 300, 200, 10)
    ground = pygame.Rect(0, 400, 800, 100)
    
    # initializing movement variables
    
    stepsize = 10
    vel = 0
    gravity = 3
    isJumping = True
    platformList = [platform1, platform2, ground]
  
  # Game loop

    running = True

    while running:
        clock.tick(100)

    # Processing events
        #check for user inputs
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_q:
                    running = False
                
                if event.key == pygame.K_SPACE and not isJumping:
                    vel = -30
                    rect_player.move_ip(0, -10)
                    isJumping  = True
        
        # Check if the player is collided with the patforms or the ground                            
        keys = pygame.key.get_pressed()
   
        if keys[pygame.K_LEFT] and rect_player.left > 0:
            rect_player.move_ip(-stepsize, 0)
    
        if keys[pygame.K_RIGHT] and rect_player.right < screenLength:
            rect_player.move_ip(stepsize, 0)
            
        if platformList[rect_player.collidelist(platformList)].top <= rect_player.bottom and platformList[rect_player.collidelist(platformList)].bottom >= rect_player.bottom:   
            if isJumping:
                isJumping = False
                rect_player.move_ip(0, platformList[rect_player.collidelist(platformList)].top-rect_player.bottom+1)
                vel = 0
        else:
            isJumping = True

        # Check for whether the player is capable of jumping
        if isJumping:
            playerSprite = playerJump
            if vel < 30:
                vel += gravity
            rect_player.move_ip(0, vel)
        else:
            playerSprite = playerStand      
        
        # Check if the player is colliding with flag pole
        if rect_player.colliderect(rect_goal):
            running = False

        # Drawing objects
        
        pygame.draw.rect(screen, (255,0,0), rect_goal)
        screen.blit(background, (0,0))
        screen.blit(flagSprite, rect_flag)
        screen.blit(playerSprite, rect_player)

        pygame.draw.rect(screen, (255,0,0), platform1)
        pygame.draw.rect(screen, (255,0,0), platform2)
        pygame.draw.rect(screen, (0,255,0), ground)

        pygame.display.update()

 

main()