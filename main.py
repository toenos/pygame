import pygame
from constants import *
from player import Player
<<<<<<< Updated upstream
=======
from asteroid import Asteroid
from asteroidfield import AsteroidField

>>>>>>> Stashed changes

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
<<<<<<< Updated upstream
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
=======

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
>>>>>>> Stashed changes

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
<<<<<<< Updated upstream
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #60 FPS
=======

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
>>>>>>> Stashed changes
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
