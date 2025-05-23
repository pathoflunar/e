import pygame
from pygame import *

# ----------------------------------------------------

window = pygame.display.set_mode((700, 500))
display.set_caption('NotCatchUp')

# ----------------------------------------------------

background = transform.scale(
    image.load('background.png'),
    (700, 500)
)

sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)

sprite2 = transform.scale(
    image.load('sprite2.png'),
    (100, 100)
)

# ----------------------------------------------------

x1 = (200)
y1 = (300)
x2 = (400)
y2 = (300)

speed = 10
clock = time.Clock()

game = True

# ----------------------------------------------------

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    keys_pressed = key.get_pressed()
    if keys_pressed[K_a] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_d] and x1 < 595:
        x1 += speed
    if keys_pressed[K_w] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_s] and y1 < 395:
        y1 += speed
    if keys_pressed[K_LEFT] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_RIGHT] and x2 < 595:
        x2 += speed
    if keys_pressed[K_UP] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_DOWN] and y2 < 395:
        y2 += speed
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(40)
    display.update()

# ----------------------------------------------------

#обработай событие «клик по кнопке "Закрыть окно"»