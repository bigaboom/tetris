import pygame
from controls import Controls
from objects import Window, Panels

pygame.init()

controls = Controls()
win = Window(440, 500)
panels = Panels()
while controls.run:
    controls.first_player()
    panels.draw_border(win)
    panels.draw_right_panel(win)
    pygame.display.update()
