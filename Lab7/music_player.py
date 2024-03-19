import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((960, 600))
done = False
songs = ['C:/Users/admin/Desktop/pp2/lab7/music songs/7vvch - Born to Fly.mp3',
         'C:/Users/admin/Desktop/pp2/lab7/music songs/Duke Dumont - Ocean Drive.mp3',
         'C:/Users/admin/Desktop/pp2/lab7/music songs/Mother Mother - Hayloft.mp3',
         'C:/Users/admin/Desktop/pp2/lab7/music songs/my!lane - This Feeling.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("C:/Users/admin/Desktop/pp2/lab7/music songs/neon-background-5120x2880-12487.jpg")
background_rect = background_image.get_rect()

while not done:
    if i == 3:
        background_image = pygame.image.load("C:/Users/baurs/Desktop/pp2/lab7/music songs/pngtree-city-street-neon-background-image_1948831.jpg")
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    else:
        background_image = pygame.image.load("C:/Users/baurs/Desktop/pp2/lab7/music songs/neon-background-5120x2880-12487.jpg")
        background_rect = background_image.get_rect()
        screen.blit(background_image, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.stop()
                    a = False
                else:
                    pygame.mixer.music.play()
                    a = True

    pygame.display.flip()

