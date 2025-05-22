from settings import *
from main_menu import Button, MAIN_MENU_STATE
import pygame


class TextBox:
    def __init__(
        self, x, y, width, height, font, text_color, background_color, initial_text=""
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text_color = text_color
        self.background_color = background_color
        self.text = initial_text
        self.is_active = False

    def update(self):
        mouse_buttons_down = pygame.mouse.get_pressed()

        if mouse_buttons_down[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_active = True

        if self.is_active:
            keys_pressed = pygame.key.get_just_pressed()
            for key in range(len(keys_pressed)):
                if keys_pressed[key]:
                    if key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif key == pygame.K_RETURN or key == pygame.K_ESCAPE:
                        self.is_active = False
                    else:
                        if (
                            pygame.key.name(key).isalnum()
                            or pygame.key.name(key) == "."
                        ):
                            self.text += pygame.key.name(key)

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)
        text_surface = self.font.render(self.text, False, self.text_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        if self.is_active:
            pygame.draw.rect(screen, "white", self.rect, 2)

    def get_text(self):
        return self.text


class MultiplayerMenu:
    def __init__(self, display_screen, change_game_state):
        self.screen = pygame.Surface(
            (WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA
        )

        self.display_screen = display_screen
        self.change_game_state = change_game_state

        self.title_font = pygame.font.Font("fonts/dos-vga-437.ttf", 80)
        self.regular_font = pygame.font.Font("fonts/dos-vga-437.ttf", 40)

        self.back_button = Button(
            (WINDOW_WIDTH - 200) // 2,
            WINDOW_HEIGHT // 12 * 11,
            200 + PADDING,
            50 + PADDING,
            "Back",
            "white",
            "black",
        )

        self.connect_button = Button(
            (WINDOW_WIDTH - 250) // 2,
            WINDOW_HEIGHT // 12 * 5,
            250 + PADDING,
            50 + PADDING,
            "Connect",
            "white",
            "black",
        )

        self.ip_box = TextBox(
            (WINDOW_WIDTH - 400) // 2,
            WINDOW_HEIGHT // 12 * 4,
            400,
            50,
            self.regular_font,
            "white",
            "black",
        )

    def draw_title(self):
        title_surface = self.title_font.render("Multiplayer", False, "white", "black")
        self.screen.blit(
            title_surface,
            (
                (WINDOW_WIDTH - title_surface.get_size()[0]) // 2,
                WINDOW_HEIGHT // 12,
            ),
        )

    def update_and_render(self):
        self.ip_box.update()

        if self.back_button.is_pressed():
            self.change_game_state(MAIN_MENU_STATE)

        self.screen.fill((0, 0, 0, 0))

        self.draw_title()

        self.back_button.draw(self.screen)

        ip_box_title_surface = self.regular_font.render(
            "Enter server IP:", False, "white", "black"
        )
        self.screen.blit(
            ip_box_title_surface,
            ((WINDOW_WIDTH - 400) // 2, WINDOW_HEIGHT // 12 * 4 - 50),
        )

        self.ip_box.draw(self.screen)
        self.connect_button.draw(self.screen)

        self.display_screen.blit(self.screen, (0, 0))
