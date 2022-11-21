import pygame
from pygame.locals import *
#from variaveis import *
import os
import time

donda = ''
largura = 1200
altura = 640
branco = 255, 255, 255
ultimo = "sprite_baixo"
mapa = pygame.image.load(os.path.join('assets', 'mapa.png'))
background = pygame.transform.scale(mapa, (1200, 640))


pygame.font.init()
fonte = pygame.font.SysFont('arial', 20, True, True)


tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
valor = 0
movimentando = False
velocity = 12
#x = largura/2
x = 35
y = 0
#y = altura/2
a = 0
b = 0
#ret_um = pygame.Rect(x, y, 50, 81)
#ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)

#retangulo = pygame.Rect(largura/2, altura/2, 500, 140)
#retangulo.midtop = (largura/2, 220)
#imagem = pygame.image.load(os.path.join('assets', 'Thief1'+'.png'))
#imagem = pygame.transform.scale(imagem, (40, 60))
roxo = (161,72,161)


def sprite(sprite_name):
    global image_sprite
    image_sprite = [
                    pygame.image.load(os.path.join('assets', sprite_name+'2'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'3'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'4'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'5'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'6'+'.png'))
                    ]
'''

def sprite(sprite_name):
    global image_sprite
    image_sprite = [pygame.image.load(os.path.join('assets', sprite_name+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'1'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'2'+'.png')),
                    pygame.image.load(os.path.join('assets', sprite_name+'.png'))]
'''

def is_moving():
    global movimentando
    global imagem_ret
    global valor
    global paredes
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s or imagem_ret.collidelist(paredes)>=0:
            #movimentando = False
            valor = 0
            movimentando = False
textinho = True
ultimo = 'Thief'
x+=5
y+=120
tempo = False
ganhou = False
ganhouT = False
cheat = 0

