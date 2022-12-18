import pygame
import sys
import random

HEIGHT = 1000
WEIGHT = 2000
CELL_SIZE = 10
BG_COLOR = 'black'

sc = pygame.display.set_mode((WEIGHT, HEIGHT))
field = [[1 if random.random() > 0.90 else 0 for _ in range(WEIGHT // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)]


def neibors(row, col):
    n = 0
    for r in [row-1, row, row+1]:
        for c in [col-1, col, col+1]:
            if (r == row and c == col) or (r < 0 or c < 0) or (r > HEIGHT // CELL_SIZE - 1 or c > WEIGHT // CELL_SIZE - 1):
                continue
            n += field[r][c]
    return n


def field_change():
    nf = [[0 for _ in range(WEIGHT // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)]
    for row_id, row in enumerate(field):
        for col_id, elem in enumerate(row):
            if elem == 1:
                if not 2 <= neibors(row_id, col_id) <= 3:
                    nf[row_id][col_id] = 0
                else:
                    nf[row_id][col_id] = 1
            else:
                if neibors(row_id, col_id) == 3:
                    nf[row_id][col_id] = 1
    return nf

while True:
    sc.fill(BG_COLOR)
    for row_id, row in enumerate(field):
        for col_id, elem in enumerate(row):
            if elem == 1:
                pygame.draw.rect(sc, 'gray',
                                 (col_id * CELL_SIZE, row_id * CELL_SIZE, CELL_SIZE, CELL_SIZE), CELL_SIZE // 3)
    pygame.display.flip()
    field = field_change()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(100)