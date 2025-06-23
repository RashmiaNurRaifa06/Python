import pygame

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Circle")

RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.draw.circle(screen, RED, (300, 200), 50)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()