import pygame


class Window:
    def __init__(self, height, width, caption="Тетрис"):
        self.height = height
        self.width = width
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.window = pygame.display.set_mode((self.width, self.height))


class Panels:
    def __init__(self):
        self.lp_width = 12
        self.lp_height = 22
        self.rp_width = 13
        self.rp_height = 22
        self.brick = 20

    def draw_border(self, window):
        window.window.fill((0, 0, 0))
        for i in range(self.lp_width):
            pygame.draw.rect(window.window, (83, 83, 83),
                             ((i * self.brick) + 1, 1, self.brick - 1, self.brick - 1))
            pygame.draw.rect(window.window, (83, 83, 83),
                             ((i * self.brick) + 1, ((self.lp_height - 1) * self.brick) + 1,
                              self.brick - 1, self.brick - 1))
        for j in range(1, self.lp_height - 1):
            pygame.draw.rect(window.window, (83, 83, 83),
                             (1, (j * self.brick) + 1, self.brick - 1, self.brick - 1))
            pygame.draw.rect(window.window, (83, 83, 83), (((self.lp_width - 1) * self.brick) + 1,
                                                           (j * self.brick) + 1, self.brick - 1, self.brick - 1))

    def draw_next_panel(self, window, spx, spy):
        count_x = 5
        count_y = 6
        startpoint_x = spx + 4 * self.brick
        startpoint_y = spy + 2 * self.brick
        pygame.draw.rect(window.window, (0, 0, 0),
                         (startpoint_x, startpoint_y, (count_x * self.brick) + 1, (count_y * self.brick) + 1))

    def draw_right_panel(self, window):
        startpoint_x = (self.lp_width * self.brick)
        startpoint_y = 0
        endpoint_x = self.rp_width * self.brick
        endpoint_y = self.rp_height * self.brick
        pygame.draw.rect(window.window, (83, 83, 83),
                         (startpoint_x + 1, startpoint_y + 1, endpoint_x - 1, endpoint_y - 1))
        self.draw_next_panel(window, startpoint_x, startpoint_y)
