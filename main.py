import pygame
import random

# intalize the pygame
pygame.init()
# background
background = pygame.image.load("background.png")

# create the screen
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

# Bullet
# Ready - you can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_changes = 0
bulletY_changes = 10
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# game loop
running = True
while running:
    # background color change
    screen.fill((150, 50, 50))
    # Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its left key or right key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                bullet_fire(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundaries of spaceship so it doesn't go out bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # checking for boundaries of enemy so it doesn't go out bounds
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -5
        enemyY += enemyY_change

    # Bullet movement
    if bullet_state is "fire":
        bullet_fire(playerX, bulletY)
        bulletY -= bulletY_changes

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()