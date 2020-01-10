import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Inicializa o jogo e cria um objeto na tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Cria o botão play
    play_button = Button(ai_settings, screen, "Play")

    # Cria uma instância para armazenar dados estatisticos do jogo e cria o painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave, um grupo de projeteis e um grupo de aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # MUSICA DE FUNDO
    pygame.mixer.music.load('Star Wars.mp3')
    pygame.mixer.music.play(-1)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
