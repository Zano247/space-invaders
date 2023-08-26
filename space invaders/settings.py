class Settings():
    """Uma classe para armazenar todas as configuracoes da Invasao Alienigena."""

    def __init__(self):
        """"Inicializa as configuracoes do jogo."""
        #Configuracoes da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        #Configuracoes da espaconave
        self.ship_speed_factor = 1.5

        #Configuracoes dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4