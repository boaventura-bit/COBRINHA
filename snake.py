import pygame
import time
import random
import os
import sys

pygame.init()

# Paleta de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (213, 50, 80)
LARANJA = (255, 165, 0)

# Tamanho da tela
LARGURA_TELA = 600
ALTURA_TELA = 400

# Tamanho e velocidade
TAMANHO_BLOCO = 10
VELOCIDADE = 9

# Tela de jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo da Cobrinha')

# Local bkg e ícone
if getattr(sys, 'frozen', False):
    caminho_imagem = os.path.join(sys._MEIPASS, "floresta_8bits.png")
    caminho_icon = os.path.join(sys._MEIPASS, "icon.ico") 
else:
    caminho_imagem = "floresta_8bits.png"
    caminho_icon = "icon.ico" 

# Carregando o bkg
background = pygame.image.load(caminho_imagem)
background = pygame.transform.scale(background, (LARGURA_TELA, ALTURA_TELA))

# Carrega e define o ícone da janela
try:
    icon = pygame.image.load(caminho_icon)
    pygame.display.set_icon(icon)
except pygame.error as e:
    print(f"Não foi possível carregar o ícone: {e}")

# Arquivo de recorde
ARQUIVO_RECORDE = "recorde.txt"

# Carregar o recorde
def carregar_recorde():
    if os.path.exists(ARQUIVO_RECORDE):
        with open(ARQUIVO_RECORDE, 'r') as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

# Salva o recorde
def salvar_recorde(novo_recorde):
    with open(ARQUIVO_RECORDE, 'w') as f:
        f.write(str(novo_recorde))

# Inicia o recorde
recorde = carregar_recorde()

# Mostra pontuação e o recorde
def sua_pontuacao(score, recorde):
    fonte = pygame.font.SysFont('arial', 20)
    valor_pontuacao = fonte.render("Pontuação: " + str(score), True, PRETO)
    valor_recorde = fonte.render("Recorde: " + str(recorde), True, PRETO)
    tela.blit(valor_pontuacao, [0, 0])
    tela.blit(valor_recorde, [0, 30])

# Função principal
def jogo():
    global recorde
    fim_jogo = False
    fim_deu_ruim = False

    x = LARGURA_TELA / 2
    y = ALTURA_TELA / 2

    x_mudanca = 0
    y_mudanca = 0

    corpo_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not fim_jogo:

        while fim_deu_ruim:
            tela.fill(BRANCO)
            fonte_perdeu = pygame.font.SysFont('arial', 20)
            mensagem_perdeu = fonte_perdeu.render('Você perdeu! Pressione C para continuar ou Q para sair', True, VERMELHO)
            tela.blit(mensagem_perdeu, [LARGURA_TELA / 6, ALTURA_TELA / 3])
            sua_pontuacao(comprimento_cobra - 1, recorde)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_jogo = True
                        fim_deu_ruim = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_mudanca = -TAMANHO_BLOCO
                    y_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x_mudanca = TAMANHO_BLOCO
                    y_mudanca = 0
                elif event.key == pygame.K_UP:
                    y_mudanca = -TAMANHO_BLOCO
                    x_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y_mudanca = TAMANHO_BLOCO
                    x_mudanca = 0

        if x >= LARGURA_TELA or x < 0 or y >= ALTURA_TELA or y < 0:
            fim_deu_ruim = True

        x += x_mudanca
        y += y_mudanca

        tela.blit(background, [0, 0])

        pygame.draw.rect(tela, LARANJA, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])

        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_deu_ruim = True

        for bloco in corpo_cobra:
            pygame.draw.rect(tela, PRETO, [bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO])

        sua_pontuacao(comprimento_cobra - 1, recorde)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / 10.0) * 10.0
            comprimento_cobra += 1

        if comprimento_cobra - 1 > recorde:
            recorde = comprimento_cobra - 1
            salvar_recorde(recorde)

        clock.tick(VELOCIDADE)

    pygame.quit()
    sys.exit()

# rodar o jogo
jogo()
