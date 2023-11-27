import pygame

# Map generator
class Map:
    def __init__(self, name="map1", size=(640, 480), tilesize=16):
        self.name = name
        self.size = size
        self.tilesize = tilesize
        self.x_max = self.size[0] // self.tilesize
        self.y_max = self.size[1] // self.tilesize
        self.tile1 = '../assets/sand01.bmp'
        self.tile2 = '../assets/rock01.bmp'
        self.tile3 = '../assets/mount01.bmp'
        self.tile4 = '../assets/spice01.bmp'
        self.map_surface = pygame.Surface(size)
    
    def add_tile(self, tile_number, x, y):
        if x > self.x_max or y > self.y_max or x < 0 or y < 0:
            print("x or y is out of range")
        else:
            tile = pygame.image.load(tile_number)
            self.map_surface.blit(tile, (x * self.tilesize, y * self.tilesize))
    
    def export(self,):
        name = self.name
        pygame.image.save(self.map_surface, name + '.bmp')
        
    def generate(self,):
        self.add_tile(self.tile1, 0, 0)
        self.add_tile(self.tile2, 1, 0)
        self.add_tile(self.tile3, 2, 0)
        self.add_tile(self.tile4, 3, 0)
        self.export()
    
map = Map()
map.generate()
