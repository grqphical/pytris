from settings import *
from os import path


class ScorePanel:
    """Renders the score panel to the main window"""

    def __init__(self):
        self.screen = pygame.Surface(
            (SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING)
        )
        self.rect = self.screen.get_rect(
            bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)
        )
        self.display_screen = pygame.display.get_surface()

        self.font = pygame.font.Font(path.join("fonts", "dos-vga-437.ttf"), 30)

        self.increment_height = self.screen.get_height() // 3

        self.score = 0
        self.level = 1
        self.lines = 0

    def display_text(self, position, text, amount):
        text_surface = self.font.render(f"{text}: {amount}", False, "white")
        text_rect = text_surface.get_rect(center=position)

        self.screen.blit(text_surface, text_rect)

    def render(self):

        self.screen.fill("black")

        for i, text in enumerate(
            [("Score", self.score), ("Level", self.level), ("Lines", self.lines)]
        ):
            x = self.screen.get_width() // 2
            y = self.increment_height // 2 + i * self.increment_height

            self.display_text((x, y), text[0], text[1])

        self.display_screen.blit(self.screen, self.rect)
