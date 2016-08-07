import pyglet
from game import resource


class Player(pyglet.sprite.Sprite):
    def __init__(self, x=0, y=0, x_bounds = [100,600], y_bounds = [100,400], *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Player, self).__init__(img=resource.player_walk, *args,**kwargs)
        self.image_right = [resource.player_walk, resource.player_idle]
        self.image_left =  [resource.player_walk_rev, resource.player_idle_rev]
        self.image_list = self.image_right
        self.scale=2
        self.x = x
        self.y = y

        self.vel_x = 100
        self.vel_y = 100

        self.x_bounds = x_bounds #low and high boundary for travel in the X direction.
        self.y_bounds = y_bounds #low and high boundary for travel in the Y direction. 
        
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
        if self.x > self.x_bounds[0]:
            self.x -= self.vel_x * dt
            return False
        return True

    
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
        if self.x < self.x_bounds[1]:
            self.x += self.vel_x * dt
            return False
        return True

    def move_up(self,dt):
        """
        move player up. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        if self.y < self.y_bounds[1]:
            self.y += self.vel_y * dt
            return False
        return True

    def move_down(self,dt):
        """
        move player down. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        if self.y > self.y_bounds[0]:
            self.y -= self.vel_y * dt
            return False
        return True
