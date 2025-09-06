"""
Section 4: Scoring & Full Game Loop.

This section introduces:
- Player paddle movement (W/S or Up/Down keys).
- Opponent paddle (simple CPU that follows the ball).
- Ball collisions with paddles.
- Ball reset when leaving the screen.

Press 1 to switch to the Menu state.
Press 2 to switch to the Game state.
Press SPACE to start the ball once in the Game state.

As is, the CPU cannot lose. In Section 5, we will address this in a few ways
"""

import pygame
from game import Game

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

        game.run(events, screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()