from settings import *


class ScorePanel:
    """Renders the score panel to the main window"""

    def __init__(self):
        self.screen = pygame.Surface(
            (SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING)
        )
        self.rect = self.screen.get_rect(
            bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT // 2 - PADDING)
        )
        self.display_screen = pygame.display.get_surface()

    def render(self):
        self.display_screen.blit(self.screen, self.rect)
