import pygame
from pygame import mixer
background = pygame.image.load("pics/background.png")
pygame.display.init()
#the size of the screen(1200,600)
screen = pygame.display.set_mode((1000, 600))

#variables for inventory
fivedollar = False
apple = False
blueberries = False
bra = False
fish = False
fishingrod = False
gun = False
jewelone = False
jeweltwo = False
jewelthree = False
keyone = False
keytwo = False
ladder = False
loveletter = False
magicpotion = False
prettyflower = False

# background
background = pygame.transform.scale(background,(2900,2900))
# Set a clock
clock = pygame.time.Clock()
time= 0

# Stand variables

L_last = False
U_last = False
D_last = False
R_last = False





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
"tree_strom": pygame.transform.scale_by(pygame.image.load("tree_storm.png"),5.8),
"black_house" : pygame.transform.scale_by(pygame.image.load("pics/black_house.png"),5.8),
"bridge" : pygame.transform.scale_by(pygame.image.load("pics/bridge.png"),5.8),
"grey_house":pygame.transform.scale_by(pygame.image.load("pics/grey_house.png"),5.8),
"mush_house": pygame.transform.scale_by(pygame.image.load("pics/mush_house.png"),5.8),
"pink_house":pygame.transform.scale_by(pygame.image.load("pics/pink_house.png"),5.8),
"sign" : pygame.transform.scale_by(pygame.image.load("pics/sign.png"),5.8),
"silo_house" : pygame.transform.scale_by(pygame.image.load("pics/silo_house.png"),5.8),
"well":pygame.transform.scale_by(pygame.image.load("pics/well.png"),5.8),
"treehouse":pygame.transform.scale_by(pygame.image.load("pics/treehouse.png"),5.8),
"f_stand":pygame.transform.scale_by(pygame.image.load("fwd-4.png"),5.8),
"b_stand":pygame.transform.scale_by(pygame.image.load("bwd-1.png"),5.8),
"5dollar" : pygame.transform.scale_by(pygame.image.load("pics/5dollar.png"), 3.5),
"apple" : pygame.transform.scale_by(pygame.image.load("pics/apple.png"), 3.5),
"blueberries" : pygame.transform.scale_by(pygame.image.load("pics/blueberries.png"), 3.5),
"bra" : pygame.transform.scale_by(pygame.image.load("pics/bra.png"), 3.5),
"fish" : pygame.transform.scale_by(pygame.image.load("pics/fish.png"), 3.5),
"fishingrod" : pygame.transform.scale_by(pygame.image.load("pics/fishingrod.png"), 3.5),
"gun" : pygame.transform.scale_by(pygame.image.load("pics/gun.png"), 3.5),
"jewel1" : pygame.transform.scale_by(pygame.image.load("pics/jewel.png"), 3.5),
"jewel2" : pygame.transform.scale_by(pygame.image.load("pics/jewel2.png"), 3.5),
"jewel3" : pygame.transform.scale_by(pygame.image.load("pics/jewel3.png"), 3.5),
"key1" : pygame.transform.scale_by(pygame.image.load("pics/key1.png"), 3.5),
"key2" : pygame.transform.scale_by(pygame.image.load("pics/key2.png"), 3.5),
"ladder" : pygame.transform.scale_by(pygame.image.load("pics/ladder.png"), 3.5),
"loveletter" : pygame.transform.scale_by(pygame.image.load("pics/loveletter.png"), 3.5),
"magicpotion" : pygame.transform.scale_by(pygame.image.load("pics/magicpotion.png"), 3.5),
"prettyflower" : pygame.transform.scale_by(pygame.image.load("pics/prettyflower.png"), 3.5),
"inventory" : pygame.transform.scale_by(pygame.image.load("pics/inventory.png"), 3.5),
# # pygame.image.load("bush.png"),
# pygame.image.load("tree.png"),
}

fwd_ani = [
# pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8)
# pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8)

]
bwd_ani =  [
# pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8)
# pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8)
]
right_ani = [

# pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
pygame.transform.scale_by(pygame.image.load("right-1.png"),5.8),
pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),

pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8)
# pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),

]

left_ani = [
# pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
pygame.transform.scale_by(pygame.image.load("left-1.png"),5.8),
pygame.transform.scale_by(pygame.image.load("left-2.png"),5.8),
pygame.transform.scale_by(pygame.image.load("left-3.png"),5.8)
# pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),
# pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),

]
f_step = 0

player = {

"fwd-2":pygame.transform.scale_by(pygame.image.load("fwd-4.png"),5.8),

}


#Camera Vector that we input into background and sprites.
camera = pygame.Vector2((0, 0))
offset = pygame.Vector2((0, 0))

print(pygame.display.get_surface())

