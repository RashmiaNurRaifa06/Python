import pygame
import random

pygame.init()

WIDTH, HEIGHT  = 600,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color changing sprite game")

class ColorSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 65
        self.image = pygame.Surface((self.size, self.size))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = (WIDTH //2, HEIGHT //2))
       
        self.vx = random.choice([-3, 3])
        self.vy = random.choice([-3, 3])
    
    def random_color(self):
        return (random.randint(50,255), random.randint(50,255), random.randint(50,255) )
    
    def update(self):
        self.image.fill(self.color)
        
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx = -self.vx
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy = -self.vy
            
    def change_color(self):
        self.color = self.random_color()
        
    def move(self, dx, dy):
        self.rect.x = dx
        self.rect.y = dy
        self.rect.clamp_ip(screen.get_rect())
        
sprite = ColorSprite()
sprites = pygame.sprite.Group(sprite)

clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont(None,32)
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite.rect.collidepoint(event.pos):
                sprite.change_color()
                score += 1
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        sprite.move(5, -0)
    if keys[pygame.K_UP]:
        sprite.move(-0, 5)
    if keys[pygame.K_DOWN]:
        sprite.move(0, -5)
    
    sprites.update()
    
    screen.fill((30, 30, 30))
    sprites.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()