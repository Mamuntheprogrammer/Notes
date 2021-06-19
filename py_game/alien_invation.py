import sys
import pygame

from setting import Settings
from ship import Ship 
import game_functions as gf

def run_game():
	""" Inital screen setup """
	pygame.init()


	# object of setting class 

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

	# screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("PyGems Shooting Game")

	#make a ship 
	ship = Ship(screen)

	#set the background color
	# bg_color = (230,230,230)

	#start main loop for the games
	while True:

		#watch for the keyboard and mouse event
		gf.check_events(ship)
		ship.update()

		gf.update_screen(ai_settings,screen,ship)

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		screen.fill(ai_settings.bg_color)
		ship.blitme()

		#make the most recently drawn screen visible
		pygame.display.flip()

run_game()