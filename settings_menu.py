from settings import *
from main_menu import Button, MAIN_MENU_STATE


class SettingsMenu:
    def __init__(self, display_screen, change_game_state, handle_setting_change):
        self.screen = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA
        )

        self.display_screen = display_screen
        self.change_game_state = change_game_state
        self.handle_setting_change = handle_setting_change

        self.title_font = pygame.font.Font("fonts/dos-vga-437.ttf", 80)
        self.regular_font = pygame.font.Font("fonts/dos-vga-437.ttf", 40)

        self.back_button = Button(
            (WINDOW_WIDTH - 200) // 2,
            WINDOW_HEIGHT // 12 * 11,
            200,
            50,
            "Back",
            "white",
            "black",
        )

    def draw_title(self):
        title_surface = self.title_font.render("Settings", False, "white", "black")
        self.screen.blit(
            title_surface,
            (
                (WINDOW_WIDTH - title_surface.get_size()[0]) // 2,
                WINDOW_HEIGHT // 12,
            ),
        )

    def update_and_render(self):
        if self.back_button.is_pressed():
            self.change_game_state(MAIN_MENU_STATE)

        self.screen.fill((0, 0, 0, 0))

        self.draw_title()

        self.back_button.draw(self.screen)

        self.display_screen.blit(self.screen, (0, 0))
