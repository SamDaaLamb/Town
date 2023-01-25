
import pygame
from pygame import mixer

#load music
from pygame import mixer
mixer.init()
# mixer.music.load('song.wav')
# mixer.music.play(-1)

background = pygame.image.load("pics/background.png")
sm_river = pygame.transform.scale_by(pygame.image.load("pics/sm_river.png"), 5.8)
pygame.display.init()
# the size of the screen(1200,600)
screen = pygame.display.set_mode((1000, 600))
# Game name
pygame.display.set_caption("Town")
# speed
speed = 5

# variables for inventory
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
background = pygame.transform.scale(background, (2900, 2900))
# Set a clock
clock = pygame.time.Clock()
time = 0

# Stand variables

L_last = False
U_last = False
D_last = False
R_last = False

doordictionary={
    "silodoor": [[-175, -80], [- 570, -530]],
    "door1": [[-1850, -1740],[-805, -765]],
    "wizarddoor": [[-1250,-1145] ,[95, 125]],
    "pinkdoor": [[-1065, -975], [-1185, -1160]],
    "blackdoor": [[-1610, -1495], [-2170, 2140]],
    "treedoor": [[165, 245], [-2205, -2175]]

}

#                  right left        bottom   top


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

    "tree_strom": pygame.transform.scale_by(pygame.image.load("tree_storm.png"), 5.8),
    "black_house": pygame.transform.scale_by(pygame.image.load("pics/black_house.png"), 5.8),
    "bridge": pygame.transform.scale_by(pygame.image.load("pics/bridge.png"), 5.8),
    "grey_house": pygame.transform.scale_by(pygame.image.load("pics/grey_house.png"), 5.8),
    "mush_house": pygame.transform.scale_by(pygame.image.load("pics/mush_house.png"), 5.8),
    "pink_house": pygame.transform.scale_by(pygame.image.load("pics/pink_house.png"), 5.8),
    "sign": pygame.transform.scale_by(pygame.image.load("pics/sign.png"), 5.8),
    "silo_house": pygame.transform.scale_by(pygame.image.load("pics/silo_house.png"), 5.8),
    "well": pygame.transform.scale_by(pygame.image.load("pics/well.png"), 5.8),
    "treehouse": pygame.transform.scale_by(pygame.image.load("pics/treehouse.png"), 5.8),
    "f_stand": pygame.transform.scale_by(pygame.image.load("fwd-4.png"), 5.8),
    "b_stand": pygame.transform.scale_by(pygame.image.load("bwd-1.png"), 5.8),
    "5dollar": pygame.transform.scale_by(pygame.image.load("pics/5dollar.png"), 3.5),
    "apple": pygame.transform.scale_by(pygame.image.load("pics/apple.png"), 3.5),
    "blueberries": pygame.transform.scale_by(pygame.image.load("pics/blueberries.png"), 3.5),
    "bra": pygame.transform.scale_by(pygame.image.load("pics/bra.png"), 3.5),
    "fish": pygame.transform.scale_by(pygame.image.load("pics/fish.png"), 3.5),
    "fishingrod": pygame.transform.scale_by(pygame.image.load("pics/fishingrod.png"), 3.5),
    "gun": pygame.transform.scale_by(pygame.image.load("pics/gun.png"), 3.5),
    "jewel1": pygame.transform.scale_by(pygame.image.load("pics/jewel.png"), 3.5),
    "jewel2": pygame.transform.scale_by(pygame.image.load("pics/jewel2.png"), 3.5),
    "jewel3": pygame.transform.scale_by(pygame.image.load("pics/jewel3.png"), 3.5),
    "key1": pygame.transform.scale_by(pygame.image.load("pics/key1.png"), 3.5),
    "key2": pygame.transform.scale_by(pygame.image.load("pics/key2.png"), 3.5),
    "ladder": pygame.transform.scale_by(pygame.image.load("pics/ladder.png"), 3.5),
    "loveletter": pygame.transform.scale_by(pygame.image.load("pics/loveletter.png"), 3.5),
    "magicpotion": pygame.transform.scale_by(pygame.image.load("pics/magicpotion.png"), 3.5),
    "prettyflower": pygame.transform.scale_by(pygame.image.load("pics/prettyflower.png"), 3.5),
    "inventory": pygame.transform.scale_by(pygame.image.load("pics/inventory.png"), 3.5),
    "towntitle": pygame.transform.scale_by(pygame.image.load("pics/towntitle.png"), 5.6),
    "door1": pygame.transform.scale_by(pygame.image.load("pics/gamehouse1img.png"), 0.05),
    "pinkdoor": pygame.transform.scale_by(pygame.image.load("pics/pinkhouseinside.png"), 5.6),
    "silodoor": pygame.transform.scale_by(pygame.image.load("pics/silohouseinside.png"), 5.6),
    "treedoor": pygame.transform.scale_by(pygame.image.load("pics/treehouseinside.png"), 5.6),
    "blackdoor": pygame.transform.scale_by(pygame.image.load("pics/blackhouseinside.png"), 5.6),
    "wizarddoor": pygame.transform.scale_by(pygame.image.load("pics/wizardhouseinside.png"), 5.6),
    # # pygame.image.load("bush.png"),
    # pygame.image.load("tree.png"),
}

