import pygame
from setting import Setting
from ship import Ship
import game_function as gf

def run_game():
    #初始化游戏，创建屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_heigth))
    pygame.display.set_caption("alien_invasion") 

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #开始游戏主循环
    while True:

        #监视键鼠
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()