import pygame
import random
from defs import *

class Enemy():

	def __init__(self, gameDisplay, x, y):
		self.gameDisplay = gameDisplay
		self.state = enemy_moving
		self.enemy = pygame.Surface((enemy_w+2, enemy_h+2), pygame.SRCALPHA)
		self.x = x
		self.y = y
		self.pointlist = [(0, enemy_h), (enemy_w, enemy_h), (enemy_w/2, 0), (0,enemy_h)]
		self.triangle = pygame.draw.polygon(self.enemy, black, self.pointlist)
		self.triangle_c = pygame.draw.polygon(self.enemy, red, self.	pointlist, 2)
		self.set_position(x, y)

	def set_position(self, x, y):
		self.triangle.left = x
		self.triangle.top = y

	def move_position(self, dx, dy):
		self.triangle.centerx += dx
		self.triangle.centery += dy

	def draw(self):
		self.gameDisplay.blit(self.enemy, (self.triangle.centerx, self.triangle.centery))

	def check_status(self):
		if self.triangle.right < 0:
			self.state = enemy_done

	def update(self, dt):
		if self.state == enemy_moving:
			self.move_position(-(enemy_speed * dt), 0)
			self.draw()
			self.check_status()


class EnemyCollection():

	def __init__(self, gameDisplay):
		self.gameDisplay = gameDisplay
		self.enemies = []

	def add_new_enemy(self, x):
		rand_x = random.randint(enemy_min_gap, enemy_gap_size)

		en1 = Enemy(self.gameDisplay, x+rand_x, enemy_y)

		self.enemies.append(en1)

	def create_new_set(self):
		self.enemies = []
		placed = enemy_first

		while placed < screen_w:
			self.add_new_enemy(placed)
			placed += enemy_min_gap

	def update(self, dt):
		rightmost = 0

		for e in self.enemies:
			e.update(dt)
			if e.triangle.left > rightmost:
				rightmost = e.triangle.left
		#print(rightmost)
		if rightmost < screen_w:
			self.add_new_enemy(screen_w)

		self.enemies = [e for e in self.enemies if e.state == enemy_moving]

