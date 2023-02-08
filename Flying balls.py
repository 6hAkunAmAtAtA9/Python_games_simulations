import pygame, sys, math, random

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1000, 800
COLORS = ['yellow', 'aqua', 'white', 'royalblue', 'pink', 'lightsalmon', 'lightcyan', 'springgreen' ]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
dots = []
timer = 0

while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if timer % 100 == 0 and len(dots) < 300:
        random_position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        random_colors = [random.choice(COLORS) for _ in range(3)]
        for _ in range(50):
            dots.append({'x': random_position[0], 'y': random_position[1],
                         'x_change': random.uniform(-1, 1),
                         'y_change': random.uniform(-1, 1),
                         'size': random.randint(1, 10),
                         "speed_x": random.uniform(0.2, 0.5),
                         "speed_y": random.uniform(0.2, 0.5),
                         'color': random.choice(random_colors),
                         'tail': [],
                         'life_time': 1
                         })

    for dot in dots:
        if dot['life_time'] % int(150 - (dot['speed_x'] + dot['speed_y']) * 100) == 0:
            if len(dot['tail']) > 5:
                del dot['tail'][0]
            dot['tail'].append((dot['x'], dot['y']))
        dot['x'] += dot['x_change'] * dot['speed_x']
        dot['y'] += dot['y_change'] * dot['speed_y'] + dot['life_time'] / 1500
        pygame.draw.circle(screen, dot['color'], (dot['x'], dot['y']), dot['size'], dot['size'] // 2)
        for closeness, tail_elem in enumerate(dot['tail'][::-1]):
            pygame.draw.circle(screen, dot['color'], tail_elem, dot['size'] - closeness, dot['size'] // 2)
        dot['life_time'] += 1

    dots = [x for x in dots if x['y'] < (HEIGHT + 500)]
    pygame.display.flip()
    timer += 1
    clock.tick(120)

