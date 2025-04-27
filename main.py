import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill((0, 0, 0))  ##### FIX FILL COLOR BLACK
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
if __name__ == "__main__":
    main()