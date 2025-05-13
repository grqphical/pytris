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

    def update(self):
        self.rect.topleft = self.position * CELL_SIZE


class Tetromino:
    """Organizes multiple blocks into a tetromino (ie: L, T, etc.)"""

    def __init__(self, shape, group):
        self.block_positions = TETROMINOS[shape]["shape"]
        self.colour = TETROMINOS[shape]["colour"]

        self.blocks = [Block(group, pos, self.colour) for pos in self.block_positions]

    def move_down(self):
        for block in self.blocks:
            block.position.y += 1
