import pygame
from PIL import Image
import glob

pygame.init()

display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
img1 = pygame.image.load('Image1.png')

image_list = []
for filename in glob.glob('/Users/binph/PycharmProjects/CSVParser/ocean frames/*.gif'):
    im = pygame.image.load(filename)
    print(1)
    image_list.append(im)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("hi")
clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

            print(event)
    num = 0
    file = 'some.mp3'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.event.wait()
    while num < 100:
        for im in image_list:
            gameDisplay.blit(im, (0, 0))
            pygame.display.flip()
            pygame.time.wait(100)
            num = num+1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

