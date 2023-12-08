

import pygame

from functoins import load_image




if __name__== '__main__':
    pygame.init()
    SIZE = WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode(SIZE)
    all_sprites = pygame.sprite.Group()
    pygame.display.set_caption('Мой курсор')
    running = True
    cursor_image = load_image('cursor.png')
    cursor = pygame.sprite.Sprite()
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()
    all_sprites.add(cursor)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                cursor.rect.x = x
                cursor.rect.y = y
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

