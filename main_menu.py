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


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        text_colour,
        background_colour,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font("fonts/dos-vga-437.ttf", 60)
        self.text_colour = text_colour
        self.background_colour = background_colour

        self.text_surface = self.font.render(text, False, text_colour)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.background_colour, self.rect)
        surface.blit(self.text_surface, self.text_rect)

    def is_pressed(self):
        mouse_buttons_pressed = pygame.mouse.get_just_pressed()
        if mouse_buttons_pressed[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


class MainMenu:
    def __init__(self, display_screen, handle_menu_button_click):
        self.screen = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA
        )

        self.display_screen = display_screen
        self.handle_menu_button_click = handle_menu_button_click

        self.title_font = pygame.font.Font("fonts/dos-vga-437.ttf", 120)

        self.single_player_button = Button(
            (WINDOW_WIDTH - 500) // 2,
            WINDOW_HEIGHT // 12 * 4,
            500,
            60,
            "Singleplayer",
            "white",
            "black",
        )
        self.multiplayer_button = Button(
            (WINDOW_WIDTH - 500) // 2,
            WINDOW_HEIGHT // 12 * 6,
            500,
            60,
            "Multiplayer",
            "white",
            "black",
        )

        self.settings_button = Button(
            (WINDOW_WIDTH - 500) // 2,
            WINDOW_HEIGHT // 12 * 8,
            500,
            60,
            "Settings",
            "white",
            "black",
        )

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

        self.single_player_button.draw(self.screen)
        self.multiplayer_button.draw(self.screen)
        self.settings_button.draw(self.screen)

        self.display_screen.blit(self.screen, (0, 0))
