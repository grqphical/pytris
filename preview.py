from settings import *
from os import path


class PreviewPanel:
    """Renders the preview panel to the main window"""

    def __init__(self):
        self.screen = pygame.Surface(
            (SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION - PADDING)
        )
        self.rect = self.screen.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display_screen = pygame.display.get_surface()

        self.shape_surfaces = {
            shape: pygame.image.load(
                path.join("sprites", "previews", f"{shape}.png")
            ).convert_alpha()
            for shape in TETROMINOS.keys()
        }

    def display_piece(self, shape):
        shape_surface = self.shape_surfaces[shape]
        rect = shape_surface.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        self.screen.blit(shape_surface, rect)

    def render(self, next_shape):
        self.screen.fill(GRAY)

        self.display_piece(next_shape)

        self.display_screen.blit(self.screen, self.rect)