fwd_ani = [
    # pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("fwd-1.png"),5.8),
    pygame.transform.scale_by(pygame.image.load("fwd-1.png"), 5.8),
    pygame.transform.scale_by(pygame.image.load("fwd-3.png"), 5.8)
    # pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("fwd-3.png"),5.8)

]
bwd_ani = [
    # pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("bwd-2.png"),5.8),
    pygame.transform.scale_by(pygame.image.load("bwd-2.png"), 5.8),
    pygame.transform.scale_by(pygame.image.load("bwd-3.png"), 5.8)
    # pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("bwd-3.png"),5.8)
]
right_ani = [

    # pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
    pygame.transform.scale_by(pygame.image.load("right-1.png"), 5.8),
    pygame.transform.scale_by(pygame.image.load("right-2.png"), 5.8),

    pygame.transform.scale_by(pygame.image.load("right-3.png"), 5.8)
    # pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),

]

left_ani = [
    # pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("right-2.png"),5.8),
    pygame.transform.scale_by(pygame.image.load("left-1.png"), 5.8),
    pygame.transform.scale_by(pygame.image.load("left-2.png"), 5.8),
    pygame.transform.scale_by(pygame.image.load("left-3.png"), 5.8)
    # pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),
    # pygame.transform.scale_by(pygame.image.load("right-3.png"),5.8),

]

f_step = 0



# Camera Vector that we input into background and sprites.
camera = pygame.Vector2((-1890, -50))
offset = pygame.Vector2((460, 0))

print(pygame.display.get_surface())

# colour for rec testing
color1 = (255,255,0)
color = (255,0,0)
rect_values = 1

# startscreen
menuAtivo = True
title = True


# Was gonna go classless but had to make a class for bit masks

class Playa(pygame.sprite.Sprite):
    def __init__(self,image,mask,rect):

        # self.settings = settings

        self.image = image
        self.mask = mask
        self.rect = rect
        # self.Playa = self.settings





class Riva(pygame.sprite.Sprite):
    def __init__(self,image,mask,rect):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.mask = mask
        self.rect = rect


