import pygame
import sys
import os

# centraliza a tela
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animação de Movimento")

# Fator de escala para o personagem
scale_factor = 1.5

# Configurações do personagem
class Player:
    def __init__(self):
        # Carrega e escala as imagens de idle para a esquerda
        self.images_idle_left = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                  pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle1.png"), (int(64 * scale_factor), int(64 * scale_factor)))]
        
        # Carrega e escala as imagens de idle para a direita (espelhadas)
        self.images_idle_right = [pygame.transform.flip(img, True, False) for img in self.images_idle_left]

        # Carrega e escala as imagens de corrida para a esquerda
        self.images_run_left = [pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun1.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun2.png"), (int(64 * scale_factor), int(64 * scale_factor))),
                                pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftrun3.png"), (int(64 * scale_factor), int(64 * scale_factor)))]

        # Carrega e escala as imagens de corrida para a direita (espelhadas)
        self.images_run_right = [pygame.transform.flip(img, True, False) for img in self.images_run_left]

        # Carrega e escala as imagens de corrida para cima
        self.images_idle_up =  [pygame.transform.flip(img, True, False) for img in self.images_idle_left]

        # Carrega e escala as imagens de corrida para baixo
        self.images_run_down = [
            pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle0.png"), (int(64 * scale_factor), int(64 * scale_factor))),
            pygame.transform.scale(pygame.image.load("Trabalho PyGame/Projeto Dark Souls do gpt/spr_hero_leftidle1.png"), (int(64 * scale_factor), int(64 * scale_factor)))
        ]

        # Inicializa a imagem e a posição do personagem
        self.image = self.images_idle_right[0]
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.speed = 7
        self.direction = "right"
        self.is_running = False
        self.idle_frame = 0
        self.run_frame = 0
        self.clock = pygame.time.Clock()
        self.frame_counter = 0
        self.run_frame_counter = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_running = False

        # Determina a direção com base nas teclas pressionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"
            self.is_running = True
            
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"
            self.is_running = True
            
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.is_running = True
            
            # Verifica a direção de acordo com as teclas pressionadas
            if keys[pygame.K_LEFT]:
                self.direction = "left"  # Subindo para a esquerda
            elif keys[pygame.K_RIGHT]:
                self.direction = "right"  # Subindo para a direita
            else:
                self.direction = "left"  # Subindo sem direção lateral (vira para a esquerda)

        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.is_running = True
            
            if not keys[pygame.K_RIGHT]  and  not keys[pygame.K_LEFT]:
                self.direction = "right"  # Somente para baixo, vira para a esquerda
            

        # Atualiza as animações
        if self.is_running:
            self.run_frame_counter += 1
            if self.run_frame_counter >= 5:
                if self.direction == "left":
                    self.image = self.images_run_left[self.run_frame % len(self.images_run_left)]
                elif self.direction == "right":
                    self.image = self.images_run_right[self.run_frame % len(self.images_run_right)]
                elif self.direction == "up":
                    self.image = self.images_run_up[self.run_frame % len(self.images_run_up)]
                elif self.direction == "down":
                    self.image = self.images_run_down[self.run_frame % len(self.images_run_down)]
                
                self.run_frame += 1
                self.run_frame_counter = 0
        else:
            self.run_frame_counter = 0
            if self.direction == "left":
                self.image = self.images_idle_left[self.idle_frame % len(self.images_idle_left)]
                self.frame_counter += 1
                if self.frame_counter >= 10:
                    self.idle_frame += 1
                    self.frame_counter = 0
            else:
                self.image = self.images_idle_right[self.idle_frame % len(self.images_idle_right)]
                self.frame_counter += 1
                if self.frame_counter >= 10:
                    self.idle_frame += 1
                    self.frame_counter = 0

        if not self.is_running:
            if self.idle_frame >= len(self.images_idle_left):
                self.idle_frame = 0
        else:
            if self.run_frame >= len(self.images_run_left):
                self.run_frame = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def criar_fundo(img, largura, altura):
    # imagem de fundo
    fundo = pygame.image.load(img)
    # ajustando tamanho do fundo
    fundo = pygame.transform.scale(fundo, (largura, altura))

    return fundo
# Loop principal do jogo
def main():
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()
        fundo_atual = criar_fundo("Estruturas/Map/Rooms/Room1_dungeon.png", screen_width, screen_height)
        screen.blit(fundo_atual, (0, 0))
        player.draw(screen)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        pygame.display.flip()
        player.clock.tick(120)

if __name__ == "__main__":
    main()