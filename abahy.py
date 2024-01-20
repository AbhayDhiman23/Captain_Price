import pygame
import random
import math


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")


icon = pygame.image.load("001-ufo-flying.png")
pygame.display.set_icon(icon)


player_img = pygame.image.load("002-arcade-game.png")
playerX = 370
playerY = 480
playerX_change = 0


enemy_img = pygame.image.load("003-alien.png")
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)


bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

score = 0

font = pygame.font.Font(None, 32)
textX = 10
textY = 10

def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_display, (x, y))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    
    playerX += playerX_change

    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i])

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()

pygame.quit()


print("Hello World ")