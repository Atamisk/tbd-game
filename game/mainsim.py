import pyglet, random, math
pyglet.options['audio'] = ('pulse')
from pyglet.window import key
from pyglet.gl import *
from game import resource, player, background

class GameBoard(object):
    def __init__(self,*args, **kwargs):
        """initialize the game's player, first level and openGL subsystems"""
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
        pyglet.clock.schedule_interval(self._update,1/300.0)
        
        #Custom entities
        self.loadlevel()

        
    def on_draw(self):
        """Interrupt handler for draw functions"""
        self.screen.clear()
        self.main_batch.draw()

    def loadlevel(self):
        """Load the player and background, and place the player at the configured location on the board"""
        #File ops and variables: 
        data=open('res/lvl1.dat') #open the file containing the x- and y- coordinates for the starting position for this board. 
        bg_x,bg_y = [int(x) for x in data.readline().split(',')] #pull these values into the system. 
        player_x = self.screen.width/2 #Set player x coordinate variable used in the below constructor. 
        player_y = self.screen.height/2 #Ditto in the y direction. 
        bg_x = player_x + bg_x*2  #Convert values from the file we loaded into coordinates the MODEL matrix will understand. 
        bg_y = player_y + bg_y*2  #See above.

        #initialize Class Background with relevant options.
        self.background = background.Background(x=bg_x, y=bg_y, img=resource.bg, batch=self.main_batch, group=self.bg_group) 
        
        #Set the boundaries after which screen movement stops (Basically defines where the camera bumps the edges of the map.)
        player_x_bounds=[self.background.x + self.screen.width/2, self.background.x +  self.background.width - self.screen.width/2]
        player_y_bounds=[self.background.y + self.screen.height/2,self.background.y + self.background.height - self.screen.height/2]

        #Call the player constructor with the options we defined above. 
        self.player = player.Player(batch=self.main_batch, group=self.fg_group, x=player_x, y=player_y  ,x_bounds=player_x_bounds, y_bounds=player_y_bounds)

    def _update(self,dt):
        """
        update the game state, item by item. 
        
        Options:
        dt = 0: The time step since the last update call. Typically set using pyglet's scheduler function. 

        See singular function handler hookup in __init__ of this class.
        """
        self.player.update(dt)

        #Boolen values defining whether or not we want to move the camera in a given direction. 
        trans_right = False
        trans_left = False
        trans_up = False
        trans_down = False

        #Move the player based on which keys are pressed. 
        if self.keys[key.LEFT]:
            trans_left = self.player.move_left(dt)
        if self.keys[key.RIGHT]:
            trans_right = self.player.move_right(dt)
        if self.keys[key.UP]:
            trans_up = self.player.move_up(dt)
        if self.keys[key.DOWN]:
            trans_down = self.player.move_down(dt)

        #Move the camera based onn results from player movement. 
        if trans_left:
            glTranslatef(100*dt,0.0,0.0)
        if trans_right:
            glTranslatef(-100*dt,0.0,0.0)
        if trans_down:
            glTranslatef(0.0,100*dt,0.0)
        if trans_up:
            glTranslatef(0.0,-100*dt,0.0)


