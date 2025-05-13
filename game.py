from settings import *
from tetromino import Tetromino
from random import choice
from timer import Timer


class Game:
    """Renders the grid and all other sprites for the actual tetris game. It also handles most of the game logic"""

    def __init__(self):
        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        self.create_new_tetromino()

        self.timers = {
            "vertical move": Timer(UPDATE_START_SPEED, True, self.move_blocks_down),
            "horizontal move": Timer(MOVE_WAIT_TIME),
        }

        self.timers["vertical move"].start()

    def create_new_tetromino(self):
        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetromino
        )

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_blocks_down(self):
        self.tetromino.move_down()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if not self.timers["horizontal move"].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers["horizontal move"].start()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers["horizontal move"].start()

    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (x, 0), (x, GAME_HEIGHT), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (0, y), (GAME_WIDTH, y), 1)

    def update_and_render(self):
        self.timer_update()
        self.get_input()
        self.sprites.update()

        self.screen.fill("black")
        self.draw_grid()
        self.sprites.draw(self.screen)

        self.display_screen.blit(self.screen, (PADDING, PADDING))
        pygame.draw.rect(self.display_screen, LINE_COLOUR, self.rect, 2, 2)
