import pygame


class Controls:
    def __init__(self):
        self.run = True

    def first_player(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.run = False
