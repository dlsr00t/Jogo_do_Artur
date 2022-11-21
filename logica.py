import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
preto = (0,0,0)
branco = (255,255,255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites= []
        self.sprites.append(pygame.image.load('./Thief.png'))


while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    pygame.display.flip()













