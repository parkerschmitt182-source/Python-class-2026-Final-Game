def define():
    import info
    import pygame, sys
    from pygame.locals import *
    from pygame import mixer
    import time
    # this is a file containing all the variables that are used in the game, such as the screen width and height, the player's position, and the level number. This file is imported into the main game file, so that all the variables can be accessed from there.
    pygame.init()
    pygame.mixer.init()
    boot = pygame.mixer.Sound("boot.mp3")
    stepsound = pygame.mixer.Sound("step.mp3")
    boot.play()
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