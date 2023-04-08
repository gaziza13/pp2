import pygame, datetime

pygame.init()

s = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
w = 800 // 2
h = 800 // 2

mickey = pygame.image.load("main-clock.png")
left = pygame.image.load("left-hand.png")
right = pygame.image.load("right-hand.png")
mickeyRect = mickey.get_rect(center=(w, h))
s.blit(mickey, (w, h))


def rotate(s, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    s.blit(rotated_image, new_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    s.blit(mickey, mickeyRect)
    t = datetime.datetime.now()
    minute, second = t.minute, t.second

    lang = (74.5 - t.second) * 6
    rang = (440 - t.minute) * 6
    rotate(s, left, (w, h), lang)
    rotate(s, right, (w, h), rang)
    pygame.display.flip()
    clock.tick(0)