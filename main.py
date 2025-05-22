from settings import *
from game import Game
from score import ScorePanel
from preview import PreviewPanel
from gameover import GameOverPopup
from main_menu import *
from settings_menu import SettingsMenu
from multiplayer_menu import MultiplayerMenu

from random import choice

pygame.init()


class PyTris:
    """Main game class to handle window, clock, and rendering. Esentially the glue that holds it all together"""

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyTris")

        icon_surface = pygame.image.load("icon.png").convert_alpha()
        pygame.display.set_icon(icon_surface)

        self.next_shape = choice(list(TETROMINOS.keys()))

        self.score_panel = ScorePanel()
        self.game = Game(self.get_next_shape, self.score_panel.set_score)
        self.preview_panel = PreviewPanel()
        self.game_over_popup = GameOverPopup()

        self.main_menu = MainMenu(self.screen, self.change_game_state)
        self.settings_menu = SettingsMenu(self.screen, self.change_game_state, None)
        self.multiplayer_menu = MultiplayerMenu(self.screen, self.change_game_state)

        self.background_image = pygame.image.load("sprites/background.png")
        self.game_state = MAIN_MENU_STATE

    def change_game_state(self, new_state):
        self.game_state = new_state

    def get_next_shape(self):
        """Returns the next shape in queue and chooses a new shape to be next in queue"""
        next_shape = self.next_shape
        self.next_shape = choice(list(TETROMINOS.keys()))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.blit(self.background_image, (0, 0))

            if self.game_state == SINGLE_PLAYER_STATE:
                self.game.update_and_render()
                self.score_panel.render()
                self.preview_panel.render(self.next_shape)

                if self.game.game_over:
                    self.game_over_popup.draw(
                        self.score_panel.score, self.score_panel.high_score
                    )
            elif self.game_state == MAIN_MENU_STATE:
                self.main_menu.render_and_update()
            elif self.game_state == SETTINGS_STATE:
                self.settings_menu.update_and_render()
            elif self.game_state == MULTIPLAYER_MENU_STATE:
                self.multiplayer_menu.update_and_render()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = PyTris()

    game.run()
