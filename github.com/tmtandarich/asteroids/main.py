import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import *
from circleshape import *
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000
        
        player.update(dt)

        log_state()
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        
    
        




if __name__ == "__main__":
    main()
