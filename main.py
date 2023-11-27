import pygame, sys
from settings import *
from classes.game import Game
from classes.commander import Commander
from classes.unit import Unit

pygame.init()
pygame.display.set_caption(GAMENAME)
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))

game = Game()

# Game loop
running = True
while running:
    # Draw background in multiple tiles
    for y in range(0, HEIGTH, TILESIZE):
        for x in range(0, WIDTH, TILESIZE):
            SCREEN.blit(BACKGROUND, (x, y))
    SCREEN.blit(game.unit1.image, game.unit1.rect)
    
    if game.pressed.get(pygame.K_UP) and game.unit1.rect.y > 0 and game.unit1.selected:
        game.unit1.move_up()
        game.unit1.image = pygame.image.load('assets/' + game.unit1.name + '_up.png')
    elif game.pressed.get(pygame.K_DOWN) and game.unit1.rect.y < HEIGTH - TILESIZE and game.unit1.selected:
        game.unit1.move_down()
        game.unit1.image = pygame.image.load('assets/' + game.unit1.name + '_down.png')
    elif game.pressed.get(pygame.K_RIGHT) and game.unit1.rect.x < WIDTH - TILESIZE and game.unit1.selected:
        game.unit1.move_right()
        game.unit1.image = pygame.image.load('assets/' + game.unit1.name + '_right.png')
    elif game.pressed.get(pygame.K_LEFT) and game.unit1.rect.x > 0 and game.unit1.selected:
        game.unit1.move_left()
        game.unit1.image = pygame.image.load('assets/' + game.unit1.name + '_left.png')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.USEREVENT:
            game.play_random_music()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.unit1.rect.collidepoint(pygame.mouse.get_pos()):
                game.unit1.selected = True
                print("Unit selected")
                game.unit1.text_display_time = pygame.time.get_ticks()
                game.unit1.text_display_time_max = game.unit1.text_display_time + 2000
                game.unit1.sound_select.play()
            else:
                game.unit1.selected = False
                print("Unit deselected")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
    if game.unit1.text_display_time and pygame.time.get_ticks() - game.unit1.text_display_time < game.unit1.text_display_time_max:
        text = game.font.render('Yes !?', True, 'white')
        SCREEN.blit(text, (game.unit1.rect.x - 4, game.unit1.rect.y - 16))
    # Screen refresh
    pygame.display.flip()
