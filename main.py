import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

player_width = 64
player_height = 64
player_pos = [screen_width // 2 - player_width //
              2, screen_height - player_height - 10]
player_speed = 5

alien_width = 64
alien_height = 64
alien_pos = [random.randint(
    0, screen_width - alien_width), random.randint(50, 150)]
alien_speed = 0.5

bullet_width = 8
bullet_height = 24
bullet_pos = [0, 0]
bullet_speed = 7
bullet_state = "ready"

score = 0

player_img = pygame.image.load("images/player.jpg")
alien_img = pygame.image.load("images/alien.jpg")


def draw_player():
    screen.blit(player_img, player_pos)


def draw_alien():
    screen.blit(alien_img, alien_pos)


def move_player(direction):
    global player_pos
    if direction == "left":
        player_pos[0] -= player_speed
    elif direction == "right":
        player_pos[0] += player_speed
    if player_pos[0] < 0:
        player_pos[0] = 0
    elif player_pos[0] > screen_width - player_width:
        player_pos[0] = screen_width - player_width


def fire_bullet():
    global bullet_state, bullet_pos
    if bullet_state == "ready":
        bullet_state = "fired"
        bullet_pos = [player_pos[0] + player_width // 2 -
                      bullet_width // 2, player_pos[1] - bullet_height]


def move_bullet():
    global bullet_pos, bullet_state
    if bullet_state == "fired":
        bullet_pos[1] -= bullet_speed
        if bullet_pos[1] < 0:
            bullet_state = "ready"


def detect_collision():
    global score, alien_pos, bullet_pos, bullet_state
    distance = ((alien_pos[0] - bullet_pos[0]) ** 2 +
                (alien_pos[1] - bullet_pos[1]) ** 2) ** 0.5
    if distance < 32:
        score += 1
        alien_pos = [random.randint(
            0, screen_width - alien_width), random.randint(50, 150)]
        bullet_state = "ready"


def draw_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def game_over():
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (screen_width //
                2 - 100, screen_height // 2 - 18))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()


def game_victory():
    font = pygame.font.Font(None, 36)
    victory_text = font.render("Victory!", True, (0, 255, 0))
    screen.blit(victory_text, (screen_width //
                2 - 70, screen_height // 2 - 18))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    quit()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player("left")
            elif event.key == pygame.K_RIGHT:
                move_player("right")
            elif event.key == pygame.K_SPACE:
                fire_bullet()

    move_bullet()
    detect_collision()

    if alien_pos[1] > screen_height - alien_height:
        game_over()

    alien_pos[1] += alien_speed
    if alien_pos[1] > screen_height:
        game_victory()

    screen.fill((0, 0, 0))
    draw_player()
    draw_alien()
    draw_score()

    if bullet_state == "fired":
        pygame.draw.rect(screen, (255, 255, 255),
                         (bullet_pos[0], bullet_pos[1], bullet_width, bullet_height))

    pygame.display.flip()

pygame.quit()
quit()
