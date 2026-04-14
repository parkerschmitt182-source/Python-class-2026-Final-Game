import pygame,random,math
from pygame.locals import *
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont(None, 40)

BLUE = (0,0,255)
DARKBLUE = (0,71,171)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
PEACH = (255,176,156)

gameLoop = True
playerSpeed = 1
grounded = False
fallSpeed = 9

tilemap = [
    'B','_','_','_',
    '_','_','_','_',
    '_','_','_','_',
    '_','_','_','B',
    ]

FPS = 100
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 1000),pygame.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
mousePos = pygame.mouse.get_pos()
offset = pygame.math.Vector2(0,0)
world = pygame.math.Vector2(w/2,h/2)
playerRect = pygame.Rect(w/2,h/2,100,100)
ground = pygame.Rect(world.x,world.y+100,1000,100)
def handleInputs():
    global gameLoop,boost,world,acceptingNewVector,inRange
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        offset.y += playerSpeed
    if keys[pygame.K_s]:
        offset.y -= playerSpeed
    if keys[pygame.K_a]:
        offset.x += playerSpeed
    if keys[pygame.K_d]:
        offset.x -= playerSpeed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameLoop = False

def draw():
    
    #screen.blit(soulImage,(playerRect.centerx-soulImageSize/2,playerRect.centery-soulImageSize/2),(soulImageX,0,soulImageStep,soulImageH))
    #pygame.draw.rect(screen, (DARKBLUE), (world.x,world.y,100,100),1,5)
    
    
    pygame.draw.rect(screen, (GREEN), ground, 0, 5)
    pygame.draw.rect(screen, ('orange'), (playerRect),0,5)
    
def collidePlayer(self,player):
    global offset,grounded,mousePos,inRange
    if self.contains(mousePos,(1,1)):
        inRange = True
    if self.colliderect(player):
        leftOverlap = player.right - self.left
        rightOverlap = self.right - player.left
        topOverlap = player.bottom - self.top
        bottomOverlap = self.bottom - player.top
        min_overlap = min(leftOverlap, rightOverlap, topOverlap, bottomOverlap)#Which of these overlaps is smallest?
        if min_overlap == topOverlap:
            offset.y += topOverlap
            grounded = True
        elif min_overlap == bottomOverlap:
            offset.y -= bottomOverlap
        elif min_overlap == leftOverlap:
            offset.x += leftOverlap
        elif min_overlap == rightOverlap:
            offset.x -= rightOverlap
def gravity():
    grounded = False
    if grounded == False:
        offset.y-=fallSpeed

while gameLoop:
    mousePos = pygame.mouse.get_pos()
    gravity()
    handleInputs()
    w, h = pygame.display.get_surface().get_size()
    playerRect = pygame.Rect(w/2-playerRect.w/2,h/2-playerRect.h/2,100,100)
    world = pygame.Vector2(playerRect.x+offset.x,playerRect.y+offset.y)
    ground = pygame.Rect(world.x- 100,world.y+150,800,200)
    
    collidePlayer(ground,playerRect)
    screen.fill(BLACK)
    
    clock.tick(FPS)
    draw()
    pygame.display.flip()
    

pygame.quit()
