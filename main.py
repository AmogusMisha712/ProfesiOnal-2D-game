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

player = Player(750//2, 300, 50, 50, (235, 56, 56), "player.png")
platforms = (
        Rectangle(100, 450, 600, 50),
        Rectangle(800, 400, 400, 50),
        Rectangle(-600+2000, 2000, 400, 200, textureUrl="secret.png"),
        
        Rectangle(-550+2000, 1750, 25, 125),
        Rectangle(-525+2000, 1750, 50, 25),
        Rectangle(-525+2000, 1800, 50, 25),
        Rectangle(-500+2000, 1825, 25, 25),
        Rectangle(-525+2000, 1850, 50, 25),
        
        Rectangle(-450+2000, 1750, 75, 25),
        Rectangle(-400+2000, 1750, 25, 125),
    )


camera_x = 0
camera_y = 0


def CheckCollision(player, platform):
    global velocityY, onGround

    # Borders
    p_top, p_right, p_bottom, p_left = player.borders
    pl_top, pl_right, pl_bottom, pl_left = platform.borders

    # Check
    if (p_right > pl_left and p_left < pl_right and
        p_bottom > pl_top and p_top < pl_bottom):

        # Overlap
        overlap_left  = p_right - pl_left 
        overlap_right = pl_right - p_left 
        overlap_top   = p_bottom - pl_top 
        overlap_bottom = pl_bottom - p_top

        # X offset
        if overlap_left < overlap_right:
            offset_x = -overlap_left
        else:
            offset_x = overlap_right

        # Y offset
        if overlap_top < overlap_bottom:
            offset_y = -overlap_top  
        else:
            offset_y = overlap_bottom
        
        # Max offset
        if abs(offset_x) < abs(offset_y):
            player.move(pixels, offset_x, 0)
            onGround = False 
        else:
            player.move(pixels, 0, offset_y)
            # On ground
            if offset_y < 0:
                onGround = True
            else:
                onGround = False

        velocityY = 0
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
        
    if (keys[pygame.K_F5] or player.y > 4000):
        player.moveTo(pixels, 750//2, 300)
        velocityY = 0
        
    if (velocityX > MAX_VELOCITY_X):
        velocityX = MAX_VELOCITY_X
    elif (velocityX < - MAX_VELOCITY_X):
        velocityX = - MAX_VELOCITY_X
    
    

    pixels[:, :] = [255, 255, 255]  

    player.move(pixels, int(velocityX), int(velocityY))
    
    for platform in platforms:
        if CheckCollision(player, platform):
            player.updateBorders()
            velocityY = 0
            break
        
    camera_x = player.x - 750//2
    camera_y = player.y - 550//2
        
    #print(velocityX, velocityY)
    #print(camera_x, camera_y)
    #print(onGround)
    
    for platform in platforms:
        platform.draw(pixels, camera_x, camera_y)
    
    player.draw(pixels, camera_x, camera_y)
    
    velocityY += GRAVITY
    
    if (velocityX > 0):
        velocityX -= FRICTION
    elif (velocityX < 0):
        velocityX += FRICTION
        
    pygame.surfarray.blit_array(screen, pixels)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


