import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing ball game")

WHITE = (255,255,255)
BLACK = (0, 0, 0)
BALL_COLOR = (0, 200, 255)
PADDLE_COLOR = (255,100,0)


BALL_RADIUS = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5* random.choice([-1,1])
ball_speed_y = 5* random.choice([-1,1])

PADDLE_WIDTH = 160
PADDLE_HEIGHT = 20
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - 40
paddle_speed = 8

score = 0
font = pygame.font.SysFont(None,36)
clock = pygame.time.Clock()

def draw():
    screen.fill(BLACK)
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10,10))
    pygame.display.flip()
    
def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 5* random.choice([-1,1])
    ball_speed_y = 5* random.choice([-1,1])
    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += paddle_speed
    
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_speed_x *= -1
    if ball_y - BALL_RADIUS <= 0:
        ball_speed_y *= -1
    if (paddle_y < ball_y + BALL_RADIUS < paddle_y + PADDLE_HEIGHT and
        paddle_x < ball_x < paddle_x + PADDLE_WIDTH and
        ball_speed_y > 0 ):
        ball_speed_y *= -1
        score += 1
        
    if ball_y - BALL_RADIUS > HEIGHT:
        score = 0
        reset_ball()
        
    draw()
    clock.tick(60)
    
pygame.quit()
sys.exit()