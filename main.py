import pygame, os, sys

pygame.init()
clock = pygame.time.Clock()

# Screen Settings
screenWidth, screenHeight = 500, 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Scrolling Background")

# Setting up Dir
dir_name = os.path.dirname(__file__)
file_dir = os.path.join(dir_name, "background.png")

# Screen refresh color
black = pygame.Color(0, 0, 0)


class BG:
    objs = []
    scroll_Speed = 2

    def __init__(self, x):
        # Background starting paramiters
        self.image = pygame.image.load(file_dir)
        self.rect = self.image.get_rect()
        self.rect.topleft = x, 0
        # Appends the new instance to objs
        BG.objs.append(self)
    
    @classmethod
    def update(cls):
        # This grabs the newest instance in the objs list
        cls.newest_instance = BG.objs[-1]
        # This gets newest instance x position
        cls.spawn_x = cls.newest_instance.rect.x + 500
        
        for obj in cls.objs:
            # Automatically scrolls background
            obj.rect.x -= BG.scroll_Speed
            
            # What happens if a background tile gets far enough of scree
            if obj.rect.x <= -1000:
                # Creates a new background instance at the newest's instance's x pos
                b_list.append(BG(BG.spawn_x))
                # Removes the background instance that triggered the function for optimization
                b_list.remove(obj)
                BG.objs.remove(obj)
            # Draws the background instance.
            screen.blit(obj.image, obj.rect)
            
# Sets up the first 3 background images and will be used to create new instances.
b_list = [BG(0), BG(500), BG(1000)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(black)
    
    BG.update()
    
    pygame.display.flip()
    clock.tick(60)