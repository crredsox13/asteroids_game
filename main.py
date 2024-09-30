import pygame

from constants import *

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
      screen.fill((255,255,255))  
      pygame.display.flip()

if __name__ == "__main__":
    main()