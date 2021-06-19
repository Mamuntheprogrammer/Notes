import pygame

class Ship():
	def __init__(self,screen):
		""" initializing the ship and its starting point on the scrren """
		self.screen = screen
		#load the image
		self.image = pygame.image.load('image/shipx.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start each new ship at the bottom center of the screen

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom 


		#movement flag 
		self.moving_right = False
		self.moving_left = False

	
	def blitme(self):
		""" draw the ship in curent location """
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.moving_right:
			self.rect.centerx +=1
		if self.moving_left:
			self.rect.centerx -=1
