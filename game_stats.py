class GameStats():
    """Armazena dados estatisticos da invasao alienigena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

        #A pontuacao maxima jamais devera ser reiniciada
        self.high_score = 0
        
        #Inicia o jogo em um estado inativo
        self.game_active = False
        
    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1