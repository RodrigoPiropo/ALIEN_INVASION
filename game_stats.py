class GameStats:
    """Armazena dados estatisticos da invasão alienigena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicia a invasao alienigena em um estado ativo
        self.game_active = True

        # Inicia o jogo em um estado inativo
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
