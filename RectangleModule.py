from TextureModule import Texture
import numpy as np

class Rectangle:
    
    
    
    def __init__(self, x, y, sizeX, sizeY, color = (122, 122, 122), textureUrl = ""):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.updateBorders()
        
        if (textureUrl != ""):
            self.texture = Texture.TextureToArray(textureUrl)
            if (self.texture.shape[1] != self.sizeY and 
                self.texture.shape[0] != self.sizeX):
                self.texture = color
                print("Texture too small or too big!")
        else:
            self.texture = np.full((self.sizeX, self.sizeY, 3), color, dtype=np.uint8)        
    def draw(self, pixels, camera_x=0, camera_y=0):
        vis_x = self.x - camera_x
        vis_y = self.y - camera_y

        x_start = max(0, vis_x)
        y_start = max(0, vis_y)
        x_end = min(800, vis_x + self.sizeX)
        y_end = min(600, vis_y + self.sizeY)

        if x_start >= x_end or y_start >= y_end:
            return
            
        tex_start_x = x_start - vis_x
        tex_start_y = y_start - vis_y
        tex_end_x = tex_start_x + (x_end - x_start)
        tex_end_y = tex_start_y + (y_end - y_start)
        
        pixels[x_start:x_end, y_start:y_end] = self.texture[tex_start_x:tex_end_x, tex_start_y:tex_end_y]
              
                
    def move(self, pixels, directionX = 0, directionY = 0):
        pixels[self.x:self.x+self.sizeX, self.y:self.y+self.sizeY] = [255, 255, 255]
        self.x += directionX
        self.y += directionY
        self.updateBorders()
        
    def moveTo(self, pixels, x, y):
        pixels[self.x:self.x+self.sizeX, self.y:self.y+self.sizeY] = [255, 255, 255]
        self.x = x
        self.y = y
        self.updateBorders()
        
    def updateBorders(self):
        #print(self.x, self.y)
        self.borders = (
            self.y,
            self.x+self.sizeX,
            self.y+self.sizeY,
            self.x
        )