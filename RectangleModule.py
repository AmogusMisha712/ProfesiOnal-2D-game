

class Rectangle:
    
    
    
    def __init__(self, x, y, sizeX, sizeY, color = (122, 122, 122)):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.updateBorders()
        
    def draw(self, pixels):
        pixels[self.x:self.x+self.sizeX, self.y:self.y+self.sizeY] = self.color
              
                
    def move(self, pixels, directionX = 0, directionY = 0):
        pixels[self.x:self.x+self.sizeX, self.y:self.y+self.sizeY] = [255, 255, 255]
        self.x += directionX
        self.y += directionY
        self.draw(pixels)
        self.updateBorders()
        
    def updateBorders(self):
        self.borders = (
            self.y,
            self.x+self.sizeX,
            self.y+self.sizeY,
            self.x
        )