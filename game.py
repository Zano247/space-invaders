import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria o botao play
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma espaconave
    ship = Ship(ai_settings, screen)

    #Cria um grupo no qual serao armazenados os projeteis e os aliens
    bullets = Group()
    aliens = Group()

    #Cria um alienigena
    alien = Alien(ai_settings, screen)

    #Cria uma frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Cria uma instancia para armazenar dados estatisticos do jogo e cria painel de pontuacao
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Inicia o laco principal do jogo
    while True: 

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()