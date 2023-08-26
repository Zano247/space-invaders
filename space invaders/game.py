import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria uma espaconave
    ship = Ship(ai_settings, screen)

    #Cria um grupo no qual serao armazenados os projeteis e os aliens
    bullets = Group()
    aliens = Group()

    #Cria um alienigena
    alien = Alien(ai_settings, screen)

    #Cria uma frota de alienigenas
    gf.create_fleet(ai_settings, screen, aliens)
    
    #Inicia o laco principal do jogo
    while True: 

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()