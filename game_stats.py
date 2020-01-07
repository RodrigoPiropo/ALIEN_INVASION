class GameStats:
    """Armazena dados estatisticos da invasão alienigena"""

    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Inicia a invasao alienigena em um estado ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar durante o jogo."""
        self.ship_left = self.ai_settings.ship_limit
