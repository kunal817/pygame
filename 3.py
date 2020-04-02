import pygame,sys 
from pygame.locals import *

catx=10
caty=10
catz=10
catr=10
screen=0

def myquit():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global catx,caty,catz,catr,screen

    for event in events:
        if event.type==QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key ==K_LEFT:
                    catx -= 5
                    print("move rect left")
                elif event.key ==K_RIGHT:
                    catx += 5
                    print("move rect Right")
                elif event.key ==K_UP:
                    caty -= 5
                    print("move rect up")
                elif event.key ==K_DOWN:
                    caty += 5
                    print("move rect down")
                elif event.key ==K_k:
                    catz +=5
                elif event.key ==K_l:
                    catz -=5
                elif event.key ==K_r:
                    catr +=5
                elif event.key ==K_t:
                    catr -=5
                else:
                    print(event.key)
    screen.fill([255,255,255])
    pygame.draw.rect(screen,[0,0,0],(catx,caty,catz,catr))
    pygame.display.update()

def main():
    global screen
    pygame.init()
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=480
    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('snake')
    screen = pygame.display.get_surface()
    
    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()
