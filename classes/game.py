import pygame
import random
from classes.unit import Unit
from classes.commander import Commander

class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.font.init()
        self.font = pygame.font.Font(None, 16)
        self.play_random_music()
        self.player = Commander()
        self.unit1 = Unit(name="tank")
        self.pressed = {}

        
    def play_random_music(self):
        musictrack = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        pygame.mixer.music.load('sounds/music/building' + musictrack + '.MID')
        pygame.mixer.music.play()
        