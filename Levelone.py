import pygame,random,math
from pygame.locals import *
from pygame.math import Vector2
import time
pygame.init()
facing = "left"
pygame.mixer.init()
bulletspeed = 60
#defining sounds
lazer = pygame.mixer.Sound("lazer.mp3")
font = pygame.font.SysFont(None, 40)
enimynum =1
BLUE = (0,0,255)
DARKBLUE = (0,71,171)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
PEACH = (255,176,156)
touchingground = False
gameLoop = True
playerSpeed = 10
grounded = False
fallSpeed = 20
imagenum = 1
imagerow = 0
momentumX = 0
momentumY = 0
bulletx = 350
alive = True
bullety = 250
shot = False
#grass = pygame.image.load("grass.png")
dirt = pygame.image.load("dirt.png")
enimy = pygame.image.load("enimy.png")
church = pygame.image.load("church.png")
#brimstone = pygame.image.load("brimstone.png")
#lavarock = pygame.image.load("lavarock.png")
#laceration = pygame.image.load("laceration.png")
#weakness= pygame.image.load("weakness.png")
imageswitch = 0
boost = 10
boostVector = (0,0)
acceptingNewVector = True
inRange=False

reticle = pygame.Rect(0,0,0,0)

FPS = 100
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 1000),pygame.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
mousePos = pygame.mouse.get_pos()
offset = pygame.math.Vector2(0,0)
world = pygame.math.Vector2(w/2,h/2)
playerRect = pygame.Rect(w/2,h/2,100,100)
playerFeet = playerRect
ground = pygame.Rect(world.x,world.y+100,1000,100)
class Church:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color
    def draw(self):
        global church
        church = pygame.transform.scale(church,self.size)
        screen.blit(church,block)
        #pygame.draw.rect(screen, (BLUE), self.rect, 0, 0)

    def collide(self,player):
        global offset,grounded,mousePos,fallSpeed,momentumY,boost,reticle

        if self.rect.colliderect(player):
            leftOverlap = player.right - self.rect.left
            rightOverlap = self.rect.right - player.left
            topOverlap = player.bottom - self.rect.top
            bottomOverlap = self.rect.bottom - player.top
            min_overlap = min(leftOverlap, rightOverlap, topOverlap, bottomOverlap)#Which of these overlaps is smallest?

            if min_overlap == topOverlap:
                momentumY=0
                offset.y += topOverlap

            elif min_overlap == bottomOverlap:
                momentumY=0
                offset.y -= bottomOverlap
                boost=0

            elif min_overlap == leftOverlap:
                offset.x += leftOverlap
            elif min_overlap == rightOverlap:
                offset.x -= rightOverlap
class Finish:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color
    def draw(self):
        global enimy,alive
        if alive:
            self.rect.topleft = (self.position.x + offset.x, self.position.y + offset.y)
            image = pygame.transform.scale(church, self.size)
            screen.blit(image, self.rect)
        #pygame.draw.rect(screen, (BLUE), self.rect, 0, 0)

    def collide(self,player):
        global offset,grounded,mousePos,fallSpeed,momentumY,boost,reticle,bullethit,alive

        if self.rect.colliderect(player):
            print("hit")
class Enimy:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color
    def draw(self):
        global enimy,alive
        if alive:
            self.rect.topleft = (self.position.x + offset.x, self.position.y + offset.y)
            image = pygame.transform.scale(enimy, self.size)
            screen.blit(image, self.rect)
        #pygame.draw.rect(screen, (BLUE), self.rect, 0, 0)

    def collide(self,player):
        global offset,grounded,mousePos,fallSpeed,momentumY,boost,reticle,bullethit,alive

        if self.rect.colliderect(player):
            print("hit")

            #alive = False
            #leftOverlap = player.right - self.rect.left
            #rightOverlap = self.rect.right - player.left
            #topOverlap = player.bottom - self.rect.top
            #bottomOverlap = self.rect.bottom - player.top
            #min_overlap = min(leftOverlap, rightOverlap, topOverlap, bottomOverlap)#Which of these overlaps is smallest?

            #if min_overlap == topOverlap:
                #momentumY=0
                #offset.y += topOverlap

            #elif min_overlap == bottomOverlap:
                #momentumY=0
                #offset.y -= bottomOverlap
                #boost=0

            #elif min_overlap == leftOverlap:
                #offset.x += leftOverlap
            #elif min_overlap == rightOverlap:
                #offset.x -= rightOverlap
