import time
import pygame

pygame.init()

size = width, height = 800, 800
grey = 125, 125, 125

screen = pygame.display.set_mode(size)
screen.fill(grey)


def serpinski_triangle(radius, min_radius, x_pos, y_pos):
    if radius > min_radius:
        pygame.draw.circle(screen,(0, 0, 0), (x_pos, y_pos), radius, 1)
        yield
        right_circle = serpinski_triangle(radius // 2, min_radius,
                                          x_pos + radius // 2, y_pos)
        down_circle = serpinski_triangle(radius // 2, min_radius, x_pos,
                                         y_pos - radius // 2)
        left_circle = serpinski_triangle(radius // 2, min_radius,
                                         x_pos - radius // 2, y_pos)

        done = False
        while not done:
            done = True
            try:
                next(right_circle)
                done = False
            except StopIteration:
                pass
            try:
                next(down_circle)
                done = False
            except StopIteration:
                pass
            try:
                next(left_circle)
                done = False
            except StopIteration:
                pass

            yield

generator = serpinski_triangle(400, 2, width // 2, height // 2)
pygame.display.update()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_ESCAPE):
            done = True
    try:
        next(generator)
    except StopIteration:
        pass
    pygame.display.update()
    time.sleep(0.75)