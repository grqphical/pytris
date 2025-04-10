import pygame
from settings import *

pygame.init()


class PyTris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_HEIGHT))
        pygame.display.set_caption("PyTris")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()


if __name__ == "__main__":
    game = PyTris()

    game.run()
