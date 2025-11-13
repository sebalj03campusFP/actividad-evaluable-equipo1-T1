import pygame
from config import *

class Player(pygame.sprite.Sprite):
    """ Clase para la nave del jugador """
    def __init__(self, all_sprites, player_bullets):
        super().__init__()
        
        # Guardamos los grupos de sprites para usarlos al disparar
        self.all_sprites = all_sprites
        self.player_bullets = player_bullets

        # Creamos la imagen del jugador (un simple rectángulo verde)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        
        # Posición inicial
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

    def update(self):
        """ Actualiza la posición del jugador basado en las teclas presionadas """
        
        # Obtener el estado actual de todas las teclas
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Mantener al jugador dentro de la pantalla
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        """ Crea un nuevo proyectil en la posición del jugador """
        projectile = Projectile(self.rect.centerx, self.rect.top)
        self.all_sprites.add(projectile)
        self.player_bullets.add(projectile)


class Projectile(pygame.sprite.Sprite):
    """ Clase para los proyectiles disparados por el jugador """
    def __init__(self, x, y):
        super().__init__()
        
        # Creamos la imagen del proyectil (un pequeño rectángulo blanco)
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
        # Posición inicial (basada en el jugador)
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        """ Mueve el proyectil hacia arriba """
        self.rect.y -= PROJECTILE_SPEED
        
        # Eliminar el proyectil si sale de la pantalla (para no consumir memoria)
        if self.rect.bottom < 0:
            self.kill()
