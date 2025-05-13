from settings import *
from game import Game
from score import ScorePanel
from preview import PreviewPanel

pygame.init()


class PyTris:
    """Main game class to handle window, clock, and rendering. Esentially the glue that holds it all together"""

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyTris")

        self.game_board = Game()
        self.score_panel = ScorePanel()
        self.preview_panel = PreviewPanel()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.fill(GRAY)

            self.game_board.update_and_render()
            self.score_panel.render()
            self.preview_panel.render()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = PyTris()

    game.run()
