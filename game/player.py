import pyglet
from game import resource, character


class Player(character.Character):
    def __init__(self, *args, **kwargs):
        # Construct a sprite with the right image and initial position. 
        super(Player, self).__init__(img=resource.player_walk, *args,**kwargs)
        self.image_right = [resource.player_walk, resource.player_idle]
        self.image_left =  [resource.player_walk_rev, resource.player_idle_rev]
        self.image_list = self.image_right
        self.scale=2
