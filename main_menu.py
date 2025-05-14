from settings import *

TITLE_COLOURS = [
    "#f1e60d",
    "#e51b20",
    "#204b9b",
    "#65b32e",
    "#7b217f",
    "#6cc6d9",
    "#f07e13",
]


class MainMenu:
    def __init__(self, display_screen, handle_menu_button_click):
        self.screen = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA
        )

        self.display_screen = display_screen
        self.handle_menu_button_click = handle_menu_button_click

        self.title_font = pygame.font.Font("fonts/dos-vga-437.ttf", 120)

    def draw_title(self):
        title_surface_size = self.title_font.size("PYTRIS")
        title_surface_size = (
            title_surface_size[0] + PADDING,
            title_surface_size[1] + PADDING,
        )

        title_surface = pygame.Surface(title_surface_size, flags=pygame.SRCALPHA)
        title_surface.fill((0, 0, 0, 255))

        for i, char in enumerate("PYTRIS"):
            letter_surface = self.title_font.render(
                char, False, TITLE_COLOURS[i % len(TITLE_COLOURS)]
            )

            title_surface.blit(
                letter_surface,
                (self.title_font.size("P")[0] * i + PADDING // 2 + 5, PADDING // 2),
            )

        self.screen.blit(
            title_surface,
            (
                (WINDOW_WIDTH - title_surface_size[0]) // 2,
                WINDOW_HEIGHT // 12,
            ),
        )

    def render_and_update(self):
        self.screen.fill((0, 0, 0, 0))

        self.draw_title()

        self.display_screen.blit(self.screen, (0, 0))
