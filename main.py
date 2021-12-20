import pygame
import random
import time
import numpy

# Initialize
pygame.init()
# Create the screen
screen = pygame.display.set_mode((1400, 1000))

# Title formatting
pygame.display.set_caption("War Star Arcade Game")
icon = pygame.image.load('war-star.png')
pygame.display.set_icon(icon)

# Player Ship image
shipImg = pygame.image.load('warstarship.png')
shipImg = pygame.transform.scale(shipImg, (1420, 1020))  # Scale it to the size of the window
# X and Y positions for movement later
shipImgX = -15
shipImgY = -15

# Enemy Ship image
enemyImg = pygame.image.load('warstarenemy.png')
enemyImg = pygame.transform.scale(enemyImg, (10, 10))  # Scale it to smaller size
# X and Y positions for movement later
enemyImgX = random.randint(0, 1400)
enemyImgY = random.randint(0, 1000)
enemyScale = 10
enemyX_change = 0
enemyY_change = 0
enemy_shot_status = False


def ship(x, y):
    screen.blit(shipImg, (x, y))


def enemy(passImg, scale, x, y):
    # Enemy movement
    if not enemy_shot_status:
        if 1000 >= y >= 0 and 1400 >= x >= 0:
            rand_num = random.randint(1, 4)
            if rand_num == 1:
                y += 3
                x *= 3
                scale *= numpy.log(scale ** 2)
            elif rand_num == 2:
                y -= 3
                x *= 3
                scale *= numpy.log(scale ** 2)
            elif rand_num == 3:
                y += 3
                x /= 3
                scale *= numpy.log(scale ** 2)
            elif rand_num == 4:
                y -= 3
                x /= 3
                scale *= numpy.log(scale ** 2)

    passImg = pygame.transform.scale(passImg, (scale, scale))
    screen.blit(passImg, (x, y))


# Loop to be sure the game doesn't close down
running = True
level = 1
while running:
    screen.fill((0, 0, 10))  # Dark blue background color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if the game is closed by X button
            running = False  # quit out of the game

        # Mouse movement
        if event.type == pygame.MOUSEMOTION:
            shipImgPos = pygame.mouse.get_pos()

    # Game refreshing
    enemy(enemyImg, enemyScale, enemyImgX, enemyImgY)
    ship(shipImgPos[0] / 62 - 20, shipImgPos[1] / 62 - 20)

    pygame.display.update()
