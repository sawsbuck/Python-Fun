import pygame
from Constants import *
# Score class
class Score:
    def __init__(self, screen):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
        self.screen = screen

    def increase(self):
        self.value += 1

    def display(self):
        text = self.font.render(f"Score: {self.value}", True, WHITE)
        self.screen.blit(text, (10, 10))
