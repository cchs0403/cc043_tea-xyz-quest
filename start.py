import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Side-Scroller Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

player_image = pygame.image.load("player.png")
player_x = 100
player_y = 300
screen.blit(player_image, (player_x, player_y))

pygame.display.update()

background_image = pygame.image.load("background.png")
background_x = 0