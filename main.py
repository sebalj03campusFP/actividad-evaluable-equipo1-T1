# main.py
# Bucle principal del juego "Galaxy Defenders"

import pygame
import sys

# Importamos todo lo necesario de nuestros módulos
from config import *
from player import Player
from enemies import spawn_wave
from game_logic import handle_collisions, check_game_over, check_wave_cleared

# --- Función para dibujar texto en la pantalla ---
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(None, size) # Usar fuente por defecto
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# --- Función principal del juego ---
def main_game_loop():
    
    # --- Inicialización ---
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    # --- Variables de estado del juego ---
    game_state = {
        "score": 0,
        "lives": 3
    }
    game_over = False

    # --- Creación de Grupos de Sprites ---
    # Grupo para TODOS los sprites (para dibujarlos y actualizarlos)
    all_sprites = pygame.sprite.Group()
    # Grupo solo para los enemigos
    enemies_group = pygame.sprite.Group()
    # Grupo solo para las balas del jugador
    player_bullets_group = pygame.sprite.Group()

    # --- Creación del Jugador ---
    # Pasamos los grupos al jugador para que pueda añadir sprites (balas)
    player = Player(all_sprites, player_bullets_group)
    all_sprites.add(player)

    # --- Creación de la primera oleada de enemigos ---
    spawn_wave(all_sprites, enemies_group)


    # ==================================================================
    # === BUCLE PRINCIPAL DEL JUEGO ====================================
    # ==================================================================
    running = True
    while running:
        # Mantener el bucle a la velocidad correcta
        clock.tick(FPS)
        
        # --- 1. Manejo de Eventos (Input) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            # Evento de tecla presionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.shoot()
                
                # Reiniciar el juego si está en "Game Over"
                if event.key == pygame.K_r and game_over:
                    main_game_loop() # Vuelve a empezar la función principal


        if not game_over:
            # --- 2. Actualización (Update) ---
            # Llama al método .update() de CADA sprite en el grupo
            all_sprites.update()
            
            # --- 3. Lógica del Juego (Colisiones, etc.) ---
            game_state = handle_collisions(player, enemies_group, player_bullets_group, game_state)
            
            # Comprobar si se acabó la oleada
            if check_wave_cleared(enemies_group):
                spawn_wave(all_sprites, enemies_group) # ¡Nueva oleada!
            
            # Comprobar si el juego ha terminado
            if check_game_over(game_state):
                game_over = True
                player.kill() # Elimina al jugador de la pantalla

        # --- 4. Dibujado (Render) ---
        screen.fill(BLACK) # Limpiar la pantalla
        all_sprites.draw(screen) # Dibujar todos los sprites

        # Dibujar la Interfaz de Usuario (UI)
        draw_text(screen, f"Puntuación: {game_state['score']}", 24, SCREEN_WIDTH // 2, 10, WHITE)
        draw_text(screen, f"Vidas: {game_state['lives']}", 24, 60, 10, WHITE)

        # Pantalla de Game Over
        if game_over:
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED)
            draw_text(screen, "Presiona 'R' para reiniciar", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, WHITE)


        # Actualizar la pantalla
        pygame.display.flip()

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main_game_loop()
