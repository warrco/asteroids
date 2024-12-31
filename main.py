import pygame
import sys
from constants import *
from circleshape import CircleShape
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #Initialize pygame and set the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set frame-rate
    clock = pygame.time.Clock()
    dt = 0

    #Create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Set up containers
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable)

    #Initializations
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #draw the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updateable:
            obj.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                sys.exit("Game over!")
        
        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        #limit FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()