class Block:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color
    def draw(self):
        global dirt
        self.rect.topleft = (self.position.x + offset.x, self.position.y + offset.y)
        image = pygame.transform.scale(dirt, self.size)
        screen.blit(image, self.rect)
        #pygame.draw.rect(screen, (BLUE), self.rect, 0, 0)
        
    def collide(self,player):
        global offset,grounded,mousePos,fallSpeed,momentumY,boost,reticle,touchingground
            
        if self.rect.colliderect(player):
            touchingground = True

            leftOverlap = player.right - self.rect.left
            rightOverlap = self.rect.right - player.left
            topOverlap = player.bottom - self.rect.top
            bottomOverlap = self.rect.bottom - player.top
            min_overlap = min(leftOverlap, rightOverlap, topOverlap, bottomOverlap)#Which of these overlaps is smallest?
            
            if min_overlap == topOverlap:
                momentumY=0
                offset.y += topOverlap
                
            elif min_overlap == bottomOverlap:
                momentumY=0
                offset.y -= bottomOverlap
                boost=0
                
            elif min_overlap == leftOverlap:
                offset.x += leftOverlap
            elif min_overlap == rightOverlap:
                offset.x -= rightOverlap
def handleInputs():
    global gameLoop,facing,boost,world,acceptingNewVector,inRange, imageswitch,imagenum,imagerow, touchingground,bulletx,bullety,shot
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
            #if inRange==True:
              #  inRange = False
            if touchingground:
                boost = 10
                acceptingNewVector = True
                touchingground = False
        #pass
    if keys[pygame.K_DOWN]:
        #offset.y -= playerSpeed
        pass
    if keys[pygame.K_LEFT]:
        facing = "left"
        offset.x += playerSpeed + 5
        imagerow = 0
        imageswitch +=1
        if imageswitch == 5:
            imageswitch =0
            imagenum+=1
        if imagenum == 3:
            imagenum = 0
    if keys[pygame.K_RIGHT]:
        offset.x -= playerSpeed + 5
        facing = "right"
        imagerow = 1
        imageswitch +=1
        if imageswitch == 5:
            imageswitch =0
            imagenum+=1
        if imagenum == 3:
            imagenum = 0
    if keys[pygame.K_SPACE]:
        shot = True

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} clicked at {event.pos}")

                
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameLoop = False

def drawPlayer():
    
    #screen.blit(soulImage,(playerRect.centerx-soulImageSize/2,playerRect.centery-soulImageSize/2),(soulImageX,0,soulImageStep,soulImageH))
        loadimage = pygame.image.load("spite.png")

        image = 132 * imagenum
        imageY = 172 * imagerow

        screen.blit(loadimage, (playerRect[0], playerRect[1]-65), (image, imageY,132,172))
        # 3. Inside your game loop, replace the draw.rect call with:



    


def angleCalc():
    global playerRect,boost,offset,acceptingNewVector,boostVector,mousePos,reticle, touchingground
    direction_vector = Vector2( 384, 540) - playerRect.center
    if direction_vector.length() > 0:
        direction_vector = direction_vector.normalize()
    target_offset = direction_vector * 100
    square_pos = playerRect.center + target_offset
    reticle = pygame.Rect(square_pos.x-25,square_pos.y-25,50,50)
    #pygame.draw.rect(screen, ('yellow'), reticle,0,5)
    
    if (acceptingNewVector):
        #if touchingground:
        boostVector = direction_vector
        acceptingNewVector = False
        #touchingground = False
        #else:
           # touchingground = False
    velocity = boostVector * boost * 4
    offset += velocity
    if boost > 0:
      boost -= 1
def gravity():
    global offset,grounded,fallSpeed,momentumY
    
    if grounded == False:
        if momentumY<fallSpeed:
            momentumY += 1
        offset.y-=momentumY

