# game_logic.py
# Funciones para manejar colisiones y el estado del juego

import pygame

def handle_collisions(player, enemies_group, player_bullets_group, game_state):
    """ Maneja todas las colisiones del juego """
    
    # 1. Colisión: Balas del jugador contra enemigos
    #    groupcollide() detecta colisiones entre dos grupos.
    #    Los 'True' significan que tanto la bala como el enemigo se eliminan.
    hits = pygame.sprite.groupcollide(enemies_group, player_bullets_group, True, True)
    
    # Por cada enemigo golpeado, sumamos puntos
    for hit in hits:
        game_state["score"] += 100
        # Aquí se podría añadir un sonido de explosión

    # 2. Colisión: Enemigos contra el jugador
    #    spritecollide() detecta colisiones entre un sprite y un grupo.
    #    'True' significa que el enemigo se elimina al chocar.
    hits = pygame.sprite.spritecollide(player, enemies_group, True)
    
    if hits:
        game_state["lives"] -= 1
        # Aquí se podría añadir un sonido de jugador golpeado
        # y quizás hacer al jugador invencible por unos segundos.

    return game_state


def check_game_over(game_state):
    """ Comprueba si el juego ha terminado """
    if game_state["lives"] <= 0:
        return True
    return False


def check_wave_cleared(enemies_group):
    """ Comprueba si todos los enemigos de la oleada han sido eliminados """
    if not enemies_group: # Si el grupo de enemigos está vacío
        return True
    return False
