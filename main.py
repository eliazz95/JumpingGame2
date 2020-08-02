import pygame
from defs import *
from enemy import EnemyCollection
from player import PlayerCollection
import time

def update_label(data, title, font, x, y, gameDisplay):
	label = font.render("{} {}".format(title, data), 1, font_color)
	gameDisplay.blit(label, (x, y))
	return y

def update_data_labels(gameDisplay, dt, game_time, font, num_of_iterations, num_alive):
	y_pos = 10
	gap = 20
	x_pos = 10
	y_pos = update_label(round(1000/dt, 2), "FPS: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(round(game_time/1000, 2), "Game Time: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(num_of_iterations, "Iterations: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(num_alive, "Alive: ", font, x_pos, y_pos + gap, gameDisplay)

def printMSG(gameDisplay, msg, x, y, size):
	# Define font and size
	font = pygame.font.Font(None, size)
	# Define what message to display and it's color
	text_surface = font.render(msg, True, (0, 0, 0))
	# Print the message to screen using coordinates
	gameDisplay.blit(text_surface, (x,y))
	#pygame.time.delay(2000)
	#time.sleep(1)

def main():

	pygame.init()
	gameDisplay = pygame.display.set_mode((screen_w, screen_h))
	pygame.display.set_caption("Jumping Game Neural Nets!")

	running = True
	label_font = pygame.font.Font(None, font_size)

	clock = pygame.time.Clock()
	dt = 0
	game_time = 0
	num_of_iterations = 1

	enemy = EnemyCollection(gameDisplay)
	enemy.create_new_set()
	players = PlayerCollection(gameDisplay)


	#ey = Enemy(gameDisplay, 700, enemy_y)

	while running:

		dt = clock.tick(fps)
		game_time += dt

		gameDisplay.fill(green)
		pygame.draw.rect(gameDisplay, red, [0,390, screen_w, 200])
		pygame.draw.line(gameDisplay, black, (0,390), (screen_w,390), 5)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				running = False

		#keys = pygame.key.get_pressed()

		#if not(player.isJump):
		#	if keys[pygame.K_SPACE]:
		#		player.isJump = True
		#else:
		#	players.jump()
				

		
		enemy.update(dt)
		num_alive = players.update(dt, enemy.enemies)

		if num_alive == 0:
			printMSG(gameDisplay, "DEAD", 400, 200, 30)

			enemy.create_new_set()
			game_time = 0
			players.create_new_generation()
			num_of_iterations += 1



		update_data_labels(gameDisplay, dt, game_time, label_font, num_of_iterations, num_alive)
		pygame.display.update()


if __name__ == "__main__":
	main()