# self.mask = pygame.mask.from_surface(self.image)
# self.rect = pygame.mask.Mask.get_rect(self.mask)
def player(offset = offset):
    global L_last
    global R_last
    global D_last
    global U_last


    pressed = pygame.key.get_pressed()
    # Up diagonals
    if ((pressed[pygame.K_UP] or pressed[pygame.K_w]) or (pressed[pygame.K_DOWN] or pressed[pygame.K_s])) and (
            pressed[pygame.K_LEFT] or pressed[pygame.K_a]):
        draw_l = left_ani[f_step]

        L_last = True
        screen.blit(draw_l, (500, 300) + offset)
        play_image = draw_l

    elif ((pressed[pygame.K_UP] or pressed[pygame.K_w]) or (pressed[pygame.K_DOWN] or pressed[pygame.K_s])) and (
            pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
        draw_r = right_ani[f_step]
        R_last = True
        screen.blit(draw_r, (500, 300) + offset)  # If U See this Mr.SLater: VI VON
        play_image = draw_r

    elif pressed[pygame.K_UP] or pressed[pygame.K_w]:
        draw_b = bwd_ani[f_step]
        U_last = True
        screen.blit(draw_b, (500, 300) + offset)
        play_image = draw_b

    elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        draw_f = fwd_ani[f_step]
        D_last = True
        screen.blit(draw_f, (500, 300) + offset)
        play_image = draw_f

    elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        draw_l = left_ani[f_step]
        L_last = True
        screen.blit(draw_l, (500, 300) + offset)
        play_image = draw_l


    elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        draw_r = right_ani[f_step]
        R_last = True
        screen.blit(draw_r, (500, 300) + offset)
        play_image = draw_r
    else:
        play_image = bwd_ani[f_step]
    if not any(pressed):  # if nothing is pressed
        if L_last == True:
            screen.blit((left_ani[0]), (500, 300) + offset)
        elif R_last == True:
            screen.blit((right_ani[0]), (500, 300) + offset)
        elif D_last == True:
            screen.blit(sprites.get("f_stand"), (500, 300) + offset)
        elif U_last == True:
            screen.blit(sprites.get("b_stand"), (500, 300) + offset)
    # print((500,300)+offset)
    return play_image

# for bitmask colisoin
player_mask = pygame.mask.from_surface(player())
river_mask = pygame.mask.from_surface(sm_river)

# Functions
def startscreen(sprites_variable):
    while title:
        screen.blit(sprites.get("towntitle"), (0, 0))
        while menuAtivo:
            for evento in pygame.event.get():
                print(evento)
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos() >= (335, 415):
                        if pygame.mouse.get_pos() <= (683, 515):
                            return

            pygame.display.update()

def inside(name,l_offset):
    while True:
        event = pygame.event.get()
        for e in event:
            if e.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        screen.fill((0,0,0))
        if name == "wizarddoor":
            screen.blit(sprites.get(name), (200, 10))
        else:
            screen.blit(sprites.get(name), (285, 85))
        player(l_offset)
        pressed = pygame.key.get_pressed()
        if any(pressed):
            print(pressed)
        # can make this faster by converting if to elif.
        if False:# len(r.collidedictall(boarders, rect_values)) != 0 and b_play <= t_wall + 5:

            pass
        else:
            print("sd")
            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: l_offset += (0, speed)

        if False: # len(r.collidedictall(boarders, rect_values)) != 0 and r_play <= l_wall + 5:
            pass
        else:

            print("dfkh")
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: l_offset += (speed, 0)

        if False: #len(r.collidedictall(boarders, rect_values)) != 0 and (t_play >= b_wall - 5):
            pass
        else:


            if pressed[pygame.K_UP] or pressed[pygame.K_w]: l_offset += (0, -speed)

        if False: #len(r.collidedictall(boarders, rect_values)) != 0 and (l_play >= r_wall - 5):

            pass
        else:
            print("dsf")
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: l_offset += (-speed, 0)
        print((500, 300) + l_offset)
        pygame.display.update()


def door():
    total_cam = camera + (-offset)


    for key in doordictionary:

        if (pressed[pygame.K_e]) and (
                doordictionary[key][1][1] > total_cam[1] and doordictionary[key][1][0] < total_cam[1]) and (
                doordictionary[key][0][0] < total_cam[0] and doordictionary[key][0][1] > total_cam[0]):
            print("hello!")
            inside(key, offset)


# can make this faster by makeing it super long with just if, elif,elif
def blitty():
    screen.blit(sprites.get("tree_strom"), (camera))
    screen.blit(sprites.get("bridge"), camera + (2151.8, 1432.6))
    # screen.blit(sm_river, camera + (550, 1020))

    if camera[1] - offset[1] >215:

        player()
    screen.blit(sprites.get("well"), camera + (1815.4, 17.4))

    if camera[1] - offset[1] <=215 and camera[1] - offset[1] > 130:
        player()
    screen.blit(sprites.get("mush_house"), camera + (1502.2, 0))

    if camera[1]-offset[1] <=130 and camera[1] >-25:
        player()
    screen.blit(sprites.get("sign"), camera + (2476.6, 203))
    if camera[1] - offset[1] <= -25 and camera[1] > -460:
        player()
    screen.blit(sprites.get("silo_house"), camera + (261, 446.6))
    if camera[1] <= -460 and camera[1] > -710:
        player()
    screen.blit(sprites.get("well"), camera + (1763.2, 933.8))
    if camera[1] <= -710 and camera[1] > -755:
        player()
    screen.blit(sprites.get("grey_house"), (camera + (2146, 916.4)))
    if camera[1] <= -755 and camera[1] > -1150:
        player()
    screen.blit(sprites.get("pink_house"), camera + (1345.6, 1183))
    if camera[1] <= -1150 and camera[1] > -1755:
        player()
    screen.blit(sprites.get("well"), camera + (2279.4, 1983.6))
    if camera[1] <= -1755 and camera[1] > -2135:
        player()
    screen.blit(sprites.get("black_house"), camera + (1769, 2076.4))
    if camera[1] <= -2135 and camera[1]-offset[1] > -2165:
        player()
    screen.blit(sprites.get("treehouse"), camera + (127.6, 2088))
    if camera[1]-offset[1] <= -2165:
        player()
    # if True:
    #     player()
    screen.blit(sprites.get("inventory"), (324, 506))

startscreen(sprites)

running = True
while running:

    # Color of the screen, RGB
    print(camera - offset)
    # Camera vector
    camera_move = pygame.Vector2()


    # If step has gone thorugh all of the animation go back to start
    if f_step >= len(fwd_ani):
        f_step = -1



    # background
    screen.blit(background, (camera))



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

    s = pygame.Rect(275 + camera[0], 680 + camera[1], 200, 85)
    # -35.0 (Left Side) -400.0 - (Highest)
    # ph =  pygame.Rect(-845, 1010, 350, 150)
    ph = pygame.Rect(1375+ camera[0], 1375 + camera[1], 340, 80)
    sh = pygame.Rect(560 + camera[0], 770 + camera[1], 295, 60)
    wh = pygame.Rect(1525 + camera[0], 155 + camera[1], 255, 20)  # [-1260.0,-995.0],[125.0,215.0]],
    h1 = pygame.Rect(2160 + camera[0], 960 + camera[1], 330, 100)
    bh = pygame.Rect(1780 + camera[0],2370 + camera[1],580,70)# [-1965.0,-1635.0],[-765.0,-595.0]],
    th = pygame.Rect(260+ camera[0], 2435+camera[1], 140, 35)
    si = pygame.Rect(2480+camera[0], 325+camera[1], 270, 1)
    tw = pygame.Rect(1810 +camera[0], 85 + camera[1], 115,1)
    mw = pygame.Rect(1760 + camera[0], 1015 + camera[1], 115, 1)
    bw = pygame.Rect(2290 + camera[0], 2055 + camera[1], 105, 1)
    rr = pygame.Rect(550 + camera[0], 1020 + camera[1], 2190, 1725)

    boarders = {
        # [camera[0],camera[0]+50],[camera[1],camera[1]+80]],
        # "silo_house":sh,#[-330.0,-35.0],[-530.0,-400.0]],
        "silo": s,  # [45.0,255.0],[-470.0,-315.0]],
        "silo_house": sh,
        "wizard_house": wh,  # [-1260.0,-995.0],[125.0,215.0]],
        "pink_house": ph,  # [-1195.0,-845.0 ],[-1160.0 ,-1010.0 ]],
        "house1": h1,  # [-1965.0,-1635.0],[-765.0,-595.0]],
        "black_house": bh,  # [-1850.0,-1270.0],[-2140.0,-2030.0]],
        "tree_house": th,  # [125, 265],[-2165, -2060]],
        "sign": si,  # [-2225.0,-1955.0],[15.0,75.0]],
        "t_well": tw,  # [-1300.0,-1410.0],[205.0,245.0]],
        "m_well": mw,
        "b_well": bw  # [-1885, -1760.0],[-1765.0,-1720.0]]
    }

    # x 1.6272189349112426035502958579882
    # y 1.3613861386138613861386138613861
    r = pygame.Rect(510+offset[0], 300+offset[1], 30, 80)
    # pygame.draw.rect(screen, color1, h1)
    # pygame.draw.rect(screen, color,r)
    # pygame.draw.rect(screen, color, ph)
    # pygame.draw.rect(screen, color, sh)
    # pygame.draw.rect(screen, color1, s)
    # pygame.draw.rect(screen, color1, wh)
    # pygame.draw.rect(screen, color1, bh)
    # pygame.draw.rect(screen, color1, th)
    # pygame.draw.rect(screen, color1, si)
    # pygame.draw.rect(screen, color1, tw)
    # pygame.draw.rect(screen, color1, mw)
    # pygame.draw.rect(screen, color1, bw)
    # pygame.draw.rect(screen, color1, rr)

    if len(r.collidedictall(boarders, rect_values)) != 0:

        l_wall = r.collidedictall(boarders, rect_values)[0][1].left
        r_wall = r.collidedictall(boarders, rect_values)[0][1].right
        b_wall = r.collidedictall(boarders, rect_values)[0][1].bottom
        t_wall = r.collidedictall(boarders, rect_values)[0][1].top
    l_play = r.left
    r_play = r.right
    t_play = r.top
    b_play = r.bottom



    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    # player()

    if any(pressed):
        L_last = False
        R_last = False
        D_last = False
        U_last = False
    blitty()

    # Collisions



    # can make this faster by converting if to elif.
    if len(r.collidedictall(boarders, rect_values)) != 0 and b_play <= t_wall+5:

        pass
    else:
        if camera[1] != -2300 and offset[1] == 0:
            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: camera_move += (0, -speed)
        elif offset[1] >= -2300:
            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: offset += (0, speed)

    if len(r.collidedictall(boarders, rect_values)) != 0 and r_play <= l_wall+5:
        pass
    else:

        if camera[0] != -1890 and offset[0] == 0:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: camera_move += (-speed, 0)
        elif offset[0] >= -1890:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: offset += (speed, 0)

    if len(r.collidedictall(boarders, rect_values)) != 0 and (t_play >= b_wall-5):
        pass
    else:

        if camera[1] != 0 and offset[1] == 0:
            if pressed[pygame.K_UP] or pressed[pygame.K_w]: camera_move += (0, speed)
        elif offset[1] <= 0 or (camera[1] == -2300 and offset != 0):
            if pressed[pygame.K_UP] or pressed[pygame.K_w]: offset += (0, -speed)

    if len(r.collidedictall(boarders, rect_values)) != 0 and (l_play >= r_wall-5):

        pass
    else:
        if camera[0] != 0 and offset[0] == 0:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: camera_move += (speed, 0)
        elif offset[0] <= 0 or (camera[0] == -1890 and offset != 0):
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: offset += (-speed, 0)

    # River collision using Bit Masking cause I have a Fivehead
    # pygame.sprite.spritecollide(player(),sm_river, False, pygame.sprite.collide_mask())


    # print(cant_swim)
    camera += camera_move
    cant_swim = pygame.sprite.collide_mask(Riva(sm_river, river_mask, rr), Playa(player, player_mask, r))


    # cheap trash solution.takeing slightly to long cus my barin is slow rn
    if cant_swim:
        camera -= camera_move*2.5


    door()

    time += 1
    if time == 7:  # frame rate for animations
        time = 0
        f_step += 1
    pygame.display.update()