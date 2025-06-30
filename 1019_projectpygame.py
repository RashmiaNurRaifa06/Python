import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 48

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the red block")
font = pygame.font.SysFont("Arial", FONT_SIZE)
clock = pygame.time.Clock()

# New: List of colors for the target to cycle through
TARGET_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 0, 128)] # Red, Green, Blue, Yellow, Cyan, Magenta, Purple

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.set_color(color) # Use set_color for initial coloring
        
    def set_color(self, new_color):
        self.color = new_color
        pygame.draw.rect(self.image, self.color, self.image.get_rect())
        
    def move(self,x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        
    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        
def create_game_objects():
    player = Sprite(pygame.Color('blue'), 30, 30)
    player.reset_position()
    # Initialize target with a random color
    target = Sprite(random.choice(TARGET_COLORS), 30, 30)
    target.reset_position()
    return player, target

player, target = create_game_objects()
score = 0
running, won = True, False

while running:
    screen.fill(pygame.Color('lightgray'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and won and event.key == pygame.K_r:
            player, target = create_game_objects()
            score = 0
            won = False
            
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        player.move(x_change, y_change)
        
        if player.rect.colliderect(target.rect):
            score += 1
            target.reset_position()
            target.set_color(random.choice(TARGET_COLORS)) # New: Change target color on collision
            if score >= 20:
                won = True
                
    screen.blit(player.image, player.rect)
    if not won or pygame.time.get_ticks() % 400 < 200:
        screen.blit(target.image, target.rect)
        
    score_text = font.render(f"Score: {score}", True, pygame.Color('black'))
    screen.blit(score_text, (20,20))
    
    if won:
        win_text = font.render("You win!", True, pygame.Color('green'))
        retry_text = pygame.font.SysFont("Arial", 28).render("Press R to restart", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 40))
        screen.blit(retry_text, ((SCREEN_WIDTH - retry_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 10))
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
