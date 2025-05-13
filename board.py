from settings import *
from tetrominos import Block


class GameBoard:
    """Renders the grid and all other sprites for the actual tetris game"""

    def __init__(self):
        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        self.block = Block(self.sprites)

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOR, (x, 0), (x, GAME_HEIGHT), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOR, (0, y), (GAME_WIDTH, y), 1)

    def render(self):
        self.screen.fill(GRAY)
        self.sprites.draw(self.screen)

        self.draw_grid()

        self.display_screen.blit(self.screen, (PADDING, PADDING))
        pygame.draw.rect(self.display_screen, LINE_COLOR, self.rect, 2, 2)
