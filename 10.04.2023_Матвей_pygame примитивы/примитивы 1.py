import pygame

pygame.init()

screen = pygame.display.set_mode((1, 1))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                key_name = "Нажата клавиша Enter"
            elif event.key == pygame.K_SPACE:
                key_name = "Нажата клавиша Space"
            elif event.key == pygame.K_w:
                key_name = "Нажата клавиша W"
            elif event.key == pygame.K_a:
                key_name = "Нажата клавиша A"
            elif event.key == pygame.K_s:
                key_name = "Нажата клавиша S"
            elif event.key == pygame.K_d:
                key_name = "Нажата клавиша D"
            elif event.key == pygame.K_ESCAPE:
                key_name = "Нажата клавиша Esc"
            elif event.key == pygame.K_LEFT:
                key_name = "Нажата клавиша Left Arrow"
            elif event.key == pygame.K_RIGHT:
                key_name = "Нажата клавиша Right Arrow"
            elif event.key == pygame.K_UP:
                key_name = "Нажата клавиша Up Arrow"
            elif event.key == pygame.K_DOWN:
                key_name = "Нажата клавиша Down Arrow"
            else:
                continue

            print(key_name)

pygame.quit()

