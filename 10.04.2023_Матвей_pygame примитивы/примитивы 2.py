import pygame

pygame.init()

width = 300
height = 300

colors = [
    pygame.Color("red"),
    pygame.Color("orange"),
    pygame.Color("yellow"),
    pygame.Color("green"),
    pygame.Color("blue"),
    pygame.Color("indigo"),
    pygame.Color("violet")
]

current_color_index = 0

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Program")

square_x = 145
square_y = 145
square_size = 10

move_left = False
move_right = False
move_up = False
move_down = False

trail_surface = pygame.Surface((width, height))
trail_surface.set_alpha(128)  # Установка прозрачности следа

running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Обработка нажатия клавиш
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_c:
                # Смена цвета клавишей "C"
                current_color_index = (current_color_index + 1) % len(colors)
        elif event.type == pygame.KEYUP:
            # Обработка отпускания клавиш
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down = False

    if move_left and square_x > 0:
        square_x -= 1
    elif move_right and square_x < width - square_size:
        square_x += 1
    elif move_up and square_y > 0:
        square_y -= 1
    elif move_down and square_y < height - square_size:
        square_y += 1

    trail_surface.fill((0, 0, 0))  # Очистка следа
    trail_surface.set_colorkey((0, 0, 0))  # Установка прозрачности для фона следа
    trail_surface.fill(colors[current_color_index], (square_x, square_y, square_size, square_size))

    window.blit(trail_surface, (0, 0))  # Отображение следа
    pygame.draw.rect(window, colors[current_color_index], (square_x, square_y, square_size, square_size))

    pygame.display.flip()

    pygame.time.delay(10)

pygame.quit()
