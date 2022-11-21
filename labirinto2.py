import pygame
from pygame.locals import *
from variaveis import *
import os


retangulo = pygame.Rect(largura/2, altura/2, 500, 140)
retangulo.midtop = (largura/2, 220)
imagem = pygame.image.load(os.path.join('assets', 'Thief1_esquerda'+'.jpg'))
imagem = pygame.transform.scale(imagem, (30, 40))
roxo = (161,72,161)

while True:
    tela.fill(branco)
    tela.blit(imagem, (450, 150))#inicio altura e 70
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    retangulo = pygame.Rect(largura/2, altura/2, 500, 140)
    retangulo.midtop = (largura/2, 220)

    
    #tela.blit(imagem, (0, 0))
    
    #pygame.draw.rect(tela, roxo, retangulo)
    
    ###inicio da primeira reta a esquerda para baixo
    pygame.draw.rect(tela, (0,0,0), (a+15, b+130,15,460))
    pygame.draw.rect(tela, (0,0,0), (a+15, b+130,100,15))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+130,15,100))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+230,100,15))
    pygame.draw.rect(tela, (0,0,0), (a+200, b+130,15,115))#
    pygame.draw.rect(tela, (0,0,0), (a+200, b+130,240,15))#
    pygame.draw.rect(tela, (0,0,0), (a+15, b+575,1115,15))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+485,15,105))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+485,205,15))
    pygame.draw.rect(tela, (0,0,0), (a+600, b+485,15,105))
    pygame.draw.rect(tela, (0,0,0), (a+500, b+485,115,15))#
    pygame.draw.rect(tela, (0,0,0), (a+500, b+430,15,70))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+430,415,15))
    pygame.draw.rect(tela, (0,0,0), (a+100, b+300,15,130))
    pygame.draw.rect(tela, (0,0,0), (a+200, b+300,15,80))#
    pygame.draw.rect(tela, (0,0,0), (a+200, b+380,415,15))#
    pygame.draw.rect(tela, (0,0,0), (a+600, b+380,15,200))
    pygame.draw.rect(tela, (0,0,0), (a+700, b+485,230,15))
    pygame.draw.rect(tela, (0,0,0), (a+915, b+310,15,190))
    pygame.draw.rect(tela, (0,0,0), (a+700, b+300,15,185))
    pygame.draw.rect(tela, (0,0,0), (a+330, b+300,370,15))
    pygame.draw.rect(tela, (0,0,0), (a+330, b+200,15,115))
    pygame.draw.rect(tela, (0,0,0), (a+330, b+200,110,15))
    pygame.draw.rect(tela, (0,0,0), (a+540, b+200,375,15))



    pygame.draw.rect(tela, (0,0,0), (a+15, b+50,1100,15))
    pygame.draw.rect(tela, (0,0,0), (a+540, b+130,375,15))
    pygame.draw.rect(tela, (0,0,0), (a+915, b+130,15,175))
    pygame.draw.rect(tela, (0,0,0), (a+915, b+305,215,15))



    pygame.draw.rect(tela, (0,0,0), (a+1115, b+50,15,450))

    pygame.display.flip()