from settings import *
from game import Game
from score import ScorePanel
from preview import PreviewPanel

from random import choice

pygame.init()


class PyTris:
    """Main game class to handle window, clock, and rendering. Esentially the glue that holds it all together"""

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("PyTris")

        self.next_shape = choice(list(TETROMINOS.keys()))

        self.game = Game(self.get_next_shape, self.update_score)
        self.score_panel = ScorePanel()
        self.preview_panel = PreviewPanel()

        self.background_image = pygame.image.load("sprites/background.png")

    def update_score(self, lines, score, level):
        self.score_panel.lines = lines
        self.score_panel.score = score
        self.score_panel.level = level

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

            self.game.update_and_render()
            self.score_panel.render()
            self.preview_panel.render(self.next_shape)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = PyTris()

    game.run()
