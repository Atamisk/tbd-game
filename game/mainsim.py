import pyglet, random, math
pyglet.options['audio'] = ('pulse')
from pyglet.window import key
from game import resource, player, background

class GameBoard(object):
    def __init__(self,*args, **kwargs):
        #Pyglet related entities
        self.main_batch = pyglet.graphics.Batch()
        self.bg_group = pyglet.graphics.OrderedGroup(0)
        self.fg_group = pyglet.graphics.OrderedGroup(1)
        self.overlay_group = pyglet.graphics.OrderedGroup(2)
        self.keys = key.KeyStateHandler()
        self.screen = pyglet.window.Window(fullscreen=True)

        #music!!
        self.audio = pyglet.media.Player()
        self.audio.queue(resource.bgm) 
        # keep playing for as long as the app is running (or you tell it to stop):
        #self.audio.eos_action = pyglet.media.SourceGroup.loop
        self.audio.play()
        print(self.audio.playing)

        #Handlers
        self.screen.push_handlers(self.on_draw)
        self.screen.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update,1/180.0)
        
        #Custom entities
        player_x=self.screen.width/2
        player_y=self.screen.height/2
        player_x_bounds=[self.screen.width*0.375,self.screen.width*0.625]
        player_y_bounds=[self.screen.height*.375,self.screen.height*0.625]
        self.player = player.Player(batch=self.main_batch, group=self.fg_group, x=player_x, y=player_y  ,x_bounds=player_x_bounds, y_bounds=player_y_bounds)
        self.background = background.Background(batch=self.main_batch, group=self.bg_group)
        
    def on_draw(self):
        self.screen.clear()
        self.main_batch.draw()

    def update(self,dt):
        self.player.update(dt)
        
        move_grid_right = False
        move_grid_left = False
        move_grid_up = False
        move_grid_down = False
        if self.keys[key.LEFT]:
            move_grid_right = self.player.move_left(dt)
        if self.keys[key.RIGHT]:
            move_grid_left = self.player.move_right(dt)
        if self.keys[key.UP]:
            move_grid_down = self.player.move_up(dt)
        if self.keys[key.DOWN]:
            move_grid_up = self.player.move_down(dt)

        
        if move_grid_left:
            self.background.move_left(dt)
        if move_grid_right:
            self.background.move_right(dt)
        if move_grid_up:
            self.background.move_up(dt)
        if move_grid_down:
            self.background.move_down(dt)
