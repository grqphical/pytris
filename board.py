from settings import *
from tetrominos import Tetromino
from random import choice
from timer import Timer


class GameBoard:
    """Renders the grid and all other sprites for the actual tetris game"""

    def __init__(self):
        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        self.initial_shape = choice(list(TETROMINOS.keys()))
        self.tetromino = Tetromino(self.initial_shape, self.sprites)

        self.timers = {
            "vertical move": Timer(UPDATE_START_SPEED, True, self.move_blocks_down)
        }

        self.timers["vertical move"].start()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_blocks_down(self):
        self.tetromino.move_down()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (x, 0), (x, GAME_HEIGHT), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (0, y), (GAME_WIDTH, y), 1)

    def render(self):
        self.timer_update()

        self.screen.fill(GRAY)
        self.sprites.update()
        self.sprites.draw(self.screen)

        self.draw_grid()

        self.display_screen.blit(self.screen, (PADDING, PADDING))
        pygame.draw.rect(self.display_screen, LINE_COLOUR, self.rect, 2, 2)
