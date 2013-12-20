# RYUYA'S GAME
# VERSION 0.0.0.1
# THIS IS STILL IN TESTING
# YOU WILL NEED PYTHON AND PYGAME FOR THIS APP TO WORK



import pygame, sys # for game
from pygame.locals import * # use everything pygame
from pygame import * # use everything pygame
import time # used for delays
import random # used for enemies



# colors
red = (255, 0, 0)
dark_red = (150, 50, 50)
green = (0, 255, 0)
dark_green = (50, 150, 50)
blue = (0, 0, 255)
dark_blue = (50, 50, 150)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (100, 100, 100)



# keyboard input
escape = K_ESCAPE
spacebar = K_SPACE
left = K_LEFT
right = K_RIGHT
a = K_a
d = K_d
p = K_p
u = K_u



# object classes
class Ship(object): # makes the ship
	def __init__(self):
		self.image = pygame.image.load("ship.png") # ship's image
		self.x = 400 # x coordinate of ship
		self.y = 500 # y coordinate of ship

	def handle_keys(self):
		key = pygame.key.get_pressed() # records what keys were pressed
		dist = 5 # how many pixels per frame
		if ((key[left]) or (key[a])): # moves ship left if a or left is pressed
			self.x -= dist # moves ship left
		elif ((key[right]) or (key[d])): # moves ship right if d or right is pressed
			self.x += dist # moves ship right

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y)) # draws enemy


class Enemy(object):
	def __init__(self, filename, x, y):
		self.image = pygame.image.load(filename)
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))


class Miniboss(object):
	def __init__(self, filename, x, y):
		self.image = pygame.image.load(filename)
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))


class Boss(object):
	def __init__(self, filename, x, y):
		self.image = pygame.image.load(filename)
		self.x = x
		self.y = y

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))


class Score(object): # score counter
	def __init__(self):
		font2 = pygame.font.Font("press_start.ttf", 14) # font setup
		counter = "0"
		int(counter)
		self.text = font2.render("Score:", False, white, grey) # text for score
		self.textbox = self.text.get_rect() # background
		self.textbox.topright = (790, 3) # align to top right

		str(counter)
		self.score = font2.render(counter, False, white, black) # score text
		self.scorebox = self.score.get_rect() # score background
		self.scorebox.topright = (790, 28) # align to top right

	def counter(self): # score counter increase
		increase = 100
		bigIncrease = 1000
		hugeIncrease = 10000
		"""if (enemy killed):
			counter += increase
		elif (miniboss killed):
			counter += bigIncrease
		elif (boss killed):
			counter += hugeIncrease
"""
	def draw(self, surface):
		surface.blit(self.text, self.textbox)
		surface.blit(self.score, self.scorebox)



pygame.init() # window
display = pygame.display.set_mode((800, 600)) # window size
pygame.display.set_caption("Space Battle")
fps = pygame.time.Clock() # fps clock


font = pygame.font.Font("press_start.ttf", 14) # font setup
text = font.render("Press 'Escape' to exit.", False, white, grey)
textbox = text.get_rect()
textbox.topleft = (10, 3)


ship = Ship() # the ship object
score = Score() # score object

# ENEMIES
enemy1 = Enemy("enemy1.png", 400, 100)
first_wave = [enemy1]


while True: # main game loop
	for event in pygame.event.get(): # main frame update loop
		if (event.type == KEYUP and event.key == escape): # press escape to quit
			pygame.quit() # closes window
			sys.exit() # quits application
		elif (event.type == QUIT):
			pygame.quit()
			sys.exit

	display.fill(black)

	pygame.draw.rect(display, grey, (0, 0, 800, 20)) # draws a rectangle
	display.blit(text, textbox) # draws text

	ship.handle_keys() # controls ship movements
	ship.draw(display) # draws ship

	enemy1.draw(display)

	score.counter()
	score.draw(display)

	pygame.display.update() # makes frames update
	fps.tick(60) # makes max fps 60
