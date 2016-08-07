import pyglet
from game import resource


class Background(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Background, self).__init__(img=resource.bg, *args,**kwargs)
        self.x = 0
        self.y = 0
        self.scale = 2

        self.vel_x = 100
        self.vel_y = 100
  
    def move_left(self,dt):
        """
        Move the background canvas to the left. May need to add tiled loading at some point. 
        """
        self.x -= self.vel_x * dt
     

    def move_right(self,dt):
        """
        Move the background canvas to the right. May need to add tiled loading at some point. 
        """
        self.x += self.vel_x * dt

    def move_up(self,dt):
        """
        Move the background canvas up. May need to add tiled loading at some point. 
        """
        self.y += self.vel_y * dt

    def move_down(self,dt):
        """
        Move the background canvas up. May need to add tiled loading at some point. 
        """
        self.y -= self.vel_y * dt

