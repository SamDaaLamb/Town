import pygame
from pygame import mixer
background = pygame.image.load("pics/background.png")
pygame.display.init()
#the size of the screen(1200,600)
screen = pygame.display.set_mode((1000, 600))
running = True

background = pygame.transform.scale(background,(2900,2900))

sprites = {
# pygame.image.load("tree_storm.png"),
# pygame.image.load("pics/black_house.png"),
# pygame.image.load("pics/bridge.png"),
# pygame.image.load("pics/grey_house.png"),
# pygame.image.load("pics/mush_house.png"),
# pygame.image.load("pics/pink_house.png"),
# pygame.image.load("pics/sign.png"),
# pygame.image.load("pics/silo_house.png"),
# pygame.image.load("pics/well.png"),
# pygame.image.load("pics/treehouse.png")
"tree_strom ": pygame.transform.scale_by(pygame.image.load("tree_storm.png"),5.8),
"black_house" : pygame.transform.scale_by(pygame.image.load("pics/black_house.png"),5.8),
"bridge" : pygame.transform.scale_by(pygame.image.load("pics/bridge.png"),3),
"grey_house":pygame.transform.scale_by(pygame.image.load("pics/grey_house.png"),5.8),
"mush_house": pygame.transform.scale_by(pygame.image.load("pics/mush_house.png"),5.8),
"pink_house":pygame.transform.scale_by(pygame.image.load("pics/pink_house.png"),5.8),
"sign" : pygame.transform.scale_by(pygame.image.load("pics/sign.png"),5.8),
"silo_house" : pygame.transform.scale_by(pygame.image.load("pics/silo_house.png"),5.8),
"well":pygame.transform.scale_by(pygame.image.load("pics/well.png"),5.8),
"treehouse":pygame.transform.scale_by(pygame.image.load("pics/treehouse.png"),5.8)
# # pygame.image.load("bush.png"),
# pygame.image.load("tree.png"),
}

player = {
"fwd-1":pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
"fwd-2":pygame.transform.scale_by(pygame.image.load("fwd-2.png"),5.8),
"fwd-3":pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8),

"bwd-1":pygame.transform.scale_by(pygame.image.load("bwd-1.png"),5.8),
"bwd-2":pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
"bwd-3":pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8),

"right-1":pygame.transform.scale_by(pygame.image.load("right-1.png"),5.8),
"right-2":pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
"right-3":pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),

"left-1":pygame.transform.scale_by(pygame.image.load("left-1.png"),5.8),
"left-2":pygame.transform.scale_by(pygame.image.load("left-2.png"),5.8),
"left-3":pygame.transform.scale_by(pygame.image.load("left-3.png"),5.8)
}


#Camera Vector that we input into background and sprites.
camera = pygame.Vector2((0, 0))
print(pygame.display.get_surface())

while running:
    # Color of the screen, RGB

    camera_move = pygame.Vector2()
    # backgroung
    screen.blit(background, (camera))
    for k,v in sprites.items():
        if k == "grey_house":
            screen.blit(v,(camera + (2146 , 916.4)))
        if k == "pink_house":
            screen.blit(v,(camera+(1345.6 , 1183)))
        if k == "silo_house":
            screen.blit(v,(camera+(261 , 446.6)))
        if k == "treehouse":
            screen.blit(v,(camera+(127.6, 2088)))
        if k == "mush_house":
            screen.blit(v,(camera+(1502.2, 0)))
        if k == "black_house":
            screen.blit(v,(camera+(1769, 2076.4)))
    print(camera)
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False



    pressed = pygame.key.get_pressed()

    if not any(pressed):
        screen.blit(player.get("fwd-2"), ((500, 300)))

    # Character
    #     if pressed[pygame.]
    #     if pressed[pygame.K_UP] or pressed[pygame.K_w]:
    if camera[1] != 0:
        if pressed[pygame.K_UP] or pressed[pygame.K_w] : camera_move += (0, 5)


    if camera[0] != 0:
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: camera_move += (5, 0)
    if camera[1] != -2300:
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: camera_move += (0, -5)
    if camera[0] != -1890:
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: camera_move += (-5, 0)
    camera += camera_move
    pygame.display.update()
