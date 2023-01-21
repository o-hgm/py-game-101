import pygame


def create_game_window(screen_width: int = 800, screen_height: int = 600) -> pygame.Surface:
    # Inicializar pygame
    pygame.init()

    # Crear la pantalla
    game_screen = pygame.display.set_mode((screen_width, screen_height))

    # Título de la ventana
    pygame.display.set_caption("Arkanoid")

    return game_screen

def run_event_loop():
    # Bucle principal del juego
    event_loop = True
    while event_loop:
        # Procesar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event_loop = False