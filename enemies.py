# enemies.py
# Define la clase Enemy y la función para generar oleadas

import pygame
from config import *

class Enemy(pygame.sprite.Sprite):
    """ Clase para las naves enemigas """
    def __init__(self, x, y):
        super().__init__()
        
        # Creamos la imagen del enemigo (un simple rectángulo rojo)
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # Posición inicial (pasada por la función de oleada)
        self.rect.x = x
        self.rect.y = y
        self.speed_x = ENEMY_SPEED

    def update(self):
        """ Mueve al enemigo """
        # Movimiento simple: de lado a lado
        self.rect.x += self.speed_x
        
        # Invertir dirección si toca los bordes y bajar un poco
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x *= -1
            self.rect.y += 15 # Bajan un poco al tocar el borde


def spawn_wave(all_sprites, enemies_group):
    """ Función para crear una oleada de enemigos """
    print("¡Nueva oleada de enemigos!")
    for row in range(3):
        for col in range(8):
            # Calculamos la posición para cada enemigo en la cuadrícula
            x = col * 80 + 70  # Espaciado horizontal
            y = row * 50 + 50  # Espaciado vertical
            
            enemy = Enemy(x, y)
            all_sprites.add(enemy)
            enemies_group.add(enemy)

            