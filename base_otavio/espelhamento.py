import os
import pygame
import sys
import random


image = pygame.image.load('minha_imagem.png')

# Espelhar a imagem horizontalmente (True para espelhamento horizontal, False para vertical)
flipped_image = pygame.transform.flip(image, True, False)
