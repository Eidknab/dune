import pygame

class Unit(pygame.sprite.Sprite):
    def __init__(self, name="soldier"):
        super().__init__()
        self.name = name
        self.text_display_time = None
        self.text_display_time_max = 1000
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.attack_range = 16
        self.defense = 0
        self.speed = 4
        self.image = pygame.image.load('assets/' + name + '_right.png')
        self.sound_select = pygame.mixer.Sound('sounds/unit_deployed.wav')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 240
        self.selected = False
        
    def move_up(self):
        self.rect.y -= self.speed
        
    def move_down(self):
        self.rect.y += self.speed
    
    def move_right(self):
        self.rect.x += self.speed
        
    def move_left(self):
        self.rect.x -= self.speed