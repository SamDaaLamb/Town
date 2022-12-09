import pygame
running = True
pygame.display.init()
screen = pygame.display.set_mode((1000, 600))
myrectangle = pygame.Rect(50,500,900,75)
# x =
while running:
    screen.fill((250,250,50))
    pygame.draw.circle(screen, (4,5,255), (250, 250), 100)
    pygame.draw.circle(screen, (4, 5, 255), (800, 250), 100)
    pygame.draw.rect(screen, (255,0,0), myrectangle)
    # screen.blit(x,(0,0))
    pygame.display.update()