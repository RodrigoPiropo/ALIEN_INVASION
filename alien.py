import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienigena da frota"""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define a sua posição inicial."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('ufo.png')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienigena próximo à parte superior esquerda da tela (0, 0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienigena em sua posição atual"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Devolve True se o alien estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienigena para a direita."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
