import pygame
import random
from defs import *

class Player():

	def __init__(self, gameDisplay):
		self.gameDisplay = gameDisplay
		self.state = player_alive
		self.player = pygame.Surface((player_w, player_h))
		self.square = pygame.draw.rect(self.player, blue, (0,0,30,50))
		self.square_c = pygame.draw.rect(self.player, turq, (0,0,30,50), 3)
		self.speed = 0
		self.time_lived = 0
		self.jumpCount = 9
		self.isJump = False
		self.set_position(player_start_x, player_start_y)

	def set_position(self, x, y):
		self.square.left = x
		self.square.top = y

	def jump(self):
		if self.jumpCount >= -9:
			neg = 1
			if self.jumpCount < 0:
				neg = -1
			# Math equation
			self.square.bottom -= ((self.jumpCount ** 2) * neg)
			self.jumpCount -= 1
		else:
			self.isJump = False
			self.jumpCount = 9

	def draw(self):
		self.gameDisplay.blit(self.player, (self.square.centerx, self.square.centery))

	def check_collision(self, enemies):
		for e in enemies:
			if e.triangle.colliderect(self.square):
				self.state = player_dead
				break

	def update(self, dt, enemies):
		if self.state == player_alive:
			self.time_lived += dt
			self.draw()
			self.check_collision(enemies)


class PlayerCollection():

	def __init__(self, gameDisplay):
		self.gameDisplay = gameDisplay
		self.players = []
		self.create_new_generation()

	def create_new_generation(self):
		self.players = []
		for i in range(0, generation_size):
			self.players.append(Player(self.gameDisplay))

	def update(self, dt, enemies):
		num_alive = 0
		for p in self.players:
			if random.randint(0,1) == 1:
				p.jump()
			p.update(dt, enemies)
			if p.state == player_alive:
				num_alive += 1

		return num_alive
		