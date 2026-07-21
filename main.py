import pygame
import numpy as np
from RectangleModule import Rectangle
from PlayerModule import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


GRAVITY = 2
FRICTION = 1

MAX_VELOCITY_X = 10

velocityX = 0
velocityY = 0

onGround = False


pixels = np.zeros((800, 600, 3), dtype=np.uint8)
running = True

player = Player(300, 50, 50, 50, (235, 56, 56))
platform = Rectangle(100, 450, 600, 50)


def CheckCollision(player, platform):
    global velocityY, onGround

    if (player.borders[3] < platform.borders[1] and
        player.borders[1] > platform.borders[3] and
        player.borders[0] < platform.borders[2] and
        player.borders[2] > platform.borders[0]):  
        velocityY = 0
        onGround = True
        return True
    onGround = False
    return False
        

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_a]):
        velocityX -= 4
    elif (keys[pygame.K_d]):
        velocityX += 4
        
    if (keys[pygame.K_w] and onGround):
        velocityY -= 25
        
    if (velocityX > MAX_VELOCITY_X):
        velocityX = MAX_VELOCITY_X
    elif (velocityX < -MAX_VELOCITY_X):
        velocityX = -MAX_VELOCITY_X
    
    

    pixels[:, :] = [255, 255, 255]  

    player.move(pixels, int(velocityX), int(velocityY))
    
    if CheckCollision(player, platform):
        player.y = platform.borders[0] - player.sizeY
        player.updateBorders()
        velocityY = 0
        
    print(velocityX, velocityY)
    
    platform.draw(pixels)
    player.draw(pixels)
    
    velocityY += GRAVITY
    
    if (velocityX > 0):
        velocityX -= FRICTION
    elif (velocityX < 0):
        velocityX += FRICTION
        
    pygame.surfarray.blit_array(screen, pixels)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


