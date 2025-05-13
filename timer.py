import pygame


class Timer:
    def __init__(self, duration: float, repeated: bool = False, timeout_func=None):
        self.duration = duration
        self.repeated = repeated
        self.timeout_func = timeout_func

        self.start_time = 0
        self.active = False

    def start(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def stop(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            if self.timeout_func and self.start_time != 0:
                self.timeout_func()

            self.stop()

            if self.repeated:
                self.start()
