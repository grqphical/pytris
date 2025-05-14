from settings import *
from tetromino import Tetromino
from random import choice
from timer import Timer


class Game:
    """Renders the grid and all other sprites for the actual tetris game. It also handles most of the game logic"""

    def __init__(self, get_next_shape, update_score):
        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        self.get_next_shape = get_next_shape
        self.update_score = update_score

        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]

        self.tetromino = Tetromino(
            choice(list(TETROMINOS.keys())),
            self.sprites,
            self.create_new_tetromino,
            self.field_data,
        )

        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False

        # store all of our timers in a dict for easy access
        self.timers = {
            "vertical move": Timer(self.down_speed, True, self.move_blocks_down),
            "horizontal move": Timer(MOVE_WAIT_TIME),
            "rotate timer": Timer(ROTATE_WAIT_TIME),
        }

        self.timers["vertical move"].start()

        self.current_score = 0
        self.current_level = 1
        self.cleared_lines = 0

        self.game_over = False

    def calculate_score(self, num_lines):
        self.cleared_lines += num_lines
        self.current_score += SCORE_DATA[num_lines] * self.current_level

        # every 10 lines is a level
        if self.cleared_lines // 10 > self.current_level:
            self.current_level += 1

        self.update_score(self.cleared_lines, self.current_score, self.current_level)

    def create_new_tetromino(self):
        """Creates a new tetromino and clears any rows that are full"""
        self.check_finished_rows()

        self.tetromino = Tetromino(
            self.get_next_shape(),
            self.sprites,
            self.create_new_tetromino,
            self.field_data,
        )

        # check if the new tetromino collides with any other tetrominos
        # if they do that means it's game over for the player
        if self.tetromino.check_vertical_collisions():
            self.game_over = True

    def timer_update(self):
        """Handles timer updates"""
        for timer in self.timers.values():
            timer.update()

    def move_blocks_down(self):
        """Moves the current tetromino down"""
        self.tetromino.move_down()

    def get_input(self):
        """Handles user input"""
        keys = pygame.key.get_pressed()

        if not self.timers["horizontal move"].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers["horizontal move"].start()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers["horizontal move"].start()

        # check for rotation
        if not self.timers["rotate timer"].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers["rotate timer"].start()

        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers["vertical move"].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers["vertical move"].duration = self.down_speed

    def draw_grid(self):
        """Draws the lines for the grid on the game board"""
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (x, 0), (x, GAME_HEIGHT), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.screen, LINE_COLOUR, (0, y), (GAME_WIDTH, y), 1)

    def check_finished_rows(self):
        """Checks if any rows are full and clears them and moves every block down by one"""
        delete_rows = []
        for index, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(index)

        if delete_rows:
            for delete_row in delete_rows:
                for block in self.field_data[delete_row]:
                    block.kill()

                for row in self.field_data:
                    for block in row:
                        if block and block.position.y < delete_row:
                            block.position.y += 1

            self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
            for block in self.sprites:
                self.field_data[int(block.position.y)][int(block.position.x)] = block

            # update the score with the amount of rows deleted
            self.calculate_score(len(delete_rows))

    def update_and_render(self):
        """Updates the game state and renders everything to the screen"""
        if not self.game_over:
            self.timer_update()
            self.get_input()
            self.sprites.update()

        self.screen.fill("black")
        self.draw_grid()
        self.sprites.draw(self.screen)

        self.display_screen.blit(self.screen, (PADDING, PADDING))
        pygame.draw.rect(self.display_screen, LINE_COLOUR, self.rect, 2, 2)
