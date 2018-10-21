import webbrowser
from PIL import Image
webbrowser.open("https://youtu.be/f2MOXW6uBf8")
import pygame
import sys
import time
import random
import codecs
from pygame.locals import *

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [300, 300]
    bg = [255, 255, 255]

    screen = pygame.display.set_mode(size)

    button = pygame.Rect(75, 75, 150, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    run("CSVParse.py")

        screen.fill(bg)

        pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Results', True, (255, 255, 255), (255, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()