import pygame

class Window:
    def __init__(self, height, width, caption="Тетрис"):
        self.heiht = height
        self.width = width
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.window = pygame.display.set_mode((self.width, self.heiht))


class Border:
    def __init__(self):
        self.width = 12
        self.height = 22
        self.brick = 20

    def draw(self, window):
        window.window.fill((0, 0, 0))
        for i in range(self.width):
            pygame.draw.rect(window.window, (83, 83, 83),
                             ((i * self.brick) + 1, 1, self.brick - 1, self.brick - 1))
            pygame.draw.rect(window.window, (83, 83, 83),
                             ((i * self.brick) + 1, ((self.height - 1) * self.brick) + 1, self.brick - 1, self.brick - 1))
        for j in range(1, self.height -1):
            pygame.draw.rect(window.window, (83, 83, 83),
                             (1, (j * self.brick) + 1, self.brick - 1, self.brick - 1))
            pygame.draw.rect(window.window, (83, 83, 83),
                             (((self.width - 1) * self.brick) + 1, (j * self.brick) + 1, self.brick - 1, self.brick - 1))
            #print(((i*20) + 1, 1, self.brick - 1, self.brick - 1))
