import pyglet
from game import resource


class Character(pyglet.sprite.Sprite):
    def __init__(self,image_right = [], image_left = [], image_list = [], *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Character, self).__init__(*args,**kwargs)
        self.scale=2
        # self.x = x
        #self.y = y

        self.vel_x = 100
        self.vel_y = 100

       
        self.animate_timer = 0
        self.animate_max_time = 0.5
        self.animation_index = 0

    
    def update(self,dt):
        if self.animate_timer <= 0:
            self.animate_timer = self.animate_max_time
            self.animation_index = (self.animation_index + 1)%2
            self.image = self.image_list[self.animation_index]
        self.animate_timer -= dt
            

    def move_left(self,dt):
        """
        move player to the left. Return false if movement occurs. 
        Return state typically used to move background once bounds are reached. 
        """
        #turn player image
        if not self.image_list == self.image_left:
            self.image_list = self.image_left
            self.animate_timer = 0 #update image immediately. 
        
        #move player
        self.x -= self.vel_x * dt

    
    def move_right(self,dt):
        """
        move player to the right. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        #turn player image
        if not self.image_list == self.image_right:
            self.image_list = self.image_right
            self.animate_timer = 0 #update image immediately. 
        
        #move player
        self.x += self.vel_x * dt

    def move_up(self,dt):
        """
        move player up. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        self.y += self.vel_y * dt

    def move_down(self,dt):
        """
        move player down. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        self.y -= self.vel_y * dt