while True:



    if ganhou == True:
        while ganhouT == False:    
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            tela.fill(roxo)
            mensagem2 = f'Voce ganhou!!!'
            texto_formatado2 = fonte.render(mensagem2,False,(255, 255, 255))
            texto_rect2 = texto_formatado.get_rect()
            texto_rect2.center = (largura/1.7, 320)
            tela.blit(texto_formatado2, texto_rect2)
            pygame.display.flip()
            time.sleep(3)
            ganhouT = True

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            tela.fill(roxo)
            mensagem2 = f'Alunos: Artur Mendes, Joao Marcelo de Souza, Gustavo Simoes'
            texto_formatado2 = fonte.render(mensagem2,False,(255, 255, 255))
            texto_rect2 = texto_formatado.get_rect()
            texto_rect2.center = (largura/3, 320)
            tela.blit(texto_formatado2, texto_rect2)
            pygame.display.flip()       
        


    else:
        tela.fill(roxo)
        if textinho == True:
            mensagem = f'Voce tem 23 segundos para sair do labirinto'
            texto_formatado = fonte.render(mensagem,False,(255, 255, 255))
            texto_rect = texto_formatado.get_rect()
            texto_rect.center = (largura/2, 50)
            tela.blit(texto_formatado, texto_rect)
        



    
        
        if tempo == True:
            fim = time.time()
            if fim-inicio>=44:
                break

        relogio.tick(30)
        imagem_ret = pygame.Rect(x, y, 40, 60)

        #tela.blit(imagem, (0,0))


        retangulo = pygame.Rect(largura/2, altura/2, 500, 140)
        retangulo.midtop = (largura/2, 220)

        sprite(ultimo)
        #tela.blit(imagem, (0, 0))

        #pygame.draw.rect(tela, roxo, retangulo)
        paredes = [
            ###inicio da primeira reta a esquerda para baixo
            pygame.draw.rect(tela, (0,0,0), (a+15, b+100,15,490)),
            pygame.draw.rect(tela, (0,0,0), (a+25, b+400,100,15 )),



            #pygame.draw.rect(tela, (0,0,0), (a+370, b+475, 15,100))



            #inicio da primeira bifurcacao
            pygame.draw.rect(tela, (0,0,0), (a+600, b+475, 15, 115)),
            pygame.draw.rect(tela, (0,0,0), (a+500 , b+460, 230, 15)),#bi
            pygame.draw.rect(tela, (0,0,0), (a+500, b+400, 15, 60)),#a esquerda
            pygame.draw.rect(tela, (0,0,0), (a+715, b+370, 15, 90)),#a direita
            #fim da primeira bifucacao

            #inicio da segunda bifurcacao
            pygame.draw.rect(tela, (0,0,0), (a+600, b+370, 260, 15)),#bi
            pygame.draw.rect(tela, (0,0,0), (a+600, b+290, 15, 90)),#a esquerda
            pygame.draw.rect(tela, (0,0,0), (a+845, b+290, 15, 90)),#a direita
            #fim da segunda bifurcacao

            #continuacao da segunda bifurcacao a esquerda
            pygame.draw.rect(tela, (0,0,0), (a+500, b+290, 100, 15 )),
            pygame.draw.rect(tela, (0,0,0), (a+500, b+200, 15, 90)),
            pygame.draw.rect(tela, (0,0,0), (a+400, b+200, 100, 15)),
            #fim da continuacao da segunda bifucacao a esquerda

            #continuacao da segunda bifurcacao a direita
            pygame.draw.rect(tela, (0,0,0), (a+845, b+200, 15, 90)),
            pygame.draw.rect(tela, (0,0,0), (a+715, b+200, 260, 15)),
            pygame.draw.rect(tela, (0,0,0), (a+715, b+200, 15, 90)),
            #fim da continuacao da segunda bifurcacao a direita

            pygame.draw.rect(tela, (0,0,0), (a+25, b+575, 1005, 15)),#reta final
            ###fim da primeira reta pricipal a esquerda para baixo





            ###inico da segunda reta principal a direita para a direita
            pygame.draw.rect(tela, (0,0,0), (a+15, b+100,1130,15)),
            pygame.draw.rect(tela, (0,0,0), (a+600, b+100,15,105)),



            #inicio da primeira bifurcacao
            pygame.draw.rect(tela, (0,0,0), (a+310, b+115,15,180)),
            pygame.draw.rect(tela, (0,0,0), (a+100, b+290,285,15)),#bi
            #fim da primeira bifurcacao

            #continuacao da primeira bifurcacao (metade do inicio da bifurcacao a esquerda para baixo)
            pygame.draw.rect(tela, (0,0,0), (a+190, b+305,15,100)),
            #fim da continuacao da primeira bifurcacao (metade do inicio da bifurcacao a esquerda para baixo)

            #continuacao da primeira bifurcacao (esquerda para cima)
            pygame.draw.rect(tela, (0,0,0), (a+100, b+200,15,90)),
            pygame.draw.rect(tela, (0,0,0), (a+100, b+200,100,15)),
            #fim da continuacao da primeira bifurcacao (esquerda para cima)

            #continuacao da primeira bifurcacao (direita para baixo)
            pygame.draw.rect(tela, (0,0,0), (a+370, b+305,15,100)),
            pygame.draw.rect(tela, (0,0,0), (a+280, b+405,105,15)),
            pygame.draw.rect(tela, (0,0,0), (a+280, b+405,15,90)),
            pygame.draw.rect(tela, (0,0,0), (a+100, b+495,195,15)),
            #fim da continuacao da primeira bifurcacao(direita para baixo)

            pygame.draw.rect(tela, (0,0,0), (a+960, b+290, 185, 15)),
            pygame.draw.rect(tela, (0,0,0), (a+960, b+290, 15, 85)),
            pygame.draw.rect(tela, (0,0,0), (a+860 , b+460, 285, 15)),
            pygame.draw.rect(tela, (0,0,0), (a+1130, b+100,15,490))#reta final
        ]
        fim = [pygame.Rect(a+1030, b+590, 100, 15)]
        #pygame.draw.rect(tela, branco, fim)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                textinho = False
                if tempo == False:
                    inicio = time.time()
                    tempo = True
                
                '''
                cheatI = time.time()
                if event.key == K_UP:
                    cheat += 1
                    print("up1")
                if event.key == K_DOWN:
                    cheat +=1
                if event.key == K_UP:
                    cheat+=1
                    print("up2")
                if event.key == K_DOWN:
                    cheat+=1
                if event.key == K_LEFT:
                    cheat+=1
                if event.key == K_RIGHT:
                    cheat+=1
                if event.key == K_LEFT:
                    cheat+=1     
                if event.key == K_RIGHT:
                    cheat+=1
                if event.key == K_b:
                    cheat+=1      
                if event.key == K_a:
                    cheat+=1    
                    '''       
            is_moving()######CHEAT CODE(CIMA, CIMA, BAIXO, BAIXO, ESQUERDA, DIREITA, ESQUERDA, DIREITA, 'B', 'A')
        #if imagem_ret.collidelist(paredes):

        if imagem_ret.collidelist(fim)>=0:
            ganhou = True

        if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_d]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_s]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_s]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_w]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_w]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_a]:
            #if x > a:
            if not imagem_ret.collidelist(paredes)>=0 or donda != 'a':

                x -= 4
                movimentando = True
                sprite("Thief_esquerda")
                ultimo = "Thief_esquerda"
                a += 4
                donda = 'a'
            else:
                movimentando = False
        elif pygame.key.get_pressed()[K_d]:
            #if x + 50 < a + 1200 :
                #if (not False in falou.values()):
                #    x+=1.5
                #    a-=1.5
            if not imagem_ret.collidelist(paredes)>=0 or donda != 'd':
                x += 4
                movimentando = True
                sprite("Thief")
                ultimo = "Thief"
                a -= 4
                donda = 'd'
            else:
                movimentando = False


        if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_s]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_a]:
            ultimo = ultimo
            movimentando = False


        elif pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_d]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_a]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_d]:
            ultimo = ultimo
            movimentando = False

        elif pygame.key.get_pressed()[K_w]:
            #if y > b :
                #if (not False in falou.values()):
                #    y-=1.5
                #    b+=1.5
                #sprite("sprite_cima")
            if not imagem_ret.collidelist(paredes)>=0 or donda != 'w':
                sprite("Thief")
                ultimo = "Thief"
                #print("to aqui")
                y -= 4
                movimentando = True
                donda = 'w'
                b += 4
            else:
                movimentando = False
        elif pygame.key.get_pressed()[K_s]:
            #if y + 81 < b + 640 :
                #if (not False in falou.values()):
                #    y+=1.5
                #    b-=1.5
                #sprite("sprite_baixo")

            if not imagem_ret.collidelist(paredes)>=0 or donda != 's':
                sprite("Thief")
                ultimo = "Thief"
                y += 4
                movimentando = True
                donda = 's'
                b-=4
            else:
                movimentando = False
        if cheat==10:
            print("cheat ativado")

        if movimentando == True:
            #if(not False in falou.values()):
            #    #valor+=0.25
            #    pass

            valor += 0.25
        else:
            valor = 0
        if valor >= len(image_sprite):
            valor = 0
        imagem = image_sprite[int(valor)]
        imagem = pygame.transform.scale(imagem, (50, 60))

        tela.blit(imagem, (x, y))

        pygame.display.flip()


