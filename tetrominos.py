from settings import *

BLOCK_SPRITE = pygame.transform.scale(
    pygame.image.load("sprites/block.png"), (CELL_SIZE, CELL_SIZE)
)


class Block(pygame.sprite.Sprite):
    """Class that is used to build all the tetrominos"""

    def __init__(self, group: pygame.sprite.Group, position: tuple[int, int], color):
        super().__init__(group)

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert_alpha()
        self.image.blit(BLOCK_SPRITE, (0, 0))
        self.image.fill(color, special_flags=pygame.BLEND_RGB_MULT)

        x = position[0] * CELL_SIZE
        y = position[1] * CELL_SIZE

        self.rect = self.image.get_rect(topleft=(x, y))
