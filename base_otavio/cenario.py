import pygame
import sys
import os  # Para verificar se o arquivo de imagem existe
import random

# Inicializando o pygame
pygame.init()

# Definindo o tamanho da janela
largura = 1200
altura = 800
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cenário Simples")

# Verificar se a imagem de fundo existe
if not os.path.exists("base_otavio/fundo.jpg"):
    print("Erro: Imagem de fundo não encontrada.")
    sys.exit()

# Verificar se a imagem do personagem existe
if not os.path.exists("base_otavio/personagem.png"):
    print("Erro: Imagem do personagem não encontrada.")
    sys.exit()

# Verificar se a imagem da espada existe
if not os.path.exists("base_otavio/espada.png"):
    print("Erro: Imagem da espada não encontrada.")
    sys.exit()

# Verificar se a imagem do inimigo existe
if not os.path.exists("base_otavio/inimigo.png"):
    print("Erro: Imagem do inimigo não encontrada.")
    sys.exit()

# Carregar as imagens
fundo = pygame.image.load("base_otavio/fundo.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

personagem = pygame.image.load("base_otavio/personagem.png")
personagem = pygame.transform.scale(personagem, (90, 90))

espada = pygame.image.load("base_otavio/espada.png")
espada = pygame.transform.scale(espada, (40, 40))  # Tamanho da espada

inimigo_img = pygame.image.load("base_otavio/inimigo.png")
inimigo_img = pygame.transform.scale(inimigo_img, (64, 64))

# Posição inicial do personagem
personagem_x = 550
personagem_y = 400

# Posição inicial do inimigo
inimigo_x = 600
inimigo_y = 100

# Velocidade do personagem
velocidade = 5

# Lista para armazenar inimigos
inimigos = []
num_inimigos = 10  # Quantidade de inimigos

# Criar inimigos aleatórios
for _ in range(num_inimigos):
    inimigo_x = random.randint(0, largura - 64)
    inimigo_y = random.randint(0, altura - 64)
    inimigos.append([inimigo_x, inimigo_y, random.choice([1, 2, 3])])  # A última posição é a velocidade do inimigo

# Controle de ataque e posição da espada
espada_mostrada = False  # Espada aparece apenas ao atacar
direcao_ataque = "right"

# Função para desenhar a espada conforme a direção do ataque
def desenhar_espada():
    global espada_x, espada_y

    if direcao_ataque == "right":
        espada_x = personagem_x + 70
        espada_y = personagem_y + 16
    elif direcao_ataque == "left":
        espada_x = personagem_x - 32
        espada_y = personagem_y + 16
    elif direcao_ataque == "up":
        espada_x = personagem_x + 16
        espada_y = personagem_y - 32
    elif direcao_ataque == "down":
        espada_x = personagem_x + 16
        espada_y = personagem_y + 70

    # Desenhar a espada
    screen.blit(espada, (espada_x, espada_y))

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Capturar teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        personagem_x -= velocidade
        direcao_ataque = "left"
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        personagem_x += velocidade
        direcao_ataque = "right"
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        personagem_y -= velocidade
        direcao_ataque = "up"
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        personagem_y += velocidade
        direcao_ataque = "down"

    # Verificar se a barra de espaço está sendo pressionada para atacar
    if teclas[pygame.K_SPACE]:
        espada_mostrada = True  # Mostra a espada
    else:
        espada_mostrada = False  # Esconde a espada quando o botão é liberado

    # Desenhar a imagem de fundo
    screen.blit(fundo, (0, 0))

    # Desenhar o personagem na tela
    screen.blit(personagem, (personagem_x, personagem_y))

        # Movimentar e desenhar os inimigos
    for inimigo in inimigos:
        inimigo_x, inimigo_y, velocidade_inimigo = inimigo

        # Movimentar o inimigo na direção do personagem
        if inimigo_x > personagem_x:
            inimigo_x -= velocidade_inimigo
        elif inimigo_x < personagem_x:
            inimigo_x += velocidade_inimigo
        if inimigo_y > personagem_y:
            inimigo_y -= velocidade_inimigo
        elif inimigo_y < personagem_y:
            inimigo_y += velocidade_inimigo

        # Desenhar o inimigo
        screen.blit(inimigo_img, (inimigo_x, inimigo_y))

        # Atualizar a posição do inimigo na lista
        inimigo[0] = inimigo_x
        inimigo[1] = inimigo_y

        # Colisão entre a espada e o inimigo
        if espada_mostrada:
            desenhar_espada()  # Desenha a espada na direção correta
            if (espada_x + 40 > inimigo_x and espada_x < inimigo_x + 64) and (espada_y + 40 > inimigo_y and espada_y < inimigo_y + 64):
                # "Destrói" o inimigo ao movê-lo para fora da tela
                inimigo[0], inimigo[1] = -1000, -1000

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(120)