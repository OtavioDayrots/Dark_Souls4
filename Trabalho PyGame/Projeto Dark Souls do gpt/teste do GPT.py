import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800  # Largura da tela
screen_height = 600  # Altura da tela
screen = pygame.display.set_mode((screen_width, screen_height))  # Cria a tela
pygame.display.set_caption("Animação de Movimento")  # Título da janela

# Cores
BLACK = (0, 0, 0)  # Define a cor preta

# Fator de escala para o personagem
scale_factor = 1.75  # Ajuste para aumentar ou diminuir o tamanho do personagem

# Configurações do personagem
class Player:
    def __init__(self):
        
        # Carrega e escala as imagens de idle para a esquerda
        self.images_idle_left = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                  pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle1.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        # Carrega e escala as imagens de idle para a direita
        self.images_idle_right = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightidle0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                   pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightidle1.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        # Carrega e escala as imagens de corrida para a esquerda
        self.images_run_left = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun1.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun2.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun3.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        # Carrega e escala as imagens de corrida para a direita
        self.images_run_right = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightrun0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                 pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightrun1.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                 pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightrun2.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                 pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_rightrun3.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        self.images_idle_top = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                  pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle1.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        

        # Define a imagem inicial e a posição do personagem
        self.image = self.images_idle_right[0]
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))  # Centraliza o personagem
        self.speed = 5  # Velocidade do personagem
        self.direction = "right"  # Direção inicial
        self.is_running = False  # Indica se o personagem está correndo
        self.idle_frame = 0  # Contador de frames para animação de idle
        self.run_frame = 0  # Contador de frames para animação de corrida
        self.clock = pygame.time.Clock()  # Controle de FPS
        self.frame_counter = 0  # Contador de frames para animações
        self.run_frame_counter = 0  # Contador específico para animação de corrida

    def update(self):
        keys = pygame.key.get_pressed()  # Captura as teclas pressionadas
        self.is_running = False  # Reseta o estado de corrida

        # Movimenta o personagem baseado nas teclas pressionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed  # Move para a esquerda
            self.direction = "left"  # Atualiza a direção
            self.is_running = True  # Indica que está correndo
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed  # Move para a direita
            self.direction = "right"  # Atualiza a direção
            self.is_running = True  # Indica que está correndo
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed  # Move para cima
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed  # Move para baixo

        # Atualiza a imagem com base no estado de corrida
        if self.is_running:
            self.run_frame_counter += 1  # Incrementa o contador de frames de corrida
            if self.run_frame_counter >= 5:  # Controla a velocidade da animação
                if self.direction == "left":
                    self.image = self.images_run_left[self.run_frame % len(self.images_run_left)]  # Atualiza imagem de corrida para a esquerda
                else:
                    self.image = self.images_run_right[self.run_frame % len(self.images_run_right)]  # Atualiza imagem de corrida para a direita
                self.run_frame += 1  # Avança para o próximo frame
                self.run_frame_counter = 0  # Reseta o contador de frames de corrida
        else:
            self.run_frame_counter = 0  # Reseta o contador de corrida quando não está correndo
            # Atualiza a imagem de idle com base na direção
            if self.direction == "left":
                self.image = self.images_idle_left[self.idle_frame % len(self.images_idle_left)]
                self.frame_counter += 1  # Incrementa o contador de frames de idle
                if self.frame_counter >= 10:
                    self.idle_frame += 1  # Avança para o próximo frame de idle
                    self.frame_counter = 0  # Reseta o contador
            else:
                self.image = self.images_idle_right[self.idle_frame % len(self.images_idle_right)]
                self.frame_counter += 1  # Incrementa o contador de frames de idle
                if self.frame_counter >= 10:
                    self.idle_frame += 1  # Avança para o próximo frame de idle
                    self.frame_counter = 0  # Reseta o contador

        # Reseta os frames quando chega no fim da animação
        if not self.is_running:
            if self.idle_frame >= len(self.images_idle_left):
                self.idle_frame = 0  # Reseta o contador de idle
        else:
            if self.run_frame >= len(self.images_run_left):
                self.run_frame = 0  # Reseta o contador de corrida

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Desenha o personagem na tela

# Loop principal do jogo
def main():
    player = Player()  # Cria uma instância do jogador

    while True:  # Loop principal do jogo
        for event in pygame.event.get():  # Processa eventos
            if event.type == pygame.QUIT:
                pygame.quit()  # Fecha o Pygame
                sys.exit()  # Sai do sistema

        # Atualiza o estado do jogador
        player.update()

        # Preenche a tela com a cor preta
        screen.fill(BLACK)

        # Desenha o jogador
        player.draw(screen)

        # Atualiza a tela
        pygame.display.flip()  # Atualiza o display
        player.clock.tick(30)  # Controla a taxa de quadros por segundo

if __name__ == "__main__":
    main()  # Chama a função principal
