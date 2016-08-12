import pyglet
from pyglet.gl import *


pyglet.resource.path=['res']
pyglet.resource.reindex()

def texture_set_mag_filter_nearest( texture ):
    glBindTexture( texture.target, texture.id )
    glTexParameteri( texture.target, GL_TEXTURE_MAG_FILTER, GL_NEAREST )
    glBindTexture( texture.target, 0 )

def center_img(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
    return image


bg = pyglet.resource.image('bg-01.png')
player_img = pyglet.resource.image('player.png')
player_idle = center_img(player_img.get_region(249,227,11,35))
player_walk = center_img(player_img.get_region(264,227,15,35))

player_img_rev = pyglet.resource.image('player_reverse.png')
player_idle_rev = center_img(player_img_rev.get_region(540,227,11,35))
player_walk_rev = center_img(player_img_rev.get_region(521,227,15,35))

#bgm = pyglet.resource.media('bgm.mp3')




texture_set_mag_filter_nearest( player_img.get_texture() )
texture_set_mag_filter_nearest( player_img_rev.get_texture() )
