import pygame

# Game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# game behaviour
UPDATE_START_SPEED = 200
MOVE_WAIT_TIME = 100
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# colours
YELLOW = "#f1e60d"
RED = "#e51b20"
BLUE = "#204b9b"
GREEN = "#65b32e"
PURPLE = "#7b217f"
CYAN = "#6cc6d9"
ORANGE = "#f07e13"
GRAY = "#1C1C1C"
LINE_COLOUR = "#1C1C1C"

# shapes
TETROMINOS = {
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "colour": PURPLE},
    "O": {"shape": [(0, 0), (0, -1), (1, 0), (1, -1)], "colour": YELLOW},
    "J": {"shape": [(0, 0), (0, -1), (0, 1), (-1, 1)], "colour": BLUE},
    "L": {"shape": [(0, 0), (0, -1), (0, 1), (1, 1)], "colour": ORANGE},
    "I": {"shape": [(0, 0), (0, -1), (0, -2), (0, 1)], "colour": CYAN},
    "S": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "colour": GREEN},
    "Z": {"shape": [(0, 0), (1, 0), (0, -1), (-1, -1)], "colour": RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}
