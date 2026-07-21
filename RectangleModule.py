

class Rectangle:
    
    
    
    def __init__(self, x, y, sizeX, sizeY, color = (122, 122, 122)):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.updateBorders()
        
    def draw(self, pixels, camera_x=0, camera_y=0):
        visualX = self.x - camera_x
        visualY = self.y - camera_y

        x_start = max(0, visualX)
        y_start = max(0, visualY)
        x_end = min(800, visualX + self.sizeX)
        y_end = min(600, visualY + self.sizeY)

        if x_start < x_end and y_start < y_end:
            pixels[x_start:x_end, y_start:y_end] = self.color
              
                
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