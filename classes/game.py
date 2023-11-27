import pygame
import random
from settings import *
from classes.unit import Unit
from classes.commander import Commander

class Game:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.font.init()
        self.font1 = pygame.font.Font(None, 16)
        self.font2 = pygame.font.Font(None, 32)
        self.play_random_music()
        self.player = Commander()
        # Max Units
        for i in range(2, MAXUNIT):
            setattr(self, f'unit{i}', None)        
        self.unit1 = Unit(name="tank")
        self.pressed = {}

        
    def play_random_music(self):
        musictrack = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        pygame.mixer.music.load('sounds/music/building' + musictrack + '.MID')
        pygame.mixer.music.play()
        
    def create_unit(self, name="tank"):
        channel = pygame.mixer.Channel(0)
        for i in range(1, MAXUNIT):
            if getattr(self, f'unit{i}') is None:
                setattr(self, f'unit{i}', Unit(name))
                unit = getattr(self, f'unit{i}')
                print(f"unité{i} created")
                if not channel.get_busy():
                    channel.play(unit.sound_deployed)
                self.select_unit()
                unit.selected = True
                break
            else:
                print(f"unit{i} => pass")
    
    def select_unit(self,):
        channel = pygame.mixer.Channel(0)
        for i in range(1, MAXUNIT):
            unit = getattr(self, f'unit{i}')
            if unit is not None and unit.rect.collidepoint(pygame.mouse.get_pos()):
                unit.selected = True
                print(f"unit{i} selected")
                unit.text_display_time = pygame.time.get_ticks()
                unit.text_display_time_max = unit.text_display_time + 2000
                if not channel.get_busy():
                    channel.play(unit.sound_select)
            elif unit is not None and not unit.rect.collidepoint(pygame.mouse.get_pos()):
                unit.selected = False
                print(f"unit{i} deselected")
        