"""
Section 5: Polish & Finishing Touches

This section introduces the final polish to make Pong feel complete:
- Audio integration (paddle hits, wall bounces, scoring, background music).
- Helper text displayed mid-game for modifier keys.
- Live value readouts showing CPU speed, Player speed, and Ball speed.
- Win condition (first to 3) and results screen with winner message.
- Quick navigation: press [1] anytime to return to the Menu.

Press 1 to switch to the Menu state.
Press 2 to start the Game state.
Press SPACE to launch the ball once the game has begun.
Use keys [3–8] to adjust CPU, Player, and Ball speeds in real-time.
"""

import pygame
from game import Game

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
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