import pygame, random
pygame.init()


WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch the Falling Objects!")

BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

player_rect=pygame.Rect((WIDTH-100)//2,HEIGHT-30,100,20)
player_speed=7
objects=[]
score=0
font=pygame.font.Font(None,36)
clock=pygame.time.Clock()


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left>0:player_rect.x-=player_speed
    if keys[pygame.K_RIGHT] and player_rect.right<WIDTH:player_rect.x+=player_speed
    if random.randint(1,100)<2: # This line controls the frequency of falling objects
        objects.append({'rect':pygame.Rect(random.randint(0,WIDTH-30),0,30,30),'color':GREEN})
    
    
    for obj in objects[:]:
        obj['rect'].y+=5
        if player_rect.colliderect(obj['rect']):
            score+=1
            objects.remove(obj)
        elif obj['rect'].top>HEIGHT:
            score-=1
            objects.remove(obj)
    
    
    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE,player_rect)
    
    
    for obj in objects:pygame.draw.rect(screen,obj['color'],obj['rect'])
    screen.blit(font.render(f"Score: {score}",True,WHITE),(10,10))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()