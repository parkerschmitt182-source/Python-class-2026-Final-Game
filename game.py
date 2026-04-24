import pygame, sys
from pygame.locals import *
import time
pygame.init()
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
loadred = pygame.image.load("bigred.png")
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
speed = 2
def text(text2, x, y):
    my_font = pygame.font.SysFont('Arial', 30)
    text_surface = my_font.render(text2, True, colorBlack)

    screen.blit(text_surface, (x, y))
while Running==True:
    screen.fill(colorBlack)
    QB1 = pygame.image.load("background.jpeg")
    QB1 = pygame.transform.scale(QB1, (screen.get_width(), screen.get_height()))
    screen.blit(QB1,(0,0),(0,0,screen.get_width(),screen.get_height()))
    key = pygame.key.get_pressed()
    text("helllo", 50,50)
    text("helllo", 50,100)
    if key[pygame.K_LEFT]:
        playerX -= speed
        imagerow = 0
        imageswitch +=1
        if imageswitch == 10:
            imageswitch =0
            imagenum+=1
        if imagenum == 3:
            imagenum = 0
    if key[pygame.K_RIGHT]:
        playerX += speed
        imagerow = 1
        imageswitch +=1
        if imageswitch == 10:
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
    screen.blit(loadred, (100, 200))
    levelone = pygame.Rect((100,200,150,150))
    playerRect = pygame.Rect((playerX,playerY,playerW,playerH))
    screen.blit(loadimage, (playerX, playerY), (image, imageY,132,172))

    pygame.display.update()
    if playerRect.colliderect(levelone):
        print("levelone")
        if key[pygame.K_RETURN]:
             Running = False
    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False
    if key[pygame.K_ESCAPE]:
        Running = False



pygame.quit()





import Levelone




sys.exit()
