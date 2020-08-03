import pygame
from defs import *
from enemy import EnemyCollection
from player import Player
import time

def update_label(data, title, font, x, y, gameDisplay):
	label = font.render("{} {}".format(title, data), 1, font_color)
	gameDisplay.blit(label, (x, y))
	return y

def update_data_labels(gameDisplay, dt, game_time, font, num_of_iterations, latest_score, best_score):
	y_pos = 10
	gap = 20
	x_pos = 10
	y_pos = update_label(round(1000/dt, 2), "FPS: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(round(game_time/1000, 2), "Game Time: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(num_of_iterations, "Number of games played: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label("", "", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(game_time, "Score: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(latest_score, "Latest Score: ", font, x_pos, y_pos + gap, gameDisplay)
	y_pos = update_label(best_score, "Best Score: ", font, x_pos, y_pos + gap, gameDisplay)


def printMSG(gameDisplay, msg, x, y, size):
	# Define font and size
	font = pygame.font.Font(None, size)
	# Define what message to display and it's color
	text_surface = font.render(msg, True, (0, 0, 0))
	# Print the message to screen using coordinates
	gameDisplay.blit(text_surface, (x,y))

def check_speed(game_time, score_multiplier, enemy_speed):
	#print(game_time)
	if game_time == (5000 * score_multiplier):
		print(enemy_speed)
		enemy_speed += 1
		score_multiplier += 1

def main():

	pygame.init()
	gameDisplay = pygame.display.set_mode((screen_w, screen_h))
	pygame.display.set_caption("Jumping Game 2!")

	running = True
	label_font = pygame.font.Font(None, font_size)

	clock = pygame.time.Clock()
	dt = 0
	game_time = 0
	num_of_iterations = 1
	latest_score = 0
	best_score = 0
	score_multiplier = 1
	it = 0

	enemy = EnemyCollection(gameDisplay)
	enemy.create_new_set()
	player = Player(gameDisplay)


	while running:

		dt = clock.tick(fps)
		game_time += dt
		it += 1

		gameDisplay.fill(green)
		pygame.draw.rect(gameDisplay, red, [0,390, screen_w, 200])
		pygame.draw.line(gameDisplay, black, (0,390), (screen_w,390), 5)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


		keys = pygame.key.get_pressed()

		if not(player.isJump):
			if keys[pygame.K_SPACE]:
				player.isJump = True
		else:
			player.jump()


		if it == 150 * score_multiplier:
			enemy.update_speed()
			score_multiplier += 1

		enemy.update(dt)
		player.update(dt, enemy.enemies)

		if player.state == player_dead:
			enemy.create_new_set()
			enemy.reset_speed()
			score_multiplier = 1
			it = 0
			latest_score = game_time
			if latest_score >= best_score:
				best_score = latest_score
			game_time = 0
			player = Player(gameDisplay)
			num_of_iterations += 1


		update_data_labels(gameDisplay, dt, game_time, label_font, num_of_iterations, latest_score, best_score)
		pygame.display.update()


if __name__ == "__main__":
	main()