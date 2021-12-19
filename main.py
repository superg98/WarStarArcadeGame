import pygame
import random
import time

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
shipImgX = -10
shipImgY = -10

# Enemy Ship image
enemyImg = pygame.image.load('warstarenemy.png')
enemyImg = pygame.transform.scale(enemyImg, (10, 10))  # Scale it to the size of the window
# X and Y positions for movement later
enemyImgX = random.randint(0, 1400)
enemyImgY = random.randint(0, 1000)
enemyX_change = 0
enemyY_change = 0
enemyScale = 10
enemy_shot_status = False


def ship(x, y):
    screen.blit(shipImg, (x, y))


def enemy(passImg, x, y):
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

        # Enemy movement
        if not enemy_shot_status and 1000 >= enemyImgY >= 0 and 1400 >= enemyImgX >= 0:
            enemyImgY += random.randint(-5, 5)
            enemyImgX += random.randint(-5, 5)
            enemyImg = pygame.transform.scale(enemyImg, (random.randint(1, 5), random.randint(1, 5)))  # Scale it slowly
        elif not enemy_shot_status and not 1000 >= enemyImgY >= 0 or not 1400 >= enemyImgX >= 0:
            enemyImgY += random.randint(5, -5)
            enemyImgX += random.randint(5, -5)
            enemyImg = pygame.transform.scale(enemyImg, (random.randint(1, 5), random.randint(1, 5)))  # Scale it slowly
        elif enemy_shot_status:
            enemy.kill()

    # Game refreshing
    enemy(enemyImg, enemyImgX, enemyImgY)
    ship(shipImgPos[0] / 75 - 20, shipImgPos[1] / 75 - 20)

    pygame.display.update()
