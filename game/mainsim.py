import pyglet, random, math
pyglet.options['audio'] = ('pulse')
from pyglet.window import key
from pyglet.gl import *
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
        #self.audio = pyglet.media.Player()
        #self.audio.queue(resource.bgm) 
        # keep playing for as long as the app is running (or you tell it to stop):
        #self.audio.eos_action = pyglet.media.SourceGroup.loop
        #self.audio.play()
        #print(self.audio.playing)

        #Handlers
        self.screen.push_handlers(self.on_draw)
        self.screen.push_handlers(self.keys)
        pyglet.clock.schedule_interval(self.update,1/300.0)
        
        #Custom entities
        self.background = background.Background(img=resource.bg, batch=self.main_batch, group=self.bg_group)
        player_x=self.screen.width/2
        player_y=self.screen.height/2
        player_x_bounds=[self.screen.width/2,self.background.width - self.screen.width/2]
        player_y_bounds=[self.screen.height/2,self.background.height - self.screen.height/2]
        self.player = player.Player(batch=self.main_batch, group=self.fg_group, x=player_x, y=player_y  ,x_bounds=player_x_bounds, y_bounds=player_y_bounds)

        
    def on_draw(self):
        self.screen.clear()
        self.main_batch.draw()

    def update(self,dt):
        self.player.update(dt)
        
        trans_right = False
        trans_left = False
        trans_up = False
        trans_down = False
        if self.keys[key.LEFT]:
            trans_left = self.player.move_left(dt)
        if self.keys[key.RIGHT]:
            trans_right = self.player.move_right(dt)
        if self.keys[key.UP]:
            trans_up = self.player.move_up(dt)
        if self.keys[key.DOWN]:
            trans_down = self.player.move_down(dt)

        if trans_left:
            glTranslatef(100*dt,0.0,0.0)
        if trans_right:
            glTranslatef(-100*dt,0.0,0.0)
        if trans_down:
            glTranslatef(0.0,100*dt,0.0)
        if trans_up:
            glTranslatef(0.0,-100*dt,0.0)


