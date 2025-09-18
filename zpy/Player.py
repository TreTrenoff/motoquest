import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("./lib/img/player/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        # Rectangle de collision
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        # Vitesse du joueur
        self.speed = 5
