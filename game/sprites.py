import pyglet
from game import resource


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Player, self).__init__(img=resource.player_walk, *args,**kwargs)
        self.image_list = [resource.player_walk, resource.player_idle]
        self.scale=2
        self.x = 400
        self.y = 300

        self.vel_x = 25
        
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
        if self.x > 300:
            self.x -= self.vel_x
            return True
        return False

    def move_right(self,dt):
        if self.x < 500:
            self.x += self.vel_x
            return True
        return False
