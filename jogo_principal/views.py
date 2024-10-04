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

#tela principal
def tela():

    # Definindo o tamanho da janela
    largura = 1200
    altura = 800
    screen = pygame.display.set_mode((largura, altura))
    # Titulo da janela
    pygame.display.set_caption("Dungeon")

    # recebendo img de fundo
    fundo_atual = criar_fundo("Estruturas/Map/Rooms/Room1_dungeon.png", largura, altura)
    # recebendo img do heori
    heroi = criar_personagem("Estruturas/Hero/spr_hero_idle0.png", 60, 60, 550, 400, 100, 5, 20)

    # controlador
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Capturar teclas pressionadas
        teclas = pygame.key.get_pressed()

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

        # Desenhar a imagem de fundo
        screen.blit(fundo_atual, (0, 0))

        # Desenhar o personagem na tela
        screen.blit(heroi.img, (heroi.pos_x, heroi.pos_y))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de quadros
        pygame.time.Clock().tick(120)

tela()