import sys
import pygame

def check_events(ship):
	""" mouse and keyboard """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True


		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
				
				#move the ship right
				# ship.rect.centerx +=1

def update_screen(ai_settings,screen,ship):
	""" update screen and flip the new screen """

	#redraw the screen

	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#make the most recent screen visible
	pygame.display.flip()