from settings import *
from os import path


class GameOverPopup:
    def __init__(self):
        self.font = pygame.font.Font(path.join("fonts", "dos-vga-437.ttf"), 80)
        self.screen = pygame.Surface((GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        self.rect = self.screen.get_rect(topleft=(GAME_OVER_PADDING, GAME_OVER_PADDING))
        self.display_screen = pygame.display.get_surface()

        self.increment_height = self.screen.get_height() // 2

    def draw(self, score):
        self.screen.fill("black")

        text_x = self.screen.get_width() // 2
        title_y = self.increment_height // 2
        score_y = self.increment_height // 2 + self.increment_height

        text_surface = self.font.render("GAME OVER", False, "white")
        text_rect = text_surface.get_rect(center=(text_x, title_y))
        self.screen.blit(text_surface, text_rect)

        self.display_screen.blit(self.screen, self.rect)
