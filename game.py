from settings import *
from tetromino import Tetromino
from random import choice
from timer import Timer


class Game:
    """Renders the grid and all other sprites for the actual tetris game. It also handles most of the game logic"""

    def __init__(self, get_next_shape, update_score):
        pygame.mixer.init()

        self.screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_screen = pygame.display.get_surface()
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()

        self.game_backdrop = pygame.image.load("sprites/game-background.png")

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

        self.drop_sound = pygame.mixer.Sound("audio/Hit.wav")
        self.clear_row_sound = pygame.mixer.Sound("audio/Boom.wav")
        self.level_up_sound = pygame.mixer.Sound("audio/Pickup.wav")

        # store all of our timers in a dict for easy access
        self.timers = {
            "vertical move": Timer(self.down_speed, True, self.move_blocks_down),
            "horizontal move": Timer(MOVE_WAIT_TIME),
            "rotate timer": Timer(ROTATE_WAIT_TIME),
            "drop timer": Timer(DROP_WAIT_TIME),
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
        if self.cleared_lines / 10 > self.current_level:
            self.current_level += 1
            self.down_speed *= 0.75
            self.down_speed_faster = self.down_speed * 0.3
            self.timers["vertical move"].duration = self.down_speed

            self.level_up_sound.play()

        self.update_score(self.current_score, self.current_level, self.cleared_lines)

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

        if keys[pygame.K_SPACE] and not self.timers["drop timer"].active:
            self.tetromino.drop()
            self.timers["drop timer"].start()
            self.drop_sound.play()

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

            self.clear_row_sound.play()

    def update_and_render(self):
        """Updates the game state and renders everything to the screen"""
        if not self.game_over:
            self.timer_update()
            self.get_input()
            self.sprites.update()

        self.screen.blit(self.game_backdrop, (0, 0))
        self.sprites.draw(self.screen)

        self.display_screen.blit(self.screen, (PADDING, PADDING))
