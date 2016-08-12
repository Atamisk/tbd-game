import pyglet
from pyglet.gl import *
from game import resource


class Background(pyglet.sprite.Sprite):
    _cellsize = 50 #pixels
    
    def __init__(self, *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Background, self).__init__( *args,**kwargs)
        self.x = 0
        self.y = 0
        self.scale = 2 
        

