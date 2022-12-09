import pygame
from pygame import mixer
background = pygame.image.load("pics/background.png")
pygame.display.init()
#the size of the screen(1200,600)
screen = pygame.display.set_mode((1000, 600))
running = True
pygame.display.init()
background = pygame.transform.scale(background,(2900,2900))

sprites = [

pygame.image.load("pics/black_house.png"),
pygame.image.load("pics/bridge.png"),
pygame.image.load("pics/bush.png"),
pygame.image.load("pics/grey_house.png"),
pygame.image.load("pics/mush_house.png"),
pygame.image.load("pics/pink_house.png"),
pygame.image.load("pics/river.png"),
pygame.image.load("pics/sign.png"),
pygame.image.load("pics/silo_house.png"),
pygame.image.load("pics/tree.png"),
pygame.image.load("pics/tree_wall.png"),
pygame.image.load("pics/well.png")


]


#Camera Vector that we input into background and sprites.
camera = pygame.Vector2((0, 0))
print(pygame.display.get_surface())
camera_move = pygame.Vector2()
while running:
    # Color of the screen, RGB





    # backgroung
    screen.blit(background, (camera))
    print(camera)
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: camera_move += (0, 1)
    if pressed[pygame.K_LEFT]: camera_move += (1, 0)
    if pressed[pygame.K_DOWN]: camera_move += (0, -1)
    if pressed[pygame.K_RIGHT]: camera_move += (-1, 0)
    camera += camera_move
    pygame.display.update()