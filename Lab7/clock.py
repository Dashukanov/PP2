import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((829, 836)) #1500 900

done = False
clock = pygame.time.Clock()

background = pygame.image.load(r"C:\Users\admin\Desktop\pp2\lab7\clock\without arms .png")
left_arm_aka_second = pygame.image.load(r"C:\Users\admin\Desktop\pp2\lab7\clock\left arm.png")
right_arm_aka_minute = pygame.image.load(r"C:\Users\admin\Desktop\pp2\lab7\clock\right arm.png")

rect = background.get_rect(center=(415, 418))

while not done:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    second_angle = -(time.second * 6)
    nsec_img = pygame.transform.rotate(left_arm_aka_second, second_angle)
    second_rect = nsec_img.get_rect(center = rect.center)
    screen.blit(nsec_img, second_rect.topleft)

    minute_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(right_arm_aka_minute, minute_angle)
    minute_rect = nmin_img.get_rect(center = rect.center)
    screen.blit(nmin_img, minute_rect.topleft)

    pygame.display.flip()
    clock.tick(60)


