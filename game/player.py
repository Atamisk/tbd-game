import pyglet
from game import resource, character


class Player(character.Character):
    def __init__(self, x_bounds = [100,600], y_bounds = [100,400], *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Player, self).__init__(img=resource.player_walk, *args,**kwargs)
        self.image_right = [resource.player_walk, resource.player_idle]
        self.image_left =  [resource.player_walk_rev, resource.player_idle_rev]
        self.image_list = self.image_right
        self.scale=2

        self.x_bounds = x_bounds #low and high boundary for travel in the X direction.
        self.y_bounds = y_bounds #low and high boundary for travel in the Y direction. 

    def move_left(self,dt):
        """
        move player to the left. Return false if movement occurs. 
        Return state typically used to move background once bounds are reached. 
        """
        super(Player, self).move_left(dt)
        if self.x < self.x_bounds[0] or self.x > self.x_bounds[1]:
            return False
        return True

    
    def move_right(self,dt):
        """
        move player to the right. Return false if movement occurs. 
        Return state typically used to move background. 
        """
        super(Player, self).move_right(dt)
        if self.x < self.x_bounds[0] or self.x > self.x_bounds[1]:
            return False
        return True

    def move_up(self,dt):
        super(Player, self).move_up(dt)
        if self.y > self.y_bounds[1] or self.y < self.y_bounds[0]:
            return False
        return True

    def move_down(self,dt):
        super(Player, self).move_down(dt)
        if self.y > self.y_bounds[1] or self.y < self.y_bounds[0]:
            return False
        return True
