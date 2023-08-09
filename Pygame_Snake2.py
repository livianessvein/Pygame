import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


# definição para a movimentação da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Cobra')

cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pygame.Surface((10, 5))
cobra_skin.fill((0, 128, 0))  # verde

#maçã
maca_pos = on_grid_random()
maca = pygame.Surface((10, 10))
maca = pygame.image.load('maca.png')
DEFAULT_IMAGE_SIZE = (20, 20)
maca = pygame.transform.scale(maca, DEFAULT_IMAGE_SIZE)
DEFAULT_IMAGE_POSITION = (200,200)
screen.blit(maca,DEFAULT_IMAGE_POSITION)


my_direction = LEFT

relogio = pygame.time.Clock()

fonte = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    relogio.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if colisao(cobra[0], maca_pos):
        maca_pos = on_grid_random()
        cobra.append((0, 0))
        score = score + 1

    # Para checar se a cobra colidiu com as laterais (bordas)
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break

    # Para checar se a cobra bateu nela mesma. 
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    # Para fazer a cobra se mexer. 
    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill((0, 0, 0))
    screen.blit(maca, maca_pos)

    for x in range(0, 600, 10):  #para desenhar linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # para desenhar linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = fonte.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in cobra:
        screen.blit(cobra_skin, pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()