running = True
while running:

    # Color of the screen, RGB

    # Camera vector
    camera_move = pygame.Vector2()

    # If step has gone thorugh all of the animation go back to start
    if f_step >= len(fwd_ani):

        f_step = -1





    # background
    screen.blit(background, (camera))


    screen.blit(sprites.get("tree_strom"),(camera))
    screen.blit(sprites.get("grey_house"), (camera + (2146 , 916.4)))
    screen.blit(sprites.get("pink_house"),camera+(1345.6 , 1183))
    screen.blit(sprites.get("silo_house"),camera+(261 , 446.6))
    screen.blit(sprites.get("treehouse"),camera+(127.6, 2088))
    screen.blit(sprites.get("mush_house"),camera+(1502.2, 0))
    screen.blit(sprites.get("black_house"),camera+(1769, 2076.4))
    screen.blit(sprites.get("bridge"),camera+(2151.8, 1432.6))
    screen.blit(sprites.get("sign"),camera+(2476.6, 203))
    screen.blit(sprites.get("well"),camera+(1815.4 , 17.4))
    screen.blit(sprites.get("well"),camera+(2279.4 , 1983.6))
    screen.blit(sprites.get("well"),camera+(1763.2, 933.8))
    screen.blit(sprites.get("inventory"), (324, 506))
    if blueberries:
        screen.blit(sprites.get("blueberries"), (324, 506))
    if fivedollar:
        screen.blit(sprites.get("5dollar"), (324, 506))
    if gun:
        screen.blit(sprites.get("gun"), (324, 506))
    if apple:
        screen.blit(sprites.get("apple"), (644, 506))
    if loveletter:
        screen.blit(sprites.get("loveletter"), (564, 506))
    if magicpotion:
        screen.blit(sprites.get("magicpotion"), (564, 506))
    if keytwo:
        screen.blit(sprites.get("key2"), (564, 506))
    if fishingrod:
        screen.blit(sprites.get("fishingrod"), (404, 506))
    if fish:
        screen.blit(sprites.get("fish"), (404, 506))
    if ladder:
        screen.blit(sprites.get("ladder"), (404, 506))
    if jewelone:
        screen.blit(sprites.get("jewel1"), (404, 506))
    if jeweltwo:
        screen.blit(sprites.get("jewel2"), (484, 506))
    if jewelthree:
        screen.blit(sprites.get("jewel3"), (644, 506))
    if keyone:
        screen.blit(sprites.get("key1"), (484, 506))
    if keytwo:
        screen.blit(sprites.get("key2"), (564, 506))
    if ladder:
        screen.blit(sprites.get("ladder"), (404, 506))
    if prettyflower:
        screen.blit(sprites.get("prettyflower"), (564, 506))


    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False





    pressed = pygame.key.get_pressed()
    if not any(pressed):#if nothing is pressed
        if L_last == True:
            screen.blit((left_ani[0]), (500, 300)+offset)
        elif R_last == True:
            screen.blit((right_ani[0]), (500, 300)+offset)
        elif D_last == True:
            screen.blit(sprites.get("f_stand"), (500, 300)+offset)
        elif U_last == True:
            screen.blit(sprites.get("b_stand"), (500, 300) + offset)
    elif any(pressed):
        L_last = False
        R_last = False
        D_last = False
        U_last = False


    #Up diagonals
    if ((pressed[pygame.K_UP] or pressed[pygame.K_w])or (pressed[pygame.K_DOWN] or pressed[pygame.K_s])) and (pressed[pygame.K_LEFT] or pressed[pygame.K_a]):
        draw_l = left_ani[f_step]

        L_last = True
        screen.blit(draw_l, (500, 300)+offset)

    elif ((pressed[pygame.K_UP] or pressed[pygame.K_w]) or (pressed[pygame.K_DOWN] or pressed[pygame.K_s])) and (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
        draw_r = right_ani[f_step]
        R_last = True
        screen.blit(draw_r, (500, 300)+offset) #If U See this Mr.SLater: VI VON

    elif pressed[pygame.K_UP] or pressed[pygame.K_w]:
        draw_b = bwd_ani[f_step]
        U_last = True
        screen.blit(draw_b, (500, 300)+offset)
    elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        draw_f = fwd_ani[f_step]
        D_last = True
        screen.blit(draw_f, (500, 300)+offset)

    elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        draw_l = left_ani[f_step]
        L_last = True
        screen.blit(draw_l, (500, 300)+offset)


    elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        draw_r = right_ani[f_step]
        R_last = True
        screen.blit(draw_r, (500, 300)+offset)
    # Character
    #     if pressed[pygame.]
    #     if pressed[pygame.K_UP] or pressed[pygame.K_w]:
    if camera[1] != -2300 and offset[1] == 0:
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: camera_move += (0, -5)
    elif offset[1] >= -2300:
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: offset += (0, 5)
        if offset[1] != 0:
            if pressed[pygame.K_UP] or pressed[pygame.K_w]: offset += (0, -5)

    if camera[0] != -1890 and offset[0] == 0:
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: camera_move += (-5, 0)
    elif offset[0] >= -1890:
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: offset += (5, 0)
        if offset[0] != 0:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: offset += (-5, 0)

    if camera[1] != 0 and offset[1] == 0:
        if pressed[pygame.K_UP] or pressed[pygame.K_w]: camera_move += (0, 5)
    elif offset[1] <= 0:
        if pressed[pygame.K_UP] or pressed[pygame.K_w]: offset += (0, -5)
        if offset[1] != 0:
            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: offset += (0, 5)


    if camera[0] != 0 and offset[0] == 0:
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: camera_move += (5, 0)
    elif offset[0] <= 0:
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a] : offset += (-5, 0)
        if offset[0] != 0:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: offset += (5, 0)


    camera += camera_move

    print(offset)
    time+=1
    if time == 7:#frame rate for animations
        time=0
        f_step += 1
    pygame.display.update()
