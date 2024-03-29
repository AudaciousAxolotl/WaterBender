from pygame import display, event, time, draw, transform
import pygame
#My import. Don't forget to do pip install libaudioverse, or this file won't run.
import libaudioverse
import soundutil
#end my import
#from gui import Viewport

from gui import Viewport
from water import Graph
libaudioverse.initialize()
server = libaudioverse.Server()
server.set_output_device("default")
bgMusic = soundutil.SoundPlayer(server)
bgAmbience = soundutil.SoundPlayer(server)
bgmPath = "assets\\waterbending.wav"
bgaPath = "assets\\underwater.wav"
display.init()
x, y = 1000, 800
screen = display.set_mode((x, y))
clock = time.Clock()

v_graph = Graph(screen)
keys = set()
game_over = False
bgMusic.play(bgmPath, True)
bgAmbience.play(bgaPath,  True)
while not game_over:
    elapsed = clock.tick()/1000
    events = event.get()

    for curr_event in events:
        if curr_event.type == pygame.QUIT:
            game_over = True
        elif curr_event.type == pygame.KEYDOWN:
            if curr_event.key == pygame.K_ESCAPE:
                game_over = True
            keys.add(curr_event.key)
        elif curr_event.type == pygame.KEYUP:
            keys.remove(curr_event.key)

    screen.fill((0, 0, 0))

    v_graph.draw(screen)
    #draw.circle(screen, (255, 0, 255), (500, 500), 30)

    display.flip()

display.quit()
libaudioverse.shutdown()
print("You win!")
#That's just their in case nothing else gets done, and we feel like being a troll. LOL!!!