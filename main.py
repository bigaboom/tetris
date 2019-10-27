import pygame
from controls import Controls
from objects import Window, Border

pygame.init()

controls = Controls()
win = Window(440, 240)
border = Border()
while controls.run:
    controls.first_player(win)
    border.draw(win)
    pygame.display.update()
