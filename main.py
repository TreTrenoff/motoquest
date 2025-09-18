import pygame
import sys

from zpy.Color import Color
from zpy.Player import Player

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MotoQuest")

player = Player(100, 100)
all_sprites = pygame.sprite.Group(player)

# Boucle principale
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu ici
    all_sprites.update()

    # Dessin
    screen.fill(Color.WHITE)
    # Ajoutez vos dessins ici
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()