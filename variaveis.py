import pygame
import os
import time


largura = 1200
altura = 640
branco = 255, 255, 255
ultimo = "sprite_baixo"
#mapa = pygame.image.load(os.path.join('assets', 'mapa.png'))
#background = pygame.transform.scale(mapa, (1200, 640))


pygame.font.init()
fonte = pygame.font.SysFont('arial', 20, True, True)


tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
valor = 0
movimentando = False
velocity = 12
#x = largura/2
x = 0
y = 0
#y = altura/2
a = 0
b = 0
#ret_um = pygame.Rect(x, y, 50, 81)
#ret_dois = pygame.Rect(a + 200, b + 281, 50, 81)

preto = (0,0,0)
azul_escuro = (0, 17, 76)
verde = (23, 108, 0)
rodando = False
valor_continuar = 0
contador = 0
inicio = time.time()
jft = 0
jfc = 0
scene = False
uncolliderect = 0
pontos=0
fases = 0
pula_fases = False
aparecer = False

'''
img_tio_juca = pygame.image.load(os.path.join('assets', 'tio_juca.png'))
tio_juca = pygame.transform.scale(img_tio_juca, (50, 81))

img_vo_jose_paulino = pygame.image.load(os.path.join('assets', 'jose_paulino.png'))
vo_jose_paulino = pygame.transform.scale(img_vo_jose_paulino, (50, 81))

img_tia_maria = pygame.image.load(os.path.join('assets', 'tia_maria.png'))
tia_maria = pygame.transform.scale(img_tia_maria, (50, 81))

img_tia_sinhazinha = pygame.image.load(os.path.join('assets', 'tia_sinhazinha.png'))
tia_sinhazinha = pygame.transform.scale(img_tia_sinhazinha, (50,81))

img_primos = pygame.image.load(os.path.join('assets', 'primos.png'))
primos = pygame.transform.scale(img_primos, (100,81))

img_prima_maria_clara = pygame.image.load(os.path.join('assets', 'prima_maria_clara.png'))
prima_maria_clara = pygame.transform.scale(img_prima_maria_clara, (50,81))


canario = pygame.image.load(os.path.join('assets', 'canario.png'))
canario = pygame.transform.scale(canario, (32, 32))




mensagem = ()
#texto_formatado = fonte.render(mensagem[0], False, (255, 255, 255))
nome = "tio juca"



info_tio_juca = {
"nome":"Tio Juca",
"posicao":((a + 200, b + 200)),
"scale":pygame.transform.scale(img_tio_juca, (50, 81)),
"mensagem":[["Est?? gostando do engenho do seu av??, meu sobrinho?", ""], ["J?? se fazem quatro anos desde que voc?? chegou, meu sobrinho", "Como o tempo passa", ""], ["Coitado de voc??, menino", "Tem estado t??o triste desde que sua prima partiu e sua tia se casou", ""]],
"contadora":0
#"mensagem_formatada":fonte.render(mensagem[texto_count-1], False, (0,0,0))
}

info_vo_jose_paulino = {
"nome":"V?? Jos?? Paulino",
"posicao":((a + 300, b + 400)),
"scale":pygame.transform.scale(img_vo_jose_paulino, (50, 81)),
"mensagem":[["Deus te aben????e, meu neto", "Um dia desses te levo para conhecer o engenho inteiro", ""], ["J?? est?? com oito anos, em?", "Voc?? cresceu muito r??pido", ""],["Parece que est?? na hora de voc?? ir para o c??legio", "?? o melhor a se fazer", ""]],
"contadora":0
#"mensagem_formatada":((fonte.render(mensagem[texto_count-1], False, (255,0,0))))

}

info_tia_maria = {
    "nome": "Tia Maria",
    "posicao": ((a+400, b+50)),
    "scale":pygame.transform.scale(img_tia_maria, (50,81)),
    "mensagem":[["N??o precisa ficar triste",  "Agora n??s seremos sua fam??lia", ""],["Que bom que est?? se dando bem com sua prima", "Ela veio de muito longe, e n??o vai ficar muito tempo aqui", ""]],
    "contadora":0
}


info_tia_sinhazinha = {
    "nome": "Tia Sinhazinha",
    "posicao": ((a+700, b+50)),
    "scale":pygame.transform.scale(img_tia_sinhazinha, (50,81)),
    "mensagem":[["Espero que voc?? seja um menino bonzinho", ""], ["Voc?? est?? ficando cada vez mais travesso, moleque",""], ["Mal posso esperar para te botar no col??gio", "J?? est?? com doze anos e n??o sabe de nada, s?? de fazer besteiras", ""]],
    "contadora":0
}
info_primos = {
    "nome": "Primos",
    "posicao": ((a+900, b+350)),
    "scale":pygame.transform.scale(img_primos, (100,81)),
    "mensagem":[["Vamos brincar, Carlinhos!",""],["A?? est?? voc??, Carlinhos", "Precisamos te contar sobre tudo o que aconteceu no col??gio", ""], ["Ficamos sabendo que voc?? vai para o col??gio, Carlinhos", "Boa sorte", ""]]
}

info_prima_maria_clara = {
    "nome": "Prima Maria Clara",
    "posicao": ((a+650, b+450)),
    "mensagem":["Oi Carlinhos", "N??s pod??amos fazer um piquenique nos cajuzeiros", ""]
}

nnpode = {
    "tio juca":((a + 200, b + 200)),
    "vo jose paulino": ((a + 300, b + 400)),
    "tia maria":((a+400, b+50)),
    "tia sinhazinha":((a+700, b+50)),
    "primos":((a+900, b+350)),
    "prima maria clara":((a+650, b+400))
}
lista_colisao = [
    pygame.Rect(a + 200, b +200 , 50, 63), 
    pygame.Rect(a + 300, b +400 , 50, 63),
    pygame.Rect(a + 400, b +50 , 50, 63),
    pygame.Rect(a + 700, b +50 , 50, 63),
    pygame.Rect(a + 900, b +365 , 100, 53)
]
cont_tio_juca = 0
cont_vo_jose_paulino = 0
cont_tia_maria = 0
cont_tia_sinhazinha = 0
cont_primos = 0
cont_prima_maria_clara = 0

texto_tio_juca = False
texto_vo_jose_paulino = False
texto_tia_maria = False
texto_tia_sinhazinha = False
texto_primos = False
texto_prima_maria_clara = False

ret1 = pygame.Rect(x, y, 50, 81)
void = False
falou = {
    "tio_juca":False,
    "vo_jose_paulino":False,
    "tia_maria":False,
    "tia_sinhazinha":False,
    "primos":False

}
passa = False

#texto_count = 0
nome_formatado = fonte.render(nome, False, (0,0,0))
nada = ''
#nada_formatado = fonte.render(nome,False, (0,0,0))
hookado = False
'''
donda2=False
bateu = ''
tava_no_elif = False
heartless = False


mensagemc = f'Can??rios: {pontos}'
texto_formatado = fonte.render(mensagemc,False,(0, 0, 0))
texto_rect = texto_formatado.get_rect()
texto_rect.center = (largura/2, 100)


pontos=0
sla = 0
gambiarra3 = 0
x_marrom = 900
y_marrom = 200
largura = 1200
altura = 640
x=largura/2
y=altura/2
#relogio=pygame.time.Clock()
#tela=pygame.display.set_mode((largura, altura))


rodando = False
valor_continuar = 0
contador = 0
valor_cutscene = 0
gambiarra = 0
gambiarra2 = 0
c = 1300
a = 0 
b = 0
x_trem_voltando = -2800
gambiarra4 = 0
contador_som_trem2 = 0

posicoesx = []
posicoesy = []
nnpode = [[a + 200, b + 200],[a + 300, b + 400],[a+400, b+50],[a+700, b+50],[a+900, b+350]]
contador_som_trem = 0