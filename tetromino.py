from settings import *

BLOCK_SPRITE = pygame.image.load("sprites/block.png")


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
        """Checks if the block is colliding with the sides of the board or any other blocks"""
        if not 0 <= x_pos < COLUMNS:
            return True

        if field_data[int(self.position.y)][x_pos]:
            return True

        return False

    def check_vertical_collision(self, y_pos, field_data):
        """Checks if the block is colliding with the sides of the floor or any other blocks"""
        if y_pos >= ROWS:
            return True

        if field_data[y_pos][int(self.position.x)] and y_pos >= 0:
            return True

        return False

    def rotate(self, pivot_position: pygame.Vector2) -> pygame.Vector2:
        """Rotates the block around a given pivot position"""
        return pivot_position + (self.position - pivot_position).rotate(90)

    def update(self):
        """Updates the block's visual location"""
        self.rect.topleft = self.position * CELL_SIZE


class Tetromino:
    """Organizes multiple blocks into a tetromino (ie: L, T, etc.)"""

    def __init__(
        self,
        shape: str,
        group: pygame.sprite.Group,
        create_new_tetromino,
        field_data: list[list[int | Block]],
    ):
        self.block_positions = TETROMINOS[shape]["shape"]
        self.colour = TETROMINOS[shape]["colour"]
        self.field_data = field_data
        self.shape = shape

        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]

        self.create_new_tetromino = create_new_tetromino

    def check_horizontal_collisions(self, direction: int):
        """Checks if the tetromino is colliding with the sides of the board or any other tetrominos"""
        collision_list = [
            block.check_horizontal_collision(
                int(block.position.x + direction), self.field_data
            )
            for block in self.blocks
        ]
        return True if any(collision_list) else False

    def check_vertical_collisions(self):
        """Checks if the tetromino is colliding with the floor of the board or any other tetrominos"""
        collision_list = [
            block.check_vertical_collision(int(block.position.y + 1), self.field_data)
            for block in self.blocks
        ]
        return True if any(collision_list) else False

    def move_down(self):
        """Moves the tetromino down"""
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
        """Moves the tetromino horizontally"""
        if self.check_horizontal_collisions(direction):
            return

        for block in self.blocks:
            block.position.x += direction

    def rotate(self):
        """Rotates the tetromino"""

        # if its a square we don't need to rotate it
        if self.shape == "O":
            return

        pivot_position = self.blocks[0].position

        new_block_positions = [block.rotate(pivot_position) for block in self.blocks]

        # check to make sure rotation doesn't go outside of board
        for position in new_block_positions:
            if position.x < 0 or position.x >= COLUMNS:
                return

            if self.field_data[int(position.y)][int(position.x)]:
                return

            if position.y > ROWS:
                return

        for index, block in enumerate(self.blocks):
            block.position = new_block_positions[index]
