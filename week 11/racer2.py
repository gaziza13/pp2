import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


w = 400
h = 600
SPEED = 5
SCORE = 0
MONEY = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

street = pygame.image.load("street.png")


sc = pygame.display.set_mode((400, 600))
sc.fill(WHITE)
pygame.display.set_caption("Game")

coin_surf = pygame.image.load("coin.png")
coin_surf = pygame.transform.scale(coin_surf, (coin_surf.get_width() // 8, coin_surf.get_height() // 8))

x, x1, = None, None


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global SCORE
        global x
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)
            x = self.rect.center


class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(coin_surf, (coin_surf.get_width() // 5, coin_surf.get_height() // 5))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def move(self):
        global x1
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)
            x1 = self.rect.center


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < w:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


p = Player()
e1 = Enemy()
e2 = coin()

enemies = pygame.sprite.Group()
enemies.add(e1)
coins = pygame.sprite.Group()
coins.add(e2)
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

s = 0


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # анимируем движущийся фон
    sc.blit(pygame.transform.scale(street, (w, h)), (0, s % h))
    sc.blit(pygame.transform.scale(street, (w, h)), (0, -h + (s % h)))
    s += SPEED / 2

    scores = font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (10, 575))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        sc.blit(entity.image, entity.rect)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(p, enemies):
        time.sleep(1)

        sc.fill(RED)
        sc.blit(game_over, (30, 250))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    for entity in coins:
        entity.move()
        sc.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(e1, coins):
        e2.center = (random.randint(30, w - 30), 0)
    if pygame.sprite.spritecollideany(p, coins):
        x != x1
    for c in coins:
        if pygame.sprite.collide_rect(p, c):  # если игровая машинка получит монетку
            c.kill()
            MONEY += 200
            new = coin()  # заново создаем объект монетки
            coins.add(new)  # добавляем новый объект в группу
    money = font_small.render(str(MONEY), True, BLACK)
    sc.blit(money, (200, 10))
    pygame.display.update()
    clock.tick(60)