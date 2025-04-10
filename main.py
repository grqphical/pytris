import pygame
from settings import *

pygame.init()


class PyTris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyTris")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.fill(GRAY)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = PyTris()

    game.run()
