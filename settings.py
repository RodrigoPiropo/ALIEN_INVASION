class Settings:
    """Uma classe para armazenar todas as configurações do jogo"""

    def __init__(self):
        """Inicializa  as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configuraçoes dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configurações dos alienigenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 reoresenta a direita; -1 esquerda
        self.fleet_direction = 1
