from pygame import display, event, time, draw
import pygame

#from gui import Viewport
import Geography

display.init()
x, y = 1000, 800
screen = display.set_mode((1000, 8000))
clock = time.Clock()

#viewport = Viewport(transform.scale())
keys = set()
game_over = False
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

    display.flip()

display.quit()
