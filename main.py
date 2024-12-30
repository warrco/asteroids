import pygame
from constants import *
from player import Player

def main():
    #Initialize pygame and set the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Set frame-rate
    clock = pygame.time.Clock()
    dt = 0

    #Set up player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #draw the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        #limit FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()