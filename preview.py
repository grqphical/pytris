from settings import *


class PreviewPanel:
    """Renders the preview panel to the main window"""

    def __init__(self):
        self.screen = pygame.Surface(
            (SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION - PADDING)
        )
        self.rect = self.screen.get_rect(topright=(WINDOW_WIDTH - PADDING, PADDING))
        self.display_screen = pygame.display.get_surface()

    def render(self):
        self.display_screen.blit(self.screen, self.rect)
