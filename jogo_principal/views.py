# import pygame
# import sys
# from classes import *

# # Iniciando pygame
# pygame.init()

# def criar_fundo(img, largura, altura):
#     # imagem de fundo
#     fundo = pygame.image.load(img)
#     # ajustando tamanho do fundo
#     fundo = pygame.transform.scale(fundo, (largura, altura))

#     return fundo

# def criar_personagem(img, largura, altura, pos_x, pos_y, vida, velocidade, dano):
#     personagem = Personagens(img, largura, altura, pos_x, pos_y, vida, velocidade, dano)
#     # imagem do personagem
#     personagem.img = pygame.image.load(personagem.img)
#     # ajustando tamanho do personagem
#     personagem.img = pygame.transform.scale(personagem.img, (largura, altura))

#     return personagem

# #tela principal
# def tela():

#     # Definindo o tamanho da janela
#     largura = 1200
#     altura = 800
#     screen = pygame.display.set_mode((largura, altura))
#     # Titulo da janela
#     pygame.display.set_caption("Dungeon")

#     # recebendo img de fundo
#     fundo_atual = criar_fundo("Estruturas/Map/Rooms/Room1_dungeon.png", largura, altura)
#     # recebendo img do heori
#     heroi = criar_personagem("Estruturas/Hero/spr_hero_idle0.png", 60, 60, 550, 400, 100, 5, 20)

#     # controlador
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Capturar teclas pressionadas
#         teclas = pygame.key.get_pressed()

#         if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
#             heroi.pos_x -= heroi.velocidade
#             direcao_ataque = "left"
#         if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
#             heroi.pos_x += heroi.velocidade
#             direcao_ataque = "right"
#         if teclas[pygame.K_UP] or teclas[pygame.K_w]:
#             heroi.pos_y -= heroi.velocidade
#             direcao_ataque = "up"
#         if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
#             heroi.pos_y += heroi.velocidade
#             direcao_ataque = "down"

#         # Desenhar a imagem de fundo
#         screen.blit(fundo_atual, (0, 0))

#         # Desenhar o personagem na tela
#         screen.blit(heroi.img, (heroi.pos_x, heroi.pos_y))

#         # Atualizar a tela
#         pygame.display.flip()

#         # Controlar a taxa de quadros
#         pygame.time.Clock().tick(120)

# tela()




import pygame
import sys
from classes import *

# Iniciando pygame
pygame.init()

def criar_fundo(img, largura, altura):
    # imagem de fundo
    fundo = pygame.image.load(img)
    # ajustando tamanho do fundo
    fundo = pygame.transform.scale(fundo, (largura, altura))

    return fundo

def criar_personagem(img, largura, altura, pos_x, pos_y, vida, velocidade, dano):
    personagem = Personagens(img, largura, altura, pos_x, pos_y, vida, velocidade, dano)
    # imagem do personagem
    personagem.img = pygame.image.load(personagem.img)
    # ajustando tamanho do personagem
    personagem.img = pygame.transform.scale(personagem.img, (largura, altura))

    return personagem

# Função para carregar e ajustar a espada
def carregar_espada(img_path, largura, altura):
    espada = pygame.image.load(img_path)
    espada = pygame.transform.scale(espada, (largura, altura))
    return espada

# Função para rotacionar a espada de acordo com a direção
def rotacionar_espada(espada_img, direcao):
    if direcao == "right":
        return pygame.transform.rotate(espada_img, 0)
    elif direcao == "left":
        # Espelhar a imagem da espada horizontalmente
        return pygame.transform.flip(espada_img, True, False)
    elif direcao == "up":
        return pygame.transform.rotate(espada_img, 90)
    elif direcao == "down":
        return pygame.transform.rotate(espada_img, -90)

# Tela principal
def tela():
    # Definindo o tamanho da janela
    largura = 1200
    altura = 800
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Dungeon")

    # Recebendo imagem de fundo
    fundo_atual = criar_fundo("Estruturas/Map/Rooms/Room1_dungeon.png", largura, altura)
    # Recebendo imagem do herói
    heroi = criar_personagem("Estruturas/Hero/spr_hero_idle0.png", 60, 60, 550, 400, 100, 5, 20)

    # Carregando as imagens da espada
    espada_idle = carregar_espada("Estruturas/Items/Weapons/spr_sword_attack0.png", 40, 40)
    espada_ataque = carregar_espada("Estruturas/Items/Weapons/spr_sword_attack1.png", 40, 40)
    espada_img_atual = espada_idle

    # Direção inicial da espada
    direcao_ataque = "right"
    atacando = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Capturar teclas pressionadas
        teclas = pygame.key.get_pressed()

        # Movimentação e direção
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            heroi.pos_x -= heroi.velocidade
            direcao_ataque = "left"
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            heroi.pos_x += heroi.velocidade
            direcao_ataque = "right"
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            heroi.pos_y -= heroi.velocidade
            direcao_ataque = "up"
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            heroi.pos_y += heroi.velocidade
            direcao_ataque = "down"

        # Verificar se a barra de espaço foi pressionada
        if teclas[pygame.K_SPACE]:
            espada_img_atual = espada_ataque
            atacando = True
        else:
            espada_img_atual = espada_idle
            atacando = False

        # Rotacionar ou espelhar a espada de acordo com a direção do ataque
        espada_img_rotacionada = rotacionar_espada(espada_img_atual, direcao_ataque)

        # Desenhar a imagem de fundo
        screen.blit(fundo_atual, (0, 0))

        # Desenhar o personagem na tela
        screen.blit(heroi.img, (heroi.pos_x, heroi.pos_y))

        # Desenhar a espada
        if direcao_ataque == "right":
            screen.blit(espada_img_rotacionada, (heroi.pos_x + 25, heroi.pos_y + 10))
        elif direcao_ataque == "left":
            screen.blit(espada_img_rotacionada, (heroi.pos_x - 5, heroi.pos_y + 10))
        elif direcao_ataque == "up":
            screen.blit(espada_img_rotacionada, (heroi.pos_x + 13, heroi.pos_y - 6))
        elif direcao_ataque == "down":
            screen.blit(espada_img_rotacionada, (heroi.pos_x + 15, heroi.pos_y + 26))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        pygame.time.Clock().tick(120)

tela()
