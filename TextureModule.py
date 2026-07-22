import numpy as np
from PIL import Image

class Texture:
    def TextureToArray(url):
        img = Image.open(url).convert('RGB')
        array = np.array(img)
        
        return array.transpose(1, 0, 2)