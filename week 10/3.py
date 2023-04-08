import pygame

pygame.init()
w = 800
h = 600

s = pygame.display.set_mode((w, h))

x = w // 2
y = h // 2
rad = 25

def ball():
    pygame.draw.circle(s, (255, 0, 0), (x, y), rad)


run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                y -= 20
            elif i.key == pygame.K_DOWN:
                y += 20
            if i.key == pygame.K_LEFT:
                x -= 20
            elif i.key == pygame.K_RIGHT:
                x += 20
        if x - rad < 0:
            x = rad
        elif x + rad > w:
            x = w - rad
        if y - rad < 0:
            y = rad
        elif y + rad > h:
            y = h- rad

    s.fill((255, 255, 255))
    ball()
    pygame.display.update()

pygame.quit()