tilemap = [
    'B_______B___E______________________________________________BBBB____F___________________________',
    'B____________________________________________________BBBB______BBBB___________________________',
    'B_______B____________________________________BBBB___________________________________________',
    'B______C_____________________________BBBBB__________________________________________________',
    'B________________________BBBBBBBBBB___________________________________________________________',
    'BBBBBBBBBBBBBBBBBBBBBBB_________________________________________________________________'
            ]
blocks = []
tileSize = 100
enimys = []
for y, row in enumerate(tilemap):
    for x, tile in enumerate(row):
        if tile == 'B':
            blocks.append(Block((offset.x + (x*tileSize), offset.y+(y*tileSize)), (tileSize, tileSize), BLUE))
        if tile == "C":
             blocks.append(Church((offset.x + (x*500), offset.y+(y*500)), (500, 500), BLUE))
        if tile =="F":
            
            finish = Finish((offset.x + (x*tileSize), offset.y+(y*tileSize)), (tileSize, tileSize), RED)
            blocks.append(finish)
        if tile =="E":
            if enimynum == 1:
                #enimy1 = Enimy((offset.x + (x*tileSize), offset.y+(y*tileSize)), (tileSize, tileSize), RED)
                #blocks.append(enimy1)
                enimynum +=1
            if enimynum == 2:
                enimy2 = Enimy((offset.x + (x*tileSize), offset.y+(y*tileSize)), (tileSize, tileSize), RED)
                blocks.append(enimy2)
                enimynum +=1
world = pygame.Vector2(playerRect.x+offset.x,playerRect.y+offset.y)
print(str(blocks))


speed = 1


enimyalive = True
while gameLoop:
    if enimyalive:
        # enimy move
        enimyspeed = 5
        player_world = pygame.Vector2(playerRect.centerx - offset.x,
                                    playerRect.centery - offset.y)
        direction = player_world - enimy2.position
        if direction.length() > 0:
            direction = direction.normalize()
            enimy2.position += direction * enimyspeed
    else:
        enimy2.position = Vector2(-10000,-10000)
    #print(f"Enemy at {enimy2.position}, player at {player_world}")
    #print(offset.y)
    
    bullety = playerRect.y - 50

    bullethit = pygame.Rect((bulletx,bullety,50,50))

    enimy2box = pygame.Rect((enimy2.position.x,enimy2.position.y,50,50))
    # end

    if offset.x < -6222.010828212269:
        time.sleep(1)
        gameLoop = False



    screen.fill(BLUE)
    QB1 = pygame.image.load("background2.jpeg")
    QB1 = pygame.transform.scale(QB1, (screen.get_width(), screen.get_height()))
    screen.blit(QB1,(0,0),(0,0,screen.get_width(),screen.get_height()))
    clock.tick(FPS)
    mousePos = pygame.mouse.get_pos()
    
    handleInputs()
    if shot:
        lazer.play()
        print(enimy2.position[1])
        if bullethit.colliderect(enimy2box):
            if shot:
                print("kill")
                enimyalive = False

        alatri = pygame.image.load("bullet.png")
        screen.blit(alatri, (bulletx, bullety))
        if facing == "right":
            bulletx += bulletspeed
        #if facing == "left":
         #   bulletx -= bulletspeed 
        

        if bulletx > 700:
            bulletx = playerRect.x
            shot = False
    w, h = pygame.display.get_surface().get_size()
    playerRect = pygame.Rect(w/2-playerRect.w/2,h/2-playerRect.h/2,100,100)
    world = pygame.Vector2(playerRect.x+offset.x,playerRect.y+offset.y)
    gravity()
    inRange=False
    for block in blocks:
        block.rect.topleft = (block.position.x + offset.x, block.position.y + offset.y)
        block.collide(playerRect)
        if block.rect.colliderect(reticle):
            inRange = True
    grounded = False

    #ground = pygame.Rect(world.x-100,world.y+150,800,200)

    
    #collidePlayer(ground,playerRect)

    #offset.y+=momentumV
    #then do all your drawing
    for block in blocks:
        block.draw()
    pygame.display.set_caption(f"{inRange}")
    drawPlayer()
    angleCalc()
    pygame.display.flip()
    

pygame.quit()
