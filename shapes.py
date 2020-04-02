import pygame,sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Shapes')

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)

DISPLAYSURF.fill(white)
pygame.draw.line(DISPLAYSURF,blue,(60,60),(60,120),4)
pygame.draw.line(DISPLAYSURF,blue,(100,60),(60,95),2)
pygame.draw.line(DISPLAYSURF,blue,(60,95),(100,120),2)
pygame.draw.circle(DISPLAYSURF,red,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,red,(300,200,40,80),1)
pygame.draw.rect(DISPLAYSURF,green,(200,150,100,50))

pix = pygame.PixelArray(DISPLAYSURF)
pix[380][280] = black
pix[382][282] = black
pix[384][284] = black
pix[386][286] = black
pix[388][288] = black
del pix

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
