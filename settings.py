class Settings():
    """Uma classe para armazenar todas as configuracoes da Invasao Alienigena."""

    def __init__(self):
        """"Inicializa as configuracoes do jogo."""
        #Configuracoes da tela
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (255, 255, 255)

        #Configuracoes da espaconave
        self.ship_limit = 3

        #Configuracoes dos projeteis
        self.bullet_width = 1200 #era 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4

        #Configuracoes dos alienigenas
        self.fleet_drop_speed = 10

        #A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        #A taxa com que os pontos para cada alienigena aumenta
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configuracoes que mudam nodecorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.7
        self.alien_points = 50  #Pontos por alienigena

        #fleet_direction igual a 1 representa a direita, -1 representa a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configuracoes de velocidade e os pontos para cada alienigena"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)