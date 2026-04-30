astilines = [
"In both the Eucharistic",
"miracles of Asti from the",
"consecrated Host gushed",
"out real blood and there are",
"numerous documents that",
"confirm these events. In the",
"first miracle, Mons. Scipione",
"Roero had a notary act",
"drawn up and Pope Paul III",
"on November 6, 1535",
"granted a plenary indulgence",
"to anyone who visited the",
"Church of San Secondo on",
"the anniversary of the",
"miraculous event"
]
alatrilines = [
"In Alatri's Cathedral of",
"Saint Paul the Apostle is kept",
"even today the reliquary",
"of the Eucharistic miracle",
"that occurred in 1228 and",
"consisted in a fragment of",
"the Host turning into flesh.",
"A young woman, in an effort",
"to regain the love of her",
"sweetheart, consulted a",
"sorceress who ordered her",
"to steal a consecrated Host to",
"make a love potion. During",
"Mass, the young woman hid",
"a Host in a cloth. But when",
"she got home, she realized",
"that the Host had been",
"transformed into bleeding flesh.",
"This miracle has extensive",
"documentation, including",
"from Pope Gregory IX."
]


import pygame, sys
from pygame.locals import *
import time
pygame.init()
import pygame
pygame.mixer.init()
boot = pygame.mixer.Sound("boot.mp3")
stepsound = pygame.mixer.Sound("step.mp3")
boot.play()
import pygame
from pygame.locals import *
from pygame import mixer
levelstart = 0
screenW = 1000
screenH = 1000
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('myGame')
playerX = screenW/2
playerY = screenH/2
playerW = 50
playerH = 50
colorBlack = (0,0,0)
colorRed = (255,0,0)
loadimage = pygame.image.load("spite.png")
asti = pygame.image.load("asti.png")
alatri = pygame.image.load("alatri.png")
imageW = 1148
numberOfImages = 8
step = imageW/numberOfImages
imageH = 172
imageX = 0
imageY = 0 
imageswitch = 0
counter = 0
Running = True
imagenum = 0
animation = 0
imagerow = 0
speed = 5
menuenabled = 0
def text(text2, x, y, size):
    my_font = pygame.font.SysFont('Arial', size)
    text_surface = my_font.render(text2, True, 'white')

    screen.blit(text_surface, (x, y))

def Menu(level):

    if levelname == "Asti":
        pygame.draw.rect(screen, (157, 171, 191), (10, 50, 270, 400), border_radius=15)
        text(level, 20,60,30)
        text(levelname, 20,90, 30)
        middle = 20
        height = 120
        line = 0
        for i in range (len(astilines)):
            text(astilines[line], middle, height, 20)
            height += 20
            line +=1
    if levelname == "Alatri":
        pygame.draw.rect(screen, (157, 171, 191), (10, 50, 290, 500), border_radius=15)
        text(level, 20,60,30)
        text(levelname, 20,90, 30)

        middle = 20
        height = 120
        line = 0
        for i in range (len(alatrilines)):
            text(alatrilines[line], middle, height, 20)
            height += 20
            line +=1

showtut = True
def tutorial():
    widthtut = 250
    heighttut = 150
    middle = screen.get_width() /2 - widthtut/2

    pygame.draw.rect(screen, (157, 171, 191), (middle, 10, widthtut, heighttut), border_radius=15)
    middle +=10
    text("Tuturial", middle,20,30)
    text("Arrow Keys To Move", middle,50, 20)
    text("Space to shoot", middle,70, 20)
    text("Enter to enter Level", middle,90, 20)
    text("Get to the end of the level", middle,110, 20)
    text("Press E to exit Tutorial", middle,130, 10)




screen.fill(colorBlack)
middle = screen.get_width() /2
text("PHOTOGRAPH: Eurcharistic Miracles", 75, 50, 50)
pygame.display.update()
loadw = 1
for i in range (100):
    loadw += 5
    pygame.draw.rect(screen, (255, 255, 255), (250, 150, 500, 5), border_radius=15)
    pygame.draw.rect(screen, (0, 255, 0), (250, 150, loadw, 5), border_radius=15)

    pygame.display.update()
    time.sleep(.01)
mixer.init()
mixer.music.load('Menu.mp3')
mixer.music.play()




while Running==True:

    screen.fill(colorBlack)
    QB1 = pygame.image.load("background.jpeg")
    QB1 = pygame.transform.scale(QB1, (screen.get_width(), screen.get_height()))
    screen.blit(QB1,(0,0),(0,0,screen.get_width(),screen.get_height()))
    key = pygame.key.get_pressed()
    if showtut:
        tutorial()
    if menuenabled == 1:
        levelname = "Asti"
        Menu("Level 1")
    if menuenabled == 2:
        levelname = "Alatri"
        Menu("Level 2")

    if key[pygame.K_e]:
         showtut = False
    if key[pygame.K_LEFT]:
        playerX -= speed
        imagerow = 0
        imageswitch +=1
        if imageswitch == 10:
            stepsound.play()
            imageswitch =0
            imagenum+=1
        if imagenum == 3:
            imagenum = 0
    if key[pygame.K_RIGHT]:
        playerX += speed
        imagerow = 1
        imageswitch +=1
        if imageswitch == 10:
            stepsound.play()
            imageswitch =0
            imagenum+=1
        if imagenum == 3:
            imagenum = 0
    if key[pygame.K_UP]:
        playerY -= speed
    if key[pygame.K_DOWN]:
        playerY += speed
    if playerX<0:
        playerX=0
    if playerY<0:
        playerY = 0
    if playerX >screenW-playerW:
        playerX=screenW-playerW
    if playerY > screenH-playerH:
        playerY=screenH-playerH
    image = 132 * imagenum
    imageY = 172 * imagerow
    screen.blit(asti, (500, 200))
    screen.blit(alatri, (200, 200))
    levelone = pygame.Rect((500,200,150,150))
    leveltwo = pygame.Rect((200,200,150,150))
    playerRect = pygame.Rect((playerX,playerY,playerW,playerH))
    screen.blit(loadimage, (playerX, playerY), (image, imageY,132,172))

    pygame.display.update()
    menuenabled = 0
    if playerRect.colliderect(levelone):
        print("levelone")
        menuenabled = 1
        if key[pygame.K_RETURN]:
             Running = False
             levelstart = 1
    if playerRect.colliderect(leveltwo):
        print("leveltwo")
        menuenabled = 2
        if key[pygame.K_RETURN]:
             Running = False
             levelstart = 2
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
    if key[pygame.K_ESCAPE]:
        Running = False



#pygame.quit()




if levelstart == (1):

    import Levelone




sys.exit()
