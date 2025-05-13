from settings import *

BLOCK_SPRITE = pygame.transform.scale(
    pygame.image.load("sprites/block.png"), (CELL_SIZE, CELL_SIZE)
)


class Block(pygame.sprite.Sprite):
    """Class that is used to build all the tetrominos"""

    def __init__(self, group: pygame.sprite.Group, position: tuple[int, int], colour):
        super().__init__(group)

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert_alpha()
        self.image.blit(BLOCK_SPRITE, (0, 0))
        self.image.fill(colour, special_flags=pygame.BLEND_RGB_MULT)

        self.position = pygame.Vector2(position) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft=self.position * CELL_SIZE)

    def check_horizontal_collision(self, x_pos, field_data):
        if not 0 <= x_pos < COLUMNS:
            return True

        if field_data[int(self.position.y)][x_pos]:
            return True

        return False

    def check_vertical_collision(self, y_pos, field_data):
        if y_pos >= ROWS:
            return True

        if field_data[y_pos][int(self.position.x)] and y_pos >= 0:
            return True

        return False

    def update(self):
        self.rect.topleft = self.position * CELL_SIZE


class Tetromino:
    """Organizes multiple blocks into a tetromino (ie: L, T, etc.)"""

    def __init__(self, shape, group, create_new_tetromino, field_data):
        self.block_positions = TETROMINOS[shape]["shape"]
        self.colour = TETROMINOS[shape]["colour"]
        self.field_data = field_data

        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]

        self.create_new_tetromino = create_new_tetromino

    def check_horizontal_collisions(self, direction):
        collision_list = [
            block.check_horizontal_collision(
                int(block.position.x + direction), self.field_data
            )
            for block in self.blocks
        ]
        return True if any(collision_list) else False

    def check_vertical_collisions(self):
        collision_list = [
            block.check_vertical_collision(int(block.position.y + 1), self.field_data)
            for block in self.blocks
        ]
        return True if any(collision_list) else False

    def move_down(self):
        if self.check_vertical_collisions():
            for block in self.blocks:
                self.field_data[int(block.position.y)][int(block.position.x)] = block

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.move_horizontal(-1)
            if keys[pygame.K_RIGHT]:
                self.move_horizontal(1)

            self.create_new_tetromino()
        else:
            for block in self.blocks:
                block.position.y += 1

    def move_horizontal(self, direction: int):
        if self.check_horizontal_collisions(direction):
            return

        for block in self.blocks:
            block.position.x += direction
