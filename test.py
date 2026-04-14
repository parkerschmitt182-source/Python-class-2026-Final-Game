import pygame, random, math
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

screen = pygame.display.set_mode((800, 1000), pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 60

offset = pygame.Vector2(0, 0)
tileSize = 100

gameLoop = True


# ================= BLOCK =================
class Block:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


# ================= ENEMY =================
class Enimy:
    def __init__(self, position, size, color):
        self.position = Vector2(position)
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color

        self.speed = 2
        self.direction = 1

        self.start_x = self.position.x
        self.range = 200

    def update(self):
        self.position.x += self.speed * self.direction

        if self.position.x > self.start_x + self.range:
            self.direction = -1
        elif self.position.x < self.start_x:
            self.direction = 1

        self.rect.topleft = self.position

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


# ================= TILEMAP =================
tilemap = [
    'B_______B',
    'B________',
    'B_______B',
    'B__________E______',
    'B______BBBBBBBBBBBB',
    'BBBBBBBBB'
]

blocks = []
enimys = []


# ================= BUILD WORLD =================
for y, row in enumerate(tilemap):
    for x, tile in enumerate(row):

        pos = (offset.x + x * tileSize, offset.y + y * tileSize)

        if tile == "B":
            blocks.append(Block(pos, (tileSize, tileSize), BLUE))

        elif tile == "E":
            enimys.append(Enimy(pos, (tileSize, tileSize), RED))


# ================= GAME LOOP =================
while gameLoop:

    screen.fill(BLACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    # UPDATE ENEMIES
    for enemy in enimys:
        enemy.update()

    # DRAW BLOCKS
    for block in blocks:
        block.draw()

    # DRAW ENEMIES
    for enemy in enimys:
        enemy.draw()

    pygame.display.flip()

pygame.quit()
