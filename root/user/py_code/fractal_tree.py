import math

import pygame
import colour


def main():
    pygame.init()

    size = width, height = 800, 800
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    screen.fill(black)
    depth = 15

    start_colour = colour.Color('green')
    generated_colours = list(start_colour.range_to(colour.Color('blue'),
                                                   depth))

    colours = []
    for generated_colour in generated_colours:
        rgb = generated_colour.rgb
        colours.append((rgb[0] * 255, rgb[1] * 255, rgb[2] * 255))

    def fractal_tree(order,
                     theta,
                     size,
                     start_x,
                     start_y,
                     heading,
                     color=(255, 255, 255),
                     depth=0):
        trunk_ratio = 0.33
        yield
        trunk = size * trunk_ratio
        delta_x = trunk * math.cos(heading)
        delta_y = trunk * math.sin(heading)
        new_pos = (start_x + delta_x, start_y + delta_y)
        pygame.draw.line(screen, colours[order - 1], (start_x, start_y),
                         new_pos)
        pygame.display.update()

        yield
        if order != 0:
            right_running = True
            left_running = True
            new_size = size * (1 - trunk_ratio)
            left_tree = fractal_tree(order - 1, theta, new_size, new_pos[0],
                                     new_pos[1], heading - theta, color,
                                     depth + 1)
            try:
                next(left_tree)
            except StopIteration:
                left_running = False

            right_tree = fractal_tree(order - 1, theta, new_size, new_pos[0],
                                      new_pos[1], heading + theta, color,
                                      depth + 1)
            try:
                next(right_tree)
            except StopIteration:
                right_running = False

            while right_running and left_running:
                try:
                    next(left_tree)
                except StopIteration:
                    left_running = False
                try:
                    next(right_tree)
                except StopIteration:
                    right_running = False
                yield

    fractal_generator_left = fractal_tree(depth, math.pi / 8, width // 2,
                                          width // 2, height // 2, math.pi)
    fractal_generator_right = fractal_tree(depth, math.pi / 8, width // 2,
                                           width // 2, height // 2, 0)
    fractal_generator_up = fractal_tree(depth, math.pi / 8, width // 2,
                                        width // 2, height // 2, -math.pi / 2)
    fractal_generator_down = fractal_tree(depth, math.pi / 8, width // 2,
                                          width // 2, height // 2, math.pi / 2)

    next(fractal_generator_left)
    next(fractal_generator_right)
    next(fractal_generator_up)
    next(fractal_generator_down)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                             and event.key == pygame.K_ESCAPE):
                done = True
        try:
            next(fractal_generator_left)
            next(fractal_generator_right)
            next(fractal_generator_up)
            next(fractal_generator_down)
        except StopIteration:
            pass

    pygame.display.update()


if __name__ == "__main__":
    main()
