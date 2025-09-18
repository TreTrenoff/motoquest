import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Template Pygame")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu ici

    # Dessin
    screen.fill(WHITE)
    # Ajoutez vos dessins ici

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()