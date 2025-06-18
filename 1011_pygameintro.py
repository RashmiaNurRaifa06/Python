import pygame 

pygame.init()

screen = pygame.display.set_mode((500,500))

font = pygame.font.SysFont(None,48)
text = font.render('Codingal', True, (255,255,255))
text_rect = text.get_rect(center = (250,250))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill((0,0,0))
    screen.blit(text,text_rect)
    pygame.display.flip()
    
pygame.quit()