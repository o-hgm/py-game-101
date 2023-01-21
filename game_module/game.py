from typing import Tuple

import pygame

class Game:
    DEFAULT_WIDTH: int = 800
    DEFAULT_HEIGHT: int = 600
    DEFAULT_SURFACE_BACKGROUND = (0, 0, 0)

    WINDOW_TITLE = 'My Game'

    def __init__(self) -> None:
        # Inicializar pygame
        self.game_window: pygame.Surface = None
        self.has_event_loop: bool = False
        self.screen_width: int = 0
        self.screen_height: int = 0
    
    def get_screen_dimension(self) -> Tuple[int, int]:
        return (self.screen_width, self.screen_height)

    def initialize(self, screen_width: int = DEFAULT_WIDTH, screen_height: int = DEFAULT_HEIGHT) -> None:
        pygame.init()
        pygame.display.set_caption(Game.WINDOW_TITLE)
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.game_window = pygame.display.set_mode(self.get_screen_dimension())

    def loop(self):
        self.has_event_loop = True
        while self.has_event_loop:
            # Procesar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.has_event_loop = False
            
            self.refresh_screen()



    def refresh_screen(self):
        self.game_window.fill(Game.DEFAULT_SURFACE_BACKGROUND)
        # Variables para controlar la posición de la barra
        bar_x = self.screen_width // 2
        bar_y = self.screen_height - 20
        bar_width = 100
        bar_height = 10
        bar_speed = 5

        # Variables para controlar la posición de la pelota
        ball_x = self.screen_width // 2
        ball_y = self.screen_height // 2
        ball_radius = 10
        ball_speed_x = 3
        ball_speed_y = -3
        pygame.draw.rect(self.game_window, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.circle(self.game_window, (255, 255, 255), (ball_x, ball_y), ball_radius)
        pygame.display.update()

    pygame.display.set_caption("Arkanoid")


def create_game_instance():
    game_instance = Game()
    
    return game_instance