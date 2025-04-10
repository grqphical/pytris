from settings import *


class GameBoard:
    """Renders the grid and all other sprites for the actual tetris game"""

    def __init__(self):
        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()

    def render(self):
        self.display_screen.blit(self.screen, (PADDING, PADDING))
