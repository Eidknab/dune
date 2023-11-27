import pygame, sys
from settings import *
from classes.game import Game
from classes.commander import Commander
from classes.unit import Unit

pygame.init()
pygame.display.set_caption(GAMENAME)
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))

game = Game()
help_text = game.font2.render("Press D to deploy. Left Clic to select. Arrow Keys to move", True, (255, 255, 255))
channel = pygame.mixer.Channel(0)

# Game loop
running = True
while running:
    # Draw background in multiple tiles
    for y in range(0, HEIGTH, TILESIZE):
        for x in range(0, WIDTH, TILESIZE):
            SCREEN.blit(BACKGROUND, (x, y))
    
    for i in range(1, MAXUNIT):
        channel = pygame.mixer.Channel(0)
        unit = getattr(game, f'unit{i}')
        if unit is not None and game.pressed.get(pygame.K_UP) and unit.rect.y > 0 and unit.selected:
            unit.move_up()
            unit.image = pygame.image.load('assets/' + unit.name + '_up.png')
        elif unit is not None and game.pressed.get(pygame.K_DOWN) and unit.rect.y < HEIGTH - TILESIZE and unit.selected:
            unit.move_down()
            unit.image = pygame.image.load('assets/' + unit.name + '_down.png')
        elif unit is not None and game.pressed.get(pygame.K_RIGHT) and unit.rect.x < WIDTH - TILESIZE and unit.selected:
            unit.move_right()
            unit.image = pygame.image.load('assets/' + unit.name + '_right.png')
        elif unit is not None and game.pressed.get(pygame.K_LEFT) and unit.rect.x > 0 and unit.selected:
            unit.move_left()
            unit.image = pygame.image.load('assets/' + unit.name + '_left.png')
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.USEREVENT:
            game.play_random_music()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.select_unit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                game.pressed[event.key] = True
            elif event.key == pygame.K_d:
                game.create_unit("tank")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                game.pressed[event.key] = False
    
    for i in range(1, MAXUNIT):
        unit = getattr(game, f'unit{i}')
        if unit is not None:
            if unit.text_display_time and pygame.time.get_ticks() - unit.text_display_time < unit.text_display_time_max:
                text = game.font1.render(unit.message_selection, True, (255, 255, 255))
                SCREEN.blit(text, (unit.rect.x - 4, unit.rect.y - 16))
    # Draw units
    for i in range(1, MAXUNIT):
        unit = getattr(game, f'unit{i}')
        if unit is not None:
            SCREEN.blit(unit.image, unit.rect)
    # Draw help text
    SCREEN.blit(help_text, (0, 480-32))
    
    # Screen refresh
    pygame.display.flip()
