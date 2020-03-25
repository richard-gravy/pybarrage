#!/usr/bin/env python3

import os
import sdl2
import sdl2.ext
import sys

VERSION = '1.0.5'

def load_image_attribs(factory: sdl2.ext.SpriteFactory, strPath: str, rgbColorKey: tuple) -> sdl2.ext.Sprite:
    sfImage = sdl2.ext.load_image(strPath)
    if not sfImage:
        return None

    sdl2.SDL_SetColorKey(sfImage, sdl2.SDL_TRUE, sdl2.SDL_MapRGB(sfImage.format, rgbColorKey[0], rgbColorKey[1], rgbColorKey[2]))
    return factory.from_surface(sfImage)

def main(argv):
    print('BARRAGE v' + VERSION)
    print('Copyright 2003-2019 Michael Speck (http://lgames.sf.net)')
    print('Released under GNU GPL\n---')
    sdl2.ext.init()
    wnd = sdl2.ext.Window('LBarrage', (0, 0), flags=sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
    intWidth = wnd.size[0]
    intHeight = wnd.size[1]
    rendr = sdl2.ext.Renderer(wnd)
    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=rendr)
    sprGround = factory.from_image(os.path.join('gfx', 'ground.bmp'))
    sprParticles = load_image_attribs(factory, os.path.join('gfx', 'particles.bmp'), (0, 0, 0))
    sprCrater = load_image_attribs(factory, os.path.join('gfx', 'crater.bmp'), (0, 0, 0))
    sprSmallCrater = load_image_attribs(factory, os.path.join('gfx', 'small_crater.bmp'), (0, 0, 0))
    sprUnits = load_image_attribs(factory, os.path.join('gfx', 'units.bmp'), (0, 0, 0))
    sprTrees = load_image_attribs(factory, os.path.join('gfx', 'trees.bmp'), (0, 0, 0))
    sprShots = load_image_attribs(factory, os.path.join('gfx', 'shots.bmp'), (0, 0, 0))
    sprAmmo = load_image_attribs(factory, os.path.join('gfx', 'ammo.bmp'), (0, 0, 0))
    sprLogo = load_image_attribs(factory, os.path.join('gfx', 'logo.bmp'), (14, 254, 234))
    sprIcons = load_image_attribs(factory, os.path.join('gfx', 'icons.bmp'), (0, 0, 0))
    sprCursors = load_image_attribs(factory, os.path.join('gfx', 'cursors.bmp'), (0, 0, 0))
    sprGun = load_image_attribs(factory, os.path.join('gfx', 'gun.bmp'), (0, 0, 0))
    wnd.show()
    rendr.copy(sprGround, dstrect=((intWidth - 1440) // 2, 0, 1440, 1080))
    rendr.copy(sprLogo, dstrect=((intWidth - sprLogo.size[0]) // 2, 70, sprLogo.size[0], sprLogo.size[1]))
    rendr.present()
    bRun = True
    while bRun:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                bRun = False
                break
            elif event.type == sdl2.SDL_KEYUP:
                if event.key.keysym.sym == sdl2.SDLK_q:
                    bRun = False
                    break

    sdl2.ext.quit()

if __name__ == '__main__': main(sys.argv)
