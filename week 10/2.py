import pygame
import os

pygame.init()

w = 650
h = 650
s = pygame.display.set_mode((w, h))
pygame.display.set_caption("gaziza's playlist")
s.fill('black')
pygame.display.flip()
clock = pygame.time.Clock()

path = 'C://Users//User//Desktop//labbs//week 10'
mix = [
    'die.mp3',
    'lana.mp3',
    'lil.mp3',
    'ngh.mp3',
]
dem = 'die.mp3'

lana = pygame.transform.scale(pygame.image.load("lana.png"), (500, 500))
com = pygame.transform.scale(pygame.image.load("compass.png"), (500, 500))
die = pygame.transform.scale(pygame.image.load("die.png"), (500, 500))
drive = pygame.transform.scale(pygame.image.load("drive.png"), (500, 500))

photo = lana

pygame.mixer.music.load(os.path.join(path, dem))
state = 'stopped'
cnt = 0

def play_m():
    global state
    pygame.mixer.music.play()
    state = 'playing'


def pause_m():
    global state
    pygame.mixer.music.pause()
    state = 'paused'


def stop_m():
    global state
    pygame.mixer.music.stop()
    state = 'stopped'


def next_m():
    global cnt, dem
    cnt = (cnt + 1) % len(mix)
    dem = mix[cnt]
    pygame.mixer.music.load(os.path.join(path, dem))
    play_m()


def prev_m():
    global cnt, dem
    cnt = (cnt - 1) % len(mix)
    dem = mix[cnt]
    pygame.mixer.music.load(os.path.join(path, dem))
    play_m()


change = False
track = None
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if state == 'playing':
                    pause_m()
                elif state == 'paused':
                    play_m()
                else:
                    play_m()
            elif i.key == pygame.K_DOWN:
                stop_m()
            elif i.key == pygame.K_RIGHT:
                next_m()
            elif i.key == pygame.K_LEFT:
                prev_m()
    if pygame.mixer.music.get_busy() and dem != track:
        track = dem
        for i in range(len(mix)):
            if dem == mix[i]:
                photo = [die, lana, drive, com][i]
                change = True
                break
    if change:
        s.blit(photo, (50, 10))
        pygame.display.flip()
        change = False
    clock.tick(60)


pygame.display.update()
