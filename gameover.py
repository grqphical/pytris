from settings import *
from os import path


class GameOverPopup:
    def __init__(self):
        self.title_font = pygame.font.Font(path.join("fonts", "dos-vga-437.ttf"), 80)
        self.score_font = pygame.font.Font(path.join("fonts", "dos-vga-437.ttf"), 40)
        self.screen = pygame.Surface((GAME_OVER_WIDTH, GAME_OVER_HEIGHT))
        self.rect = self.screen.get_rect(topleft=(PADDING, PADDING * 5))
        self.display_screen = pygame.display.get_surface()

        self.increment_height = self.screen.get_height() // 2

    def draw(self, score, high_score):
        self.screen.fill("black")

        text_x = self.screen.get_width() // 2
        title_y = self.increment_height // 2
        score_y = self.increment_height // 2 + self.increment_height

        title_surface = self.title_font.render("GAME OVER", False, "white")
        title_rect = title_surface.get_rect(center=(text_x, title_y))
        self.screen.blit(title_surface, title_rect)

        if score >= high_score:
            high_score_surface = self.score_font.render(
                f"NEW HIGH SCORE: {high_score}", False, "white"
            )
            high_score_rect = high_score_surface.get_rect(center=(text_x, score_y))
            self.screen.blit(high_score_surface, high_score_rect)

        self.display_screen.blit(self.screen, self.rect)
        pygame.draw.rect(self.display_screen, "white", self.rect, 2, 2)
