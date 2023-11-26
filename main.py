import pygame, sys
from settings import *


# Create the Game class
class Game:
# Initialize the Game class
    def __init__(self):
        """
        Initialize the Game class.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Custom Dune II")
        self.clock = pygame.time.Clock()

# Run the game loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill("black")
            pygame.display.update()
            self.clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
            
