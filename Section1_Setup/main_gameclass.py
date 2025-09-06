"""
Section 1: Game Class State Manager

This example moves state handling into a Game class.
Press 1 to switch to the Menu state.
Press 2 to switch to the Game state.

In this example, there are no fonts, as all the responsibilities have been placed
on the Game class, therefore, fonts, images and text are handled inside Game instead.
"""

import pygame
from game_class import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    game = Game()
    
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Using a Game class keeps state logic organized and makes it easier to expand than the integrated example.
        game.run(events, screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()