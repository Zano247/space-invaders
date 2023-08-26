import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um unico alienigena na frota."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienigena e defina sua posicao inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('Imagens/ship.bmp')
        self.rect = self.image.get_rect()

        #Mudar o tamanho do alienigena
        new_width = self.image.get_width() // 2
        new_height = self.image.get_height() // 2
        self.image = pygame.transform.scale(self.image, (new_width, new_height))


        #Inicia cada novo alienigena proximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #Armazena a posicao exata do alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienigena em sua posicao atual."""
        self.screen.blit(self.image, self.rect)