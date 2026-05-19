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

def text(text2, x, y, size):
    my_font = pygame.font.SysFont('Arial', size)
    text_surface = my_font.render(text2, True, 'white')
    screen.blit(text_surface, (x, y))

# 1. Initialize Pygame

typingstory = True
screen.fill((0, 0, 0)) 
print(len(alatrilines[1]))
pygame.mixer.init()

# 2. Load and play the music in an infinite loop (-1 means loop forever)
pygame.mixer.music.load("typing.mp3")
pygame.mixer.music.play(-1)

if typingstory:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            typingstory = False
    for i in range(len(alatrilines)):
        for x in range(len(alatrilines[i])):

            
            
            final = x +1
            
            text(alatrilines[i][:final], screen.get_width()/2-100, 20*i, 20)
            pygame.display.flip()
            clock.tick(60)
            

            time.sleep(.01)
time.sleep(1)

alatrilines = [
"You are playing as the",
"priest your goal is to",
"find the missing hosts",
"while fighting off the",
"devils."
]
screen.fill((0, 0, 0)) 
if typingstory:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            typingstory = False
    for i in range(len(alatrilines)):
        for x in range(len(alatrilines[i])):


            
            final = x +1
            
            text(alatrilines[i][:final], screen.get_width()/2-100, 20*i, 20)
            pygame.display.flip()
            clock.tick(60)
            

            time.sleep(.01)
time.sleep(1)
pygame.mixer.music.stop()








print("main")
# 4. Main Game Loop

while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background (Red, Green, Blue)
    screen.fill((0, 0, 0)) 
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate to 60 FPS
    clock.tick(60)

# 5. Clean up
pygame.quit()
sys.